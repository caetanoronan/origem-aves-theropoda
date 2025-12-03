#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Mapeamento Visual PDF → HTML
Projeto: Origem das Aves em Theropoda

Este script cria um guia visual interativo que ajuda a identificar
qual figura de qual PDF deve ser usada para cada imagem no HTML.

Gera um arquivo HTML com preview das imagens extraídas organizadas
por paper científico, facilitando a seleção manual.

Uso:
    python map_pdf_to_html.py
"""

from pathlib import Path
import json
import base64
from datetime import datetime

# ================== CONFIGURAÇÃO ==================

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"
OUTPUT_HTML = PROJECT_ROOT / "image_mapping_guide.html"

# Imagens esperadas no HTML
HTML_IMAGES = {
    "intro_aves_dinos.jpg": {
        "description": "Ilustração artística da evolução dinossauro para ave",
        "context": "Slide de introdução",
        "suggested_source": "Archaeopteryx ou transição Theropoda-Aves"
    },
    "respiracao_aves.png": {
        "description": "Esquema dos sacos aéreos e pulmões em aves",
        "context": "Aba 'Modificações do Plano Corpóreo' - Sistema Respiratório",
        "suggested_source": "Diagramas anatômicos de sistema respiratório aviano"
    },
    "cladograma_theropoda_aves.png": {
        "description": "Árvore filogenética de Theropoda até Aves",
        "context": "Aba 'Ancestrais' - Timeline Evolutiva",
        "suggested_source": "Agnolín & Novas (2013) - cladogramas"
    },
    "archosauria_skull.jpg": {
        "description": "Crânio de Arcossauro mostrando a fenestra antorbital",
        "context": "Card de Archosauria",
        "suggested_source": "Comparações cranianas ou diagrama anatômico"
    },
    "theropoda_overview.jpg": {
        "description": "Visão geral de Theropoda",
        "context": "Card de Theropoda",
        "suggested_source": "Diversidade de Theropoda ou esqueletos comparativos"
    },
    "coelophysis.jpg": {
        "description": "Coelophysis",
        "context": "Card de Coelophysis (Triássico Superior)",
        "suggested_source": "Fóssil ou reconstrução de Coelophysis"
    },
    "deinonychus.jpg": {
        "description": "Deinonychus",
        "context": "Card de Deinonychus (Cretáceo Inferior)",
        "suggested_source": "Fóssil ou reconstrução de Deinonychus/Velociraptor"
    },
    "archaeopteryx.jpg": {
        "description": "Fóssil de Archaeopteryx",
        "context": "Card de Archaeopteryx (Jurássico Superior)",
        "suggested_source": "Foth & Rauhut (2017) - Haarlem Archaeopteryx"
    },
    "confuciusornis.jpg": {
        "description": "Confuciusornis",
        "context": "Card de Confuciusornis (Cretáceo Inferior)",
        "suggested_source": "Fóssil ou reconstrução de aves primitivas"
    },
    "neornithes_anatomy.jpg": {
        "description": "Anatomia da Ave Moderna",
        "context": "Card de Neornithes",
        "suggested_source": "Diagrama anatômico de ave moderna"
    }
}

# Papers científicos
PDF_SOURCES = {
    "Uno & Hirasawa (2023)": {
        "title": "Origin of the propatagium in non-avian dinosaurs",
        "key_figures": ["Fig. 2 - Microraptor e Caudipteryx com tecidos moles"],
        "relevance": "Tecidos moles, propatágio, Microraptor"
    },
    "Macaulay et al. (2023)": {
        "title": "Decoupling body shape and mass distribution",
        "key_figures": ["Fig. 1-2 - Mudança do Centro de Massa"],
        "relevance": "Postura corporal, evolução de forma"
    },
    "Nebreda et al. (2021)": {
        "title": "Dinosaur-bird macroevolution, locomotor modules",
        "key_figures": ["Gráficos de disparidade de membros"],
        "relevance": "Macroevolução, módulos locomotores"
    },
    "Foth & Rauhut (2017)": {
        "title": "Haarlem Archaeopteryx and maniraptoran radiation",
        "key_figures": ["Fósseis de Archaeopteryx, comparações"],
        "relevance": "Archaeopteryx, Ostromia, Maniraptora"
    },
    "Agnolín & Novas (2013)": {
        "title": "Avian Ancestors",
        "key_figures": ["Cladogramas, detalhes ósseos"],
        "relevance": "Filogenia, ancestrais avianos"
    }
}

# ================== FUNÇÕES ==================

def image_to_base64(image_path):
    """Converte imagem para base64 para embedding no HTML"""
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            return base64.b64encode(image_data).decode('utf-8')
    except:
        return None


def generate_mapping_guide():
    """Gera o guia HTML interativo"""
    
    print("=" * 70)
    print("🗺️  GERANDO GUIA DE MAPEAMENTO PDF → HTML")
    print("=" * 70)
    
    # Coletar imagens extraídas
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    extracted_images = sorted([f for f in IMAGES_DIR.iterdir() 
                               if f.is_file() and f.suffix.lower() in image_extensions])
    
    if not extracted_images:
        print("\n⚠️  Nenhuma imagem encontrada em:", IMAGES_DIR)
        print("   Execute extract_pdf_images.py primeiro.")
        return
    
    print(f"\n📁 Encontradas {len(extracted_images)} imagens extraídas")
    
    # Organizar imagens por prefixo (origem do PDF)
    images_by_source = {}
    for img in extracted_images:
        # Detectar prefixo (nome do PDF de origem)
        name_lower = img.stem.lower()
        
        source = "outros"
        if "propatagium" in name_lower:
            source = "Uno & Hirasawa (2023)"
        elif "body_shape" in name_lower or "com" in name_lower:
            source = "Macaulay et al. (2023)"
        elif "macroevolution" in name_lower or "locomotor" in name_lower:
            source = "Nebreda et al. (2021)"
        elif "archaeopteryx" in name_lower or "haarlem" in name_lower:
            source = "Foth & Rauhut (2017)"
        elif "cladogram" in name_lower or "phylo" in name_lower:
            source = "Agnolín & Novas (2013)"
        
        if source not in images_by_source:
            images_by_source[source] = []
        
        images_by_source[source].append(img)
    
    print(f"📚 Organizadas por {len(images_by_source)} fontes")
    
    # Gerar HTML
    html_content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Mapeamento: Imagens PDF → HTML</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #E1F5FE 0%, #B3E5FC 100%);
            padding: 20px;
            color: #263238;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            padding: 40px;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 4px solid #0288D1;
            padding-bottom: 20px;
        }}
        
        h1 {{
            color: #01579B;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            color: #455A64;
            font-size: 1.2em;
        }}
        
        .section {{
            margin-bottom: 50px;
        }}
        
        .section-title {{
            background: linear-gradient(135deg, #0288D1, #01579B);
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            font-size: 1.5em;
            margin-bottom: 20px;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: #F5F5F5;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        }}
        
        .card img {{
            width: 100%;
            height: 200px;
            object-fit: contain;
            border-radius: 8px;
            background: white;
            padding: 10px;
            margin-bottom: 10px;
        }}
        
        .card-title {{
            font-weight: bold;
            color: #01579B;
            font-size: 1.1em;
            margin-bottom: 8px;
        }}
        
        .card-info {{
            font-size: 0.9em;
            color: #455A64;
            line-height: 1.6;
        }}
        
        .html-target {{
            background: #FFF3E0;
            border-left: 4px solid #FF6F00;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
        }}
        
        .html-target-title {{
            font-weight: bold;
            color: #E65100;
            font-size: 1.1em;
            margin-bottom: 8px;
        }}
        
        .html-target-desc {{
            color: #455A64;
            font-size: 0.95em;
            margin-bottom: 5px;
        }}
        
        .badge {{
            display: inline-block;
            background: #0288D1;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            margin-right: 5px;
            margin-top: 5px;
        }}
        
        .instructions {{
            background: #E8F5E9;
            border-left: 4px solid #4CAF50;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        
        .instructions h3 {{
            color: #2E7D32;
            margin-bottom: 10px;
        }}
        
        .instructions ol {{
            margin-left: 20px;
            line-height: 2;
        }}
        
        .source-info {{
            background: #E3F2FD;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        
        .source-title {{
            font-weight: bold;
            color: #01579B;
            font-size: 1.2em;
            margin-bottom: 8px;
        }}
        
        .source-desc {{
            color: #455A64;
            line-height: 1.6;
        }}
        
        footer {{
            text-align: center;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #E0E0E0;
            color: #757575;
        }}
        
        .timestamp {{
            font-size: 0.9em;
            color: #9E9E9E;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🗺️ Guia de Mapeamento: PDF → HTML</h1>
            <p class="subtitle">Origem das Aves em Theropoda - Seleção de Imagens</p>
        </header>
        
        <div class="instructions">
            <h3>📋 Como Usar Este Guia</h3>
            <ol>
                <li>Revise as <strong>10 imagens necessárias</strong> listadas abaixo (esperadas pelo HTML)</li>
                <li>Navegue pelas <strong>imagens extraídas dos PDFs</strong> organizadas por paper científico</li>
                <li>Identifique qual imagem extraída melhor corresponde a cada necessidade do HTML</li>
                <li>Use o script <code>rename_images.py</code> para renomear as imagens escolhidas</li>
                <li>Se necessário, processe as imagens com <code>process_images.py</code> para otimizar</li>
            </ol>
        </div>
        
        <div class="section">
            <div class="section-title">🎯 IMAGENS NECESSÁRIAS NO HTML (10 alvos)</div>
"""
    
    # Listar imagens esperadas pelo HTML
    for idx, (filename, info) in enumerate(HTML_IMAGES.items(), 1):
        exists = (IMAGES_DIR / filename).exists()
        status_badge = f'<span class="badge" style="background: {"#4CAF50" if exists else "#F44336"}">{"✅ Presente" if exists else "❌ Ausente"}</span>'
        
        html_content += f"""
            <div class="html-target">
                <div class="html-target-title">{idx}. {filename} {status_badge}</div>
                <div class="html-target-desc"><strong>Descrição:</strong> {info['description']}</div>
                <div class="html-target-desc"><strong>Contexto:</strong> {info['context']}</div>
                <div class="html-target-desc"><strong>Sugestão:</strong> {info['suggested_source']}</div>
            </div>
"""
    
    html_content += """
        </div>
        
        <div class="section">
            <div class="section-title">📚 IMAGENS EXTRAÍDAS DOS PDFs</div>
"""
    
    # Listar imagens extraídas organizadas por fonte
    for source_name, images in images_by_source.items():
        # Informações do paper (se disponível)
        paper_info = PDF_SOURCES.get(source_name, {})
        
        html_content += f"""
            <div class="source-info">
                <div class="source-title">📄 {source_name}</div>
"""
        
        if paper_info:
            html_content += f"""
                <div class="source-desc">
                    <strong>Título:</strong> {paper_info.get('title', 'N/A')}<br>
                    <strong>Figuras-chave:</strong> {', '.join(paper_info.get('key_figures', ['N/A']))}<br>
                    <strong>Relevância:</strong> {paper_info.get('relevance', 'N/A')}
                </div>
"""
        
        html_content += f"""
            </div>
            
            <div class="grid">
"""
        
        # Cards das imagens
        for img_path in images:
            # Obter informações da imagem
            file_size = img_path.stat().st_size / 1024  # KB
            
            # Tentar carregar dimensões
            try:
                from PIL import Image
                with Image.open(img_path) as pil_img:
                    width, height = pil_img.size
                    dimensions = f"{width}x{height}"
            except:
                dimensions = "N/A"
            
            html_content += f"""
                <div class="card">
                    <img src="{img_path.name}" alt="{img_path.name}" 
                         onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22100%22 height=%22100%22%3E%3Crect fill=%22%23ddd%22 width=%22100%22 height=%22100%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22%3EImagem%3C/text%3E%3C/svg%3E'">
                    <div class="card-title">{img_path.name}</div>
                    <div class="card-info">
                        <strong>Dimensões:</strong> {dimensions}<br>
                        <strong>Tamanho:</strong> {file_size:.1f} KB<br>
                        <strong>Formato:</strong> {img_path.suffix.upper()[1:]}
                    </div>
                </div>
"""
        
        html_content += """
            </div>
"""
    
    html_content += f"""
        </div>
        
        <footer>
            <p>Guia gerado automaticamente por <strong>map_pdf_to_html.py</strong></p>
            <p class="timestamp">Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
            <p>Projeto: Origem das Aves em Theropoda (Reveal.js)</p>
        </footer>
    </div>
</body>
</html>
"""
    
    # Salvar arquivo
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Guia HTML gerado com sucesso!")
    print(f"📁 Local: {OUTPUT_HTML}")
    print(f"\n💡 Abra o arquivo no navegador para visualizar o guia interativo.")
    print("=" * 70)


# ================== EXECUÇÃO ==================

if __name__ == "__main__":
    print("\n🚀 Gerando Guia de Mapeamento Visual...")
    
    try:
        generate_mapping_guide()
        print("\n✨ Processo concluído!")
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
