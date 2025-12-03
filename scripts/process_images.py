#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Processamento e Otimização de Imagens
Projeto: Origem das Aves em Theropoda

Este script processa as imagens para otimizar para uso web:
- Redimensionamento (manter proporções)
- Recorte inteligente (crop)
- Compressão (qualidade vs tamanho)
- Conversão de formatos

Requisitos:
    pip install Pillow

Uso:
    python process_images.py
"""

from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path
import json

# ================== CONFIGURAÇÃO ==================

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"
PROCESSED_DIR = PROJECT_ROOT / "images" / "processed"
BACKUP_DIR = PROJECT_ROOT / "images" / "backup"

# Criar diretórios
PROCESSED_DIR.mkdir(exist_ok=True, parents=True)
BACKUP_DIR.mkdir(exist_ok=True, parents=True)

# Configurações de processamento
PROCESSING_PRESETS = {
    "reveal_slide": {
        "max_width": 1200,
        "max_height": 800,
        "quality": 85,
        "format": "JPEG",
        "description": "Otimizado para slides Reveal.js full-width"
    },
    "card_image": {
        "max_width": 600,
        "max_height": 450,
        "quality": 85,
        "format": "JPEG",
        "description": "Otimizado para cards e colunas de duas colunas"
    },
    "thumbnail": {
        "max_width": 300,
        "max_height": 200,
        "quality": 80,
        "format": "JPEG",
        "description": "Miniatura para visualização rápida"
    },
    "high_quality": {
        "max_width": 2000,
        "max_height": 1500,
        "quality": 95,
        "format": "PNG",
        "description": "Alta qualidade para impressão ou zoom"
    }
}

# ================== FUNÇÕES DE PROCESSAMENTO ==================

def resize_image(image, max_width, max_height, maintain_aspect=True):
    """
    Redimensiona uma imagem mantendo proporções.
    
    Args:
        image (PIL.Image): Imagem a redimensionar
        max_width (int): Largura máxima
        max_height (int): Altura máxima
        maintain_aspect (bool): Manter proporção original
    
    Returns:
        PIL.Image: Imagem redimensionada
    """
    if maintain_aspect:
        # Calcular proporção
        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return image
    else:
        # Forçar dimensões exatas (pode distorcer)
        return image.resize((max_width, max_height), Image.Resampling.LANCZOS)


def smart_crop(image, target_width, target_height):
    """
    Recorte inteligente focando no centro da imagem.
    
    Args:
        image (PIL.Image): Imagem original
        target_width (int): Largura desejada
        target_height (int): Altura desejada
    
    Returns:
        PIL.Image: Imagem recortada
    """
    img_width, img_height = image.size
    aspect_ratio = target_width / target_height
    img_aspect_ratio = img_width / img_height
    
    if img_aspect_ratio > aspect_ratio:
        # Imagem mais larga - recortar laterais
        new_width = int(img_height * aspect_ratio)
        offset = (img_width - new_width) // 2
        crop_box = (offset, 0, offset + new_width, img_height)
    else:
        # Imagem mais alta - recortar topo/base
        new_height = int(img_width / aspect_ratio)
        offset = (img_height - new_height) // 2
        crop_box = (0, offset, img_width, offset + new_height)
    
    cropped = image.crop(crop_box)
    return cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)


def enhance_image(image, sharpness=1.2, contrast=1.1, brightness=1.0):
    """
    Aplica melhorias sutis na imagem.
    
    Args:
        image (PIL.Image): Imagem original
        sharpness (float): Fator de nitidez (1.0 = sem mudança)
        contrast (float): Fator de contraste
        brightness (float): Fator de brilho
    
    Returns:
        PIL.Image: Imagem melhorada
    """
    # Nitidez
    if sharpness != 1.0:
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness)
    
    # Contraste
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
    
    # Brilho
    if brightness != 1.0:
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)
    
    return image


def process_image(input_path, output_path, preset="reveal_slide", enhance=False, crop=False):
    """
    Processa uma imagem com base no preset escolhido.
    
    Args:
        input_path (Path): Caminho da imagem original
        output_path (Path): Caminho de saída
        preset (str): Nome do preset de processamento
        enhance (bool): Aplicar melhorias de qualidade
        crop (bool): Aplicar recorte inteligente
    
    Returns:
        dict: Informações sobre o processamento
    """
    try:
        # Carregar imagem
        image = Image.open(input_path)
        original_size = image.size
        original_format = image.format
        original_file_size = input_path.stat().st_size / 1024  # KB
        
        # Converter para RGB se necessário (para salvar em JPEG)
        if image.mode in ('RGBA', 'LA', 'P'):
            # Criar fundo branco
            background = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        elif image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Obter configurações do preset
        config = PROCESSING_PRESETS[preset]
        
        # Aplicar recorte inteligente se solicitado
        if crop:
            image = smart_crop(image, config["max_width"], config["max_height"])
        else:
            # Apenas redimensionar mantendo proporções
            image = resize_image(image, config["max_width"], config["max_height"])
        
        # Aplicar melhorias se solicitado
        if enhance:
            image = enhance_image(image, sharpness=1.2, contrast=1.1)
        
        # Salvar imagem processada
        save_kwargs = {"quality": config["quality"], "optimize": True}
        
        if config["format"] == "JPEG":
            save_kwargs["format"] = "JPEG"
            if not str(output_path).lower().endswith(('.jpg', '.jpeg')):
                output_path = output_path.with_suffix('.jpg')
        elif config["format"] == "PNG":
            save_kwargs["format"] = "PNG"
            save_kwargs.pop("quality")  # PNG não usa quality
            if not str(output_path).lower().endswith('.png'):
                output_path = output_path.with_suffix('.png')
        
        image.save(output_path, **save_kwargs)
        
        # Calcular estatísticas
        new_file_size = output_path.stat().st_size / 1024  # KB
        compression_ratio = (1 - new_file_size / original_file_size) * 100 if original_file_size > 0 else 0
        
        result = {
            "status": "success",
            "input": str(input_path.name),
            "output": str(output_path.name),
            "preset": preset,
            "original_size": original_size,
            "new_size": image.size,
            "original_file_size_kb": round(original_file_size, 2),
            "new_file_size_kb": round(new_file_size, 2),
            "compression_ratio_percent": round(compression_ratio, 2),
            "enhanced": enhance,
            "cropped": crop
        }
        
        print(f"✅ {input_path.name}")
        print(f"   {original_size[0]}x{original_size[1]} → {image.size[0]}x{image.size[1]}")
        print(f"   {original_file_size:.1f}KB → {new_file_size:.1f}KB ({compression_ratio:.1f}% redução)")
        
        return result
        
    except Exception as e:
        print(f"❌ Erro ao processar {input_path.name}: {e}")
        return {
            "status": "error",
            "input": str(input_path.name),
            "error": str(e)
        }


def process_all_images(preset="reveal_slide", enhance=False, crop=False, backup=True):
    """
    Processa todas as imagens da pasta images/
    
    Args:
        preset (str): Preset de processamento
        enhance (bool): Aplicar melhorias
        crop (bool): Aplicar recorte
        backup (bool): Criar backup antes de processar
    """
    print("=" * 70)
    print("🎨 PROCESSAMENTO DE IMAGENS")
    print("=" * 70)
    print(f"Preset: {preset} - {PROCESSING_PRESETS[preset]['description']}")
    print(f"Melhorias: {'Sim' if enhance else 'Não'}")
    print(f"Recorte: {'Sim' if crop else 'Não'}")
    print(f"Backup: {'Sim' if backup else 'Não'}")
    print("=" * 70)
    
    # Listar imagens
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images = [f for f in IMAGES_DIR.iterdir() 
              if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not images:
        print("\n⚠️  Nenhuma imagem encontrada para processar.")
        return
    
    print(f"\n📁 Encontradas {len(images)} imagens para processar.\n")
    
    # Confirmar processamento
    response = input("Continuar? (s/n): ").lower()
    if response != 's':
        print("Operação cancelada.")
        return
    
    # Processar imagens
    results = []
    
    for img_path in images:
        # Criar backup se solicitado
        if backup:
            backup_path = BACKUP_DIR / img_path.name
            if not backup_path.exists():
                import shutil
                shutil.copy2(img_path, backup_path)
        
        # Processar imagem
        output_path = PROCESSED_DIR / img_path.name
        result = process_image(img_path, output_path, preset, enhance, crop)
        results.append(result)
        print()
    
    # Gerar relatório
    report_path = PROJECT_ROOT / "processing_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            "preset": preset,
            "total_images": len(images),
            "successful": sum(1 for r in results if r["status"] == "success"),
            "failed": sum(1 for r in results if r["status"] == "error"),
            "results": results
        }, f, indent=2, ensure_ascii=False)
    
    # Resumo
    successful = sum(1 for r in results if r["status"] == "success")
    total_reduction = sum(r.get("compression_ratio_percent", 0) for r in results if r["status"] == "success")
    avg_reduction = total_reduction / successful if successful > 0 else 0
    
    print("=" * 70)
    print("📊 RESUMO DO PROCESSAMENTO")
    print("=" * 70)
    print(f"✅ Processadas com sucesso: {successful}/{len(images)}")
    print(f"📉 Redução média de tamanho: {avg_reduction:.1f}%")
    print(f"📁 Imagens processadas salvas em: {PROCESSED_DIR}")
    if backup:
        print(f"💾 Backups salvos em: {BACKUP_DIR}")
    print(f"📄 Relatório detalhado: {report_path}")
    print("=" * 70)


def process_single_image_interactive():
    """Modo interativo para processar uma imagem específica"""
    print("\n🖼️  PROCESSAMENTO INDIVIDUAL")
    print("=" * 70)
    
    # Listar imagens
    images = sorted([f for f in IMAGES_DIR.iterdir() 
                     if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']])
    
    if not images:
        print("⚠️  Nenhuma imagem encontrada.")
        return
    
    print("\nImagens disponíveis:")
    for idx, img in enumerate(images, 1):
        print(f"   {idx}. {img.name}")
    
    try:
        choice = int(input("\nEscolha o número da imagem: ")) - 1
        
        if choice < 0 or choice >= len(images):
            print("⚠️  Número inválido.")
            return
        
        selected_image = images[choice]
        
        # Escolher preset
        print("\nPresets disponíveis:")
        for idx, (preset_name, preset_config) in enumerate(PROCESSING_PRESETS.items(), 1):
            print(f"   {idx}. {preset_name}: {preset_config['description']}")
        
        preset_choice = int(input("\nEscolha o preset: ")) - 1
        preset_names = list(PROCESSING_PRESETS.keys())
        
        if preset_choice < 0 or preset_choice >= len(preset_names):
            print("⚠️  Preset inválido.")
            return
        
        selected_preset = preset_names[preset_choice]
        
        # Opções adicionais
        enhance = input("\nAplicar melhorias de qualidade? (s/n): ").lower() == 's'
        crop = input("Aplicar recorte inteligente? (s/n): ").lower() == 's'
        
        # Processar
        output_path = PROCESSED_DIR / selected_image.name
        print(f"\n🔄 Processando {selected_image.name}...\n")
        
        result = process_image(selected_image, output_path, selected_preset, enhance, crop)
        
        if result["status"] == "success":
            print(f"\n✅ Imagem processada com sucesso!")
            print(f"   Salva em: {output_path}")
        
    except ValueError:
        print("⚠️  Por favor, digite um número válido.")
    except Exception as e:
        print(f"❌ Erro: {e}")


# ================== MENU PRINCIPAL ==================

def main_menu():
    """Menu principal"""
    while True:
        print("\n" + "=" * 70)
        print("🎨 PROCESSAMENTO DE IMAGENS - Menu Principal")
        print("=" * 70)
        print("1. Processar todas as imagens (Preset: Reveal Slide)")
        print("2. Processar todas as imagens (Preset: Card Image)")
        print("3. Processar uma imagem específica (interativo)")
        print("4. Ver presets disponíveis")
        print("5. Processar com configurações personalizadas")
        print("0. Sair")
        print("=" * 70)
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == '1':
            enhance = input("Aplicar melhorias? (s/n): ").lower() == 's'
            process_all_images(preset="reveal_slide", enhance=enhance, crop=False, backup=True)
        elif choice == '2':
            enhance = input("Aplicar melhorias? (s/n): ").lower() == 's'
            crop = input("Aplicar recorte? (s/n): ").lower() == 's'
            process_all_images(preset="card_image", enhance=enhance, crop=crop, backup=True)
        elif choice == '3':
            process_single_image_interactive()
        elif choice == '4':
            print("\n📋 PRESETS DISPONÍVEIS:")
            print("=" * 70)
            for name, config in PROCESSING_PRESETS.items():
                print(f"\n🎯 {name.upper()}")
                print(f"   Descrição: {config['description']}")
                print(f"   Dimensões máximas: {config['max_width']}x{config['max_height']}")
                print(f"   Qualidade: {config.get('quality', 'N/A')}")
                print(f"   Formato: {config['format']}")
            print("=" * 70)
        elif choice == '5':
            print("\n⚙️  PROCESSAMENTO PERSONALIZADO")
            try:
                preset = input("Preset (reveal_slide/card_image/thumbnail/high_quality): ").strip()
                if preset not in PROCESSING_PRESETS:
                    print("⚠️  Preset inválido.")
                    continue
                
                enhance = input("Aplicar melhorias? (s/n): ").lower() == 's'
                crop = input("Aplicar recorte? (s/n): ").lower() == 's'
                backup = input("Criar backup? (s/n): ").lower() == 's'
                
                process_all_images(preset=preset, enhance=enhance, crop=crop, backup=backup)
            except Exception as e:
                print(f"❌ Erro: {e}")
        elif choice == '0':
            print("\n✅ Encerrando. Até logo!")
            break
        else:
            print("⚠️  Opção inválida.")


# ================== EXECUÇÃO ==================

if __name__ == "__main__":
    print("\n🚀 Script de Processamento de Imagens")
    print("   Projeto: Origem das Aves em Theropoda\n")
    
    if not IMAGES_DIR.exists():
        print(f"❌ Pasta de imagens não encontrada: {IMAGES_DIR}")
        exit(1)
    
    main_menu()
