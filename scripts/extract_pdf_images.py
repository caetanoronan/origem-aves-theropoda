#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Extração de Imagens de PDFs Científicos
Projeto: Origem das Aves em Theropoda (Reveal.js)

Este script extrai imagens de alta qualidade dos PDFs científicos
e as organiza para uso na apresentação web.

Requisitos:
    pip install PyMuPDF Pillow

Uso:
    python extract_pdf_images.py
    
Autor: Sistema de Extração Automática
Data: Dezembro 2025
"""

import fitz  # PyMuPDF
from PIL import Image
import io
import os
import sys
from pathlib import Path
import json

# ================== CONFIGURAÇÃO ==================

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent.parent
PDF_DIR = PROJECT_ROOT
IMAGES_OUTPUT_DIR = PROJECT_ROOT / "images"
ASSETS_DIR = PROJECT_ROOT / "assets"

# Criar diretórios se não existirem
IMAGES_OUTPUT_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# Mapeamento de PDFs para categorias de imagens
PDF_MAPPING = {
    "Origin of the propatagium in non-avian dinosaurs.pdf": {
        "description": "Uno & Hirasawa (2023) - Propatágio em dinossauros",
        "target_figures": ["Fig. 2", "Figure 2"],
        "keywords": ["Microraptor", "Caudipteryx", "propatagium", "soft tissue"],
        "output_prefix": "propatagium"
    },
    "Decoupling body shape and mass distribution in birds and their dinosaurian ancestors.pdf": {
        "description": "Macaulay et al. (2023) - Mudança do Centro de Massa",
        "target_figures": ["Fig. 1", "Fig. 2", "Figure 1", "Figure 2"],
        "keywords": ["center of mass", "CoM", "body shape", "posture"],
        "output_prefix": "body_shape"
    },
    "'Dinosaur-bird' macroevolution, locomotor modules and the origins of flight.pdf": {
        "description": "Nebreda et al. (2021) - Macroevolução dinossauro-ave",
        "target_figures": ["Fig. 1", "Fig. 2", "Fig. 3"],
        "keywords": ["disparity", "limb", "locomotor", "evolution"],
        "output_prefix": "macroevolution"
    },
    "Re-evaluation of the Haarlem Archaeopteryx and the radiation of maniraptoran theropod dinosaurs.pdf": {
        "description": "Foth & Rauhut (2017) - Archaeopteryx de Haarlem",
        "target_figures": ["Fig. 1", "Fig. 2", "Fig. 3", "Fig. 4"],
        "keywords": ["Archaeopteryx", "Ostromia", "Haarlem", "fossil"],
        "output_prefix": "archaeopteryx"
    },
    "Agnoln-Novas2013-Avianancestors.pdf": {
        "description": "Agnolín & Novas (2013) - Ancestrais Avianos",
        "target_figures": ["Fig. 1", "Fig. 2", "cladogram"],
        "keywords": ["cladogram", "phylogeny", "avian", "ancestor"],
        "output_prefix": "cladogram"
    }
}

# Qualidade mínima de imagem (DPI e dimensões)
MIN_WIDTH = 400
MIN_HEIGHT = 400
MIN_DPI = 150

# ================== FUNÇÕES PRINCIPAIS ==================

def extract_images_from_pdf(pdf_path, output_prefix="image", min_width=MIN_WIDTH, min_height=MIN_HEIGHT):
    """
    Extrai todas as imagens de um PDF e salva com qualidade alta.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        output_prefix (str): Prefixo para nomear as imagens extraídas
        min_width (int): Largura mínima para considerar a imagem
        min_height (int): Altura mínima para considerar a imagem
    
    Returns:
        list: Lista de caminhos das imagens extraídas
    """
    if not os.path.exists(pdf_path):
        print(f"❌ PDF não encontrado: {pdf_path}")
        return []
    
    print(f"\n📄 Processando: {os.path.basename(pdf_path)}")
    extracted_images = []
    
    try:
        # Abrir o PDF
        pdf_document = fitz.open(pdf_path)
        print(f"   Total de páginas: {pdf_document.page_count}")
        
        # Iterar por cada página
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            image_list = page.get_images(full=True)
            
            if image_list:
                print(f"   📑 Página {page_num + 1}: {len(image_list)} imagem(ns) encontrada(s)")
            
            # Extrair cada imagem da página
            for img_index, img_info in enumerate(image_list):
                xref = img_info[0]  # Referência da imagem
                
                try:
                    # Extrair imagem base
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    # Carregar com Pillow para verificar dimensões
                    pil_image = Image.open(io.BytesIO(image_bytes))
                    width, height = pil_image.size
                    
                    # Filtrar imagens muito pequenas (logos, ícones)
                    if width < min_width or height < min_height:
                        print(f"      ⚠️  Imagem {img_index + 1} ignorada (muito pequena: {width}x{height})")
                        continue
                    
                    # Nome do arquivo de saída
                    output_filename = f"{output_prefix}_p{page_num + 1}_img{img_index + 1}.{image_ext}"
                    output_path = IMAGES_OUTPUT_DIR / output_filename
                    
                    # Salvar imagem
                    if image_ext.lower() in ['png', 'jpg', 'jpeg']:
                        pil_image.save(output_path, quality=95, optimize=True)
                    else:
                        with open(output_path, "wb") as img_file:
                            img_file.write(image_bytes)
                    
                    print(f"      ✅ Extraída: {output_filename} ({width}x{height})")
                    extracted_images.append(str(output_path))
                    
                except Exception as img_error:
                    print(f"      ❌ Erro ao extrair imagem {img_index + 1}: {img_error}")
                    continue
        
        pdf_document.close()
        print(f"   ✨ Total extraído deste PDF: {len(extracted_images)} imagens\n")
        
    except Exception as e:
        print(f"   ❌ Erro ao processar PDF: {e}\n")
        return []
    
    return extracted_images


def extract_images_high_resolution(pdf_path, output_prefix="highres", target_dpi=300):
    """
    Extrai imagens em alta resolução renderizando páginas como imagens.
    Útil para capturar figuras compostas ou gráficos complexos.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        output_prefix (str): Prefixo para nomear as imagens
        target_dpi (int): DPI para renderização (padrão: 300)
    
    Returns:
        list: Lista de caminhos das imagens geradas
    """
    if not os.path.exists(pdf_path):
        print(f"❌ PDF não encontrado: {pdf_path}")
        return []
    
    print(f"\n📸 Renderização em alta resolução: {os.path.basename(pdf_path)}")
    rendered_images = []
    
    try:
        pdf_document = fitz.open(pdf_path)
        zoom = target_dpi / 72  # Fator de zoom (72 DPI é o padrão)
        matrix = fitz.Matrix(zoom, zoom)
        
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            
            # Renderizar página como imagem
            pix = page.get_pixmap(matrix=matrix)
            
            # Salvar imagem
            output_filename = f"{output_prefix}_page{page_num + 1}.png"
            output_path = IMAGES_OUTPUT_DIR / output_filename
            pix.save(output_path)
            
            print(f"   ✅ Página {page_num + 1} renderizada: {output_filename} ({pix.width}x{pix.height})")
            rendered_images.append(str(output_path))
        
        pdf_document.close()
        print(f"   ✨ Total renderizado: {len(rendered_images)} páginas\n")
        
    except Exception as e:
        print(f"   ❌ Erro na renderização: {e}\n")
        return []
    
    return rendered_images


def process_all_pdfs():
    """
    Processa todos os PDFs mapeados e gera relatório.
    """
    print("=" * 70)
    print("🔬 EXTRAÇÃO DE IMAGENS DE PDFs CIENTÍFICOS")
    print("   Projeto: Origem das Aves em Theropoda")
    print("=" * 70)
    
    extraction_report = {
        "total_pdfs_processed": 0,
        "total_images_extracted": 0,
        "pdfs_details": {}
    }
    
    # Processar cada PDF mapeado
    for pdf_filename, metadata in PDF_MAPPING.items():
        pdf_path = PDF_DIR / pdf_filename
        
        if not pdf_path.exists():
            print(f"\n⚠️  PDF não encontrado: {pdf_filename}")
            print(f"   Por favor, coloque o arquivo na pasta raiz do projeto.")
            extraction_report["pdfs_details"][pdf_filename] = {
                "status": "not_found",
                "images_extracted": 0
            }
            continue
        
        # Extração método 1: Imagens embutidas
        output_prefix = metadata["output_prefix"]
        extracted_images = extract_images_from_pdf(
            str(pdf_path), 
            output_prefix=output_prefix
        )
        
        # Extração método 2: Renderização em alta resolução (opcional)
        # Descomente se quiser também páginas completas renderizadas
        # rendered_images = extract_images_high_resolution(
        #     str(pdf_path),
        #     output_prefix=f"{output_prefix}_fullpage",
        #     target_dpi=300
        # )
        # all_images = extracted_images + rendered_images
        
        all_images = extracted_images
        
        # Atualizar relatório
        extraction_report["total_pdfs_processed"] += 1
        extraction_report["total_images_extracted"] += len(all_images)
        extraction_report["pdfs_details"][pdf_filename] = {
            "status": "success",
            "description": metadata["description"],
            "images_extracted": len(all_images),
            "files": [os.path.basename(img) for img in all_images]
        }
    
    # Salvar relatório JSON
    report_path = PROJECT_ROOT / "extraction_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(extraction_report, f, indent=2, ensure_ascii=False)
    
    # Exibir resumo
    print("=" * 70)
    print("📊 RESUMO DA EXTRAÇÃO")
    print("=" * 70)
    print(f"✅ PDFs processados: {extraction_report['total_pdfs_processed']}")
    print(f"🖼️  Total de imagens extraídas: {extraction_report['total_images_extracted']}")
    print(f"📁 Pasta de saída: {IMAGES_OUTPUT_DIR}")
    print(f"📄 Relatório salvo em: {report_path}")
    print("=" * 70)
    
    return extraction_report


# ================== EXECUÇÃO PRINCIPAL ==================

if __name__ == "__main__":
    print("\n🚀 Iniciando extração de imagens...")
    
    try:
        report = process_all_pdfs()
        
        if report["total_images_extracted"] > 0:
            print("\n✨ Extração concluída com sucesso!")
            print("\n📋 PRÓXIMOS PASSOS:")
            print("   1. Revise as imagens na pasta 'images/'")
            print("   2. Execute 'rename_images.py' para renomear conforme HTML")
            print("   3. Execute 'process_images.py' para otimizar (resize/crop)")
            print("   4. Atualize os caminhos no index.html se necessário")
        else:
            print("\n⚠️  Nenhuma imagem foi extraída.")
            print("   Verifique se os PDFs estão na pasta raiz do projeto.")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ ERRO FATAL: {e}")
        sys.exit(1)
