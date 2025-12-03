#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Renomeação Inteligente de Imagens
Projeto: Origem das Aves em Theropoda

Este script ajuda a renomear as imagens extraídas dos PDFs para
corresponder aos nomes esperados no HTML, facilitando a integração.

Uso:
    python rename_images.py
    
O script irá:
1. Listar todas as imagens extraídas
2. Sugerir correspondências com os nomes do HTML
3. Permitir renomeação manual ou automática
"""

import os
import shutil
from pathlib import Path
import json

# ================== CONFIGURAÇÃO ==================

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"

# Nomes de imagens esperados pelo HTML (extraídos do index.html)
HTML_IMAGE_NAMES = [
    "intro_aves_dinos.jpg",
    "respiracao_aves.png",
    "cladograma_theropoda_aves.png",
    "archosauria_skull.jpg",
    "theropoda_overview.jpg",
    "coelophysis.jpg",
    "deinonychus.jpg",
    "archaeopteryx.jpg",
    "confuciusornis.jpg",
    "neornithes_anatomy.jpg"
]

# Mapeamento sugerido baseado no conteúdo dos PDFs
SUGGESTED_MAPPING = {
    # Imagens de cladogramas e filogenias
    "cladogram": ["cladograma_theropoda_aves.png"],
    
    # Fósseis e anatomia de Archaeopteryx
    "archaeopteryx": ["archaeopteryx.jpg", "intro_aves_dinos.jpg"],
    
    # Anatomia geral e modificações corporais
    "body_shape": ["respiracao_aves.png", "neornithes_anatomy.jpg"],
    "macroevolution": ["theropoda_overview.jpg"],
    
    # Propatágio e tecidos moles
    "propatagium": ["intro_aves_dinos.jpg", "deinonychus.jpg"],
}

# ================== FUNÇÕES ==================

def list_extracted_images():
    """Lista todas as imagens na pasta images/"""
    if not IMAGES_DIR.exists():
        print(f"❌ Pasta de imagens não encontrada: {IMAGES_DIR}")
        return []
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images = []
    
    for file in IMAGES_DIR.iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions:
            images.append(file)
    
    return sorted(images)


def display_images_and_targets():
    """Exibe as imagens extraídas e os nomes esperados pelo HTML"""
    print("=" * 70)
    print("📋 IMAGENS EXTRAÍDAS vs NOMES ESPERADOS NO HTML")
    print("=" * 70)
    
    extracted = list_extracted_images()
    
    print("\n🖼️  IMAGENS EXTRAÍDAS:")
    print("-" * 70)
    if extracted:
        for idx, img in enumerate(extracted, 1):
            file_size = img.stat().st_size / 1024  # KB
            print(f"   {idx:2d}. {img.name:<40} ({file_size:.1f} KB)")
    else:
        print("   ⚠️  Nenhuma imagem encontrada. Execute primeiro extract_pdf_images.py")
    
    print("\n🎯 NOMES ESPERADOS NO HTML:")
    print("-" * 70)
    for idx, name in enumerate(HTML_IMAGE_NAMES, 1):
        exists = (IMAGES_DIR / name).exists()
        status = "✅" if exists else "❌"
        print(f"   {idx:2d}. {status} {name}")
    
    print("=" * 70)
    
    return extracted


def suggest_mappings(extracted_images):
    """Sugere correspondências entre imagens extraídas e nomes do HTML"""
    print("\n💡 SUGESTÕES DE MAPEAMENTO")
    print("=" * 70)
    
    suggestions = {}
    
    for img in extracted_images:
        img_name = img.stem.lower()  # Nome sem extensão
        
        # Buscar correspondências por palavras-chave
        for keyword, target_names in SUGGESTED_MAPPING.items():
            if keyword in img_name:
                for target in target_names:
                    if target not in suggestions:
                        suggestions[target] = []
                    suggestions[target].append(img.name)
    
    if suggestions:
        for target_name, source_images in suggestions.items():
            print(f"\n📌 {target_name}:")
            for src in source_images:
                print(f"   ← {src}")
    else:
        print("   ⚠️  Nenhuma correspondência automática encontrada.")
        print("   Por favor, renomeie manualmente usando a função rename_image()")
    
    print("=" * 70)
    
    return suggestions


def rename_image(old_name, new_name, backup=True):
    """
    Renomeia uma imagem da pasta images/
    
    Args:
        old_name (str): Nome atual da imagem
        new_name (str): Novo nome desejado
        backup (bool): Criar backup antes de renomear
    """
    old_path = IMAGES_DIR / old_name
    new_path = IMAGES_DIR / new_name
    
    if not old_path.exists():
        print(f"❌ Arquivo não encontrado: {old_name}")
        return False
    
    if new_path.exists():
        print(f"⚠️  Arquivo de destino já existe: {new_name}")
        response = input("   Sobrescrever? (s/n): ").lower()
        if response != 's':
            print("   Operação cancelada.")
            return False
    
    try:
        if backup and new_path.exists():
            backup_path = IMAGES_DIR / f"{new_path.stem}_backup{new_path.suffix}"
            shutil.copy2(new_path, backup_path)
            print(f"   💾 Backup criado: {backup_path.name}")
        
        shutil.move(str(old_path), str(new_path))
        print(f"✅ Renomeado: {old_name} → {new_name}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao renomear: {e}")
        return False


def interactive_rename():
    """Modo interativo para renomear imagens"""
    print("\n🔄 MODO INTERATIVO DE RENOMEAÇÃO")
    print("=" * 70)
    
    extracted = list_extracted_images()
    
    if not extracted:
        print("⚠️  Nenhuma imagem para renomear.")
        return
    
    print("\n📋 Imagens disponíveis:")
    for idx, img in enumerate(extracted, 1):
        print(f"   {idx}. {img.name}")
    
    print("\n🎯 Nomes esperados pelo HTML:")
    for idx, name in enumerate(HTML_IMAGE_NAMES, 1):
        exists = (IMAGES_DIR / name).exists()
        status = "✅" if exists else "❌"
        print(f"   {idx}. {status} {name}")
    
    print("\n" + "=" * 70)
    print("Digite o número da imagem atual e o número do nome destino.")
    print("Exemplo: 1 3 (renomeia imagem #1 para nome #3 do HTML)")
    print("Digite 'q' para sair.")
    print("=" * 70)
    
    while True:
        try:
            choice = input("\nRenomear (ex: 1 3) ou 'q' para sair: ").strip().lower()
            
            if choice == 'q':
                print("✅ Saindo do modo interativo.")
                break
            
            parts = choice.split()
            if len(parts) != 2:
                print("⚠️  Formato inválido. Use: <número_origem> <número_destino>")
                continue
            
            source_idx = int(parts[0]) - 1
            target_idx = int(parts[1]) - 1
            
            if source_idx < 0 or source_idx >= len(extracted):
                print(f"⚠️  Número de origem inválido (1-{len(extracted)})")
                continue
            
            if target_idx < 0 or target_idx >= len(HTML_IMAGE_NAMES):
                print(f"⚠️  Número de destino inválido (1-{len(HTML_IMAGE_NAMES)})")
                continue
            
            old_name = extracted[source_idx].name
            new_name = HTML_IMAGE_NAMES[target_idx]
            
            # Manter a extensão original se o novo nome não especificar
            if '.' not in new_name:
                new_name += extracted[source_idx].suffix
            
            rename_image(old_name, new_name)
            
            # Atualizar lista
            extracted = list_extracted_images()
            
        except ValueError:
            print("⚠️  Por favor, digite números válidos.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")


def auto_rename_by_suggestions():
    """Renomeia automaticamente baseado nas sugestões"""
    print("\n🤖 RENOMEAÇÃO AUTOMÁTICA")
    print("=" * 70)
    
    extracted = list_extracted_images()
    suggestions = suggest_mappings(extracted)
    
    if not suggestions:
        print("⚠️  Nenhuma sugestão automática disponível.")
        return
    
    print("\n⚠️  ATENÇÃO: Esta operação irá renomear arquivos automaticamente!")
    response = input("Continuar? (s/n): ").lower()
    
    if response != 's':
        print("Operação cancelada.")
        return
    
    renamed_count = 0
    
    for target_name, source_images in suggestions.items():
        # Usar apenas a primeira sugestão para cada alvo
        if source_images:
            old_name = source_images[0]
            
            # Manter a extensão da imagem de origem
            old_path = IMAGES_DIR / old_name
            if old_path.exists():
                target_ext = Path(target_name).suffix
                source_ext = old_path.suffix
                
                # Se o alvo não tem extensão ou é diferente, usar a da origem
                if not target_ext or target_ext != source_ext:
                    target_name = Path(target_name).stem + source_ext
                
                if rename_image(old_name, target_name, backup=True):
                    renamed_count += 1
    
    print(f"\n✅ Total de imagens renomeadas: {renamed_count}")
    print("=" * 70)


def create_mapping_file():
    """Cria um arquivo JSON para mapeamento manual"""
    mapping_file = PROJECT_ROOT / "image_mapping.json"
    
    extracted = list_extracted_images()
    
    mapping_template = {
        "instructions": "Edite este arquivo para mapear imagens extraídas para nomes do HTML",
        "format": "{ 'html_name': 'extracted_image_name' }",
        "mappings": {}
    }
    
    # Pré-preencher com imagens extraídas
    for img in extracted:
        mapping_template["mappings"][img.name] = ""
    
    # Adicionar nomes esperados do HTML
    mapping_template["html_targets"] = HTML_IMAGE_NAMES
    
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping_template, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Arquivo de mapeamento criado: {mapping_file}")
    print("   Edite este arquivo e execute apply_mapping_file() para aplicar.")


def apply_mapping_file():
    """Aplica mapeamentos de um arquivo JSON"""
    mapping_file = PROJECT_ROOT / "image_mapping.json"
    
    if not mapping_file.exists():
        print(f"❌ Arquivo de mapeamento não encontrado: {mapping_file}")
        print("   Execute create_mapping_file() primeiro.")
        return
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mappings = data.get("mappings", {})
    renamed_count = 0
    
    print("\n🔄 Aplicando mapeamentos do arquivo JSON...")
    print("=" * 70)
    
    for old_name, new_name in mappings.items():
        if new_name and new_name.strip():
            if rename_image(old_name, new_name):
                renamed_count += 1
    
    print(f"\n✅ Total de imagens renomeadas: {renamed_count}")
    print("=" * 70)


# ================== MENU PRINCIPAL ==================

def main_menu():
    """Menu principal do script"""
    while True:
        print("\n" + "=" * 70)
        print("🎨 RENOMEAÇÃO DE IMAGENS - Menu Principal")
        print("=" * 70)
        print("1. Listar imagens extraídas e nomes esperados")
        print("2. Ver sugestões de mapeamento")
        print("3. Renomeação interativa (manual)")
        print("4. Renomeação automática (baseada em sugestões)")
        print("5. Criar arquivo de mapeamento JSON")
        print("6. Aplicar mapeamentos do arquivo JSON")
        print("0. Sair")
        print("=" * 70)
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == '1':
            display_images_and_targets()
        elif choice == '2':
            extracted = list_extracted_images()
            suggest_mappings(extracted)
        elif choice == '3':
            interactive_rename()
        elif choice == '4':
            auto_rename_by_suggestions()
        elif choice == '5':
            create_mapping_file()
        elif choice == '6':
            apply_mapping_file()
        elif choice == '0':
            print("\n✅ Encerrando. Até logo!")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")


# ================== EXECUÇÃO ==================

if __name__ == "__main__":
    print("\n🚀 Script de Renomeação de Imagens")
    print("   Projeto: Origem das Aves em Theropoda\n")
    
    # Verificar se a pasta de imagens existe
    if not IMAGES_DIR.exists():
        print(f"❌ Pasta de imagens não encontrada: {IMAGES_DIR}")
        print("   Execute primeiro extract_pdf_images.py")
        exit(1)
    
    main_menu()
