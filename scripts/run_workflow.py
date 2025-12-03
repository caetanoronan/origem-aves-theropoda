#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Script - Workflow Completo de Extração de Imagens
Projeto: Origem das Aves em Theropoda

Este script orquestra todo o processo de extração, organização
e otimização de imagens dos PDFs científicos.

Uso:
    python run_workflow.py
"""

import sys
import os
from pathlib import Path

# Adicionar pasta scripts ao path
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

# Importar módulos dos scripts
try:
    import extract_pdf_images
    import map_pdf_to_html
    import rename_images
    import process_images
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("   Certifique-se de que todos os scripts estão na pasta 'scripts/'")
    sys.exit(1)

# ================== CONFIGURAÇÃO ==================

def print_banner():
    """Exibe banner de boas-vindas"""
    print("\n" + "=" * 80)
    print(" " * 20 + "🦅 WORKFLOW MASTER DE EXTRAÇÃO DE IMAGENS")
    print(" " * 25 + "Origem das Aves em Theropoda")
    print("=" * 80)
    print()


def print_step(step_num, title, description):
    """Exibe cabeçalho de etapa"""
    print("\n" + "▶" * 40)
    print(f"   ETAPA {step_num}: {title}")
    print(f"   {description}")
    print("▶" * 40 + "\n")


def confirm_step(message):
    """Solicita confirmação do usuário"""
    response = input(f"\n❓ {message} (s/n): ").lower().strip()
    return response == 's'


def pause_step():
    """Pausa entre etapas"""
    input("\n⏸️  Pressione ENTER para continuar para a próxima etapa...")


# ================== WORKFLOW PRINCIPAL ==================

def workflow_completo():
    """Executa o workflow completo"""
    
    print_banner()
    
    print("""
📋 Este workflow executará as seguintes etapas:

   1️⃣  Extração de imagens dos 5 PDFs científicos
   2️⃣  Geração do guia visual de mapeamento (HTML)
   3️⃣  Renomeação interativa/automática das imagens
   4️⃣  Processamento e otimização para web
   
⚙️  Você pode escolher executar:
   A) Workflow completo automatizado
   B) Workflow passo a passo (com confirmações)
   C) Etapas individuais
    """)
    
    print("=" * 80)
    choice = input("\nEscolha (A/B/C): ").upper().strip()
    
    if choice == 'A':
        workflow_automatizado()
    elif choice == 'B':
        workflow_passo_a_passo()
    elif choice == 'C':
        menu_etapas_individuais()
    else:
        print("⚠️  Opção inválida. Encerrando.")


def workflow_automatizado():
    """Workflow totalmente automatizado"""
    print("\n🤖 MODO AUTOMATIZADO")
    print("=" * 80)
    print("⚠️  Este modo executará todas as etapas automaticamente.")
    print("   As imagens serão renomeadas com sugestões automáticas.")
    print("   O processamento usará o preset 'reveal_slide' com melhorias.")
    
    if not confirm_step("Continuar com o modo automatizado?"):
        print("Operação cancelada.")
        return
    
    # Etapa 1: Extração
    print_step(1, "EXTRAÇÃO DE IMAGENS", "Extraindo figuras dos PDFs científicos")
    try:
        extract_pdf_images.process_all_pdfs()
        print("✅ Extração concluída!")
    except Exception as e:
        print(f"❌ Erro na extração: {e}")
        return
    
    # Etapa 2: Guia Visual
    print_step(2, "GUIA VISUAL", "Gerando guia de mapeamento HTML")
    try:
        map_pdf_to_html.generate_mapping_guide()
        print("✅ Guia visual criado!")
    except Exception as e:
        print(f"❌ Erro ao gerar guia: {e}")
    
    # Etapa 3: Renomeação Automática
    print_step(3, "RENOMEAÇÃO AUTOMÁTICA", "Aplicando sugestões de nomes")
    try:
        # Usar função de renomeação automática
        print("🔄 Aplicando renomeação automática...")
        rename_images.auto_rename_by_suggestions()
        print("✅ Renomeação concluída!")
    except Exception as e:
        print(f"❌ Erro na renomeação: {e}")
    
    # Etapa 4: Processamento
    print_step(4, "OTIMIZAÇÃO", "Processando imagens para web")
    try:
        print("🎨 Processando com preset 'reveal_slide'...")
        process_images.process_all_images(
            preset="reveal_slide",
            enhance=True,
            crop=False,
            backup=True
        )
        print("✅ Processamento concluído!")
    except Exception as e:
        print(f"❌ Erro no processamento: {e}")
    
    # Finalização
    print("\n" + "=" * 80)
    print("✨ WORKFLOW AUTOMATIZADO CONCLUÍDO!")
    print("=" * 80)
    print("\n📋 PRÓXIMOS PASSOS MANUAIS:")
    print("   1. Abra 'image_mapping_guide.html' para revisar as imagens")
    print("   2. Ajuste renomeações se necessário (use rename_images.py)")
    print("   3. Teste o index.html no navegador")
    print("   4. Busque imagens externas para alvos não encontrados")
    print("=" * 80)


def workflow_passo_a_passo():
    """Workflow com confirmações em cada etapa"""
    print("\n👣 MODO PASSO A PASSO")
    print("=" * 80)
    
    # Etapa 1: Extração
    if confirm_step("Executar Etapa 1 - Extração de imagens dos PDFs?"):
        print_step(1, "EXTRAÇÃO DE IMAGENS", "Extraindo figuras dos PDFs científicos")
        try:
            extract_pdf_images.process_all_pdfs()
            print("✅ Extração concluída!")
        except Exception as e:
            print(f"❌ Erro na extração: {e}")
            if not confirm_step("Continuar mesmo com erro?"):
                return
        pause_step()
    
    # Etapa 2: Guia Visual
    if confirm_step("Executar Etapa 2 - Gerar guia visual de mapeamento?"):
        print_step(2, "GUIA VISUAL", "Gerando guia de mapeamento HTML")
        try:
            map_pdf_to_html.generate_mapping_guide()
            print("✅ Guia visual criado!")
            print("\n💡 Abra 'image_mapping_guide.html' no navegador antes de continuar.")
        except Exception as e:
            print(f"❌ Erro ao gerar guia: {e}")
        pause_step()
    
    # Etapa 3: Renomeação
    if confirm_step("Executar Etapa 3 - Renomear imagens?"):
        print_step(3, "RENOMEAÇÃO", "Organizando nomes das imagens")
        print("\n🔄 Escolha o modo de renomeação:")
        print("   1. Interativo (manual, recomendado)")
        print("   2. Automático (baseado em sugestões)")
        print("   3. Pular esta etapa")
        
        rename_choice = input("\nEscolha (1/2/3): ").strip()
        
        if rename_choice == '1':
            try:
                rename_images.interactive_rename()
            except Exception as e:
                print(f"❌ Erro na renomeação: {e}")
        elif rename_choice == '2':
            try:
                rename_images.auto_rename_by_suggestions()
            except Exception as e:
                print(f"❌ Erro na renomeação: {e}")
        else:
            print("⏭️  Etapa de renomeação pulada.")
        
        pause_step()
    
    # Etapa 4: Processamento
    if confirm_step("Executar Etapa 4 - Processar e otimizar imagens?"):
        print_step(4, "OTIMIZAÇÃO", "Processando imagens para web")
        print("\n⚙️  Configurações de processamento:")
        print("   Preset disponíveis:")
        print("   1. reveal_slide (1200x800, ideal para slides)")
        print("   2. card_image (600x450, ideal para cards)")
        print("   3. high_quality (2000x1500, alta resolução)")
        
        preset_choice = input("\nEscolha o preset (1/2/3, padrão=1): ").strip() or '1'
        preset_map = {'1': 'reveal_slide', '2': 'card_image', '3': 'high_quality'}
        selected_preset = preset_map.get(preset_choice, 'reveal_slide')
        
        enhance = confirm_step("Aplicar melhorias de qualidade (nitidez/contraste)?")
        crop = confirm_step("Aplicar recorte inteligente?")
        
        try:
            process_images.process_all_images(
                preset=selected_preset,
                enhance=enhance,
                crop=crop,
                backup=True
            )
            print("✅ Processamento concluído!")
        except Exception as e:
            print(f"❌ Erro no processamento: {e}")
        
        pause_step()
    
    # Finalização
    print("\n" + "=" * 80)
    print("✨ WORKFLOW CONCLUÍDO!")
    print("=" * 80)
    print("\n📋 REVISÃO FINAL:")
    print("   1. Verifique a pasta 'images/' para as imagens finais")
    print("   2. Revise 'extraction_report.json' e 'processing_report.json'")
    print("   3. Teste o index.html no navegador")
    print("   4. Ajuste manualmente se necessário")
    print("=" * 80)


def menu_etapas_individuais():
    """Menu para executar etapas individuais"""
    while True:
        print("\n" + "=" * 80)
        print("🔧 MENU DE ETAPAS INDIVIDUAIS")
        print("=" * 80)
        print("1. Extrair imagens dos PDFs")
        print("2. Gerar guia visual de mapeamento")
        print("3. Renomear imagens (interativo)")
        print("4. Renomear imagens (automático)")
        print("5. Processar e otimizar imagens")
        print("6. Ver status do projeto")
        print("0. Voltar ao menu principal")
        print("=" * 80)
        
        choice = input("\nEscolha uma etapa: ").strip()
        
        if choice == '1':
            try:
                extract_pdf_images.process_all_pdfs()
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        elif choice == '2':
            try:
                map_pdf_to_html.generate_mapping_guide()
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        elif choice == '3':
            try:
                rename_images.interactive_rename()
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        elif choice == '4':
            try:
                rename_images.auto_rename_by_suggestions()
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        elif choice == '5':
            try:
                process_images.main_menu()
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        elif choice == '6':
            show_project_status()
        
        elif choice == '0':
            break
        
        else:
            print("⚠️  Opção inválida.")


def show_project_status():
    """Exibe status atual do projeto"""
    print("\n" + "=" * 80)
    print("📊 STATUS DO PROJETO")
    print("=" * 80)
    
    PROJECT_ROOT = Path(__file__).parent.parent
    IMAGES_DIR = PROJECT_ROOT / "images"
    
    # Contar arquivos
    pdfs = list(PROJECT_ROOT.glob("*.pdf"))
    images = list(IMAGES_DIR.glob("*.*")) if IMAGES_DIR.exists() else []
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    images = [img for img in images if img.suffix.lower() in image_extensions]
    
    # Verificar imagens necessárias
    html_images_needed = [
        "intro_aves_dinos.jpg", "respiracao_aves.png", "cladograma_theropoda_aves.png",
        "archosauria_skull.jpg", "theropoda_overview.jpg", "coelophysis.jpg",
        "deinonychus.jpg", "archaeopteryx.jpg", "confuciusornis.jpg", "neornithes_anatomy.jpg"
    ]
    
    images_found = sum(1 for name in html_images_needed if (IMAGES_DIR / name).exists())
    
    # Verificar relatórios
    extraction_report = PROJECT_ROOT / "extraction_report.json"
    processing_report = PROJECT_ROOT / "processing_report.json"
    mapping_guide = PROJECT_ROOT / "image_mapping_guide.html"
    
    # Exibir informações
    print(f"\n📁 Estrutura do Projeto:")
    print(f"   PDFs encontrados: {len(pdfs)}/5")
    for pdf in pdfs[:5]:  # Limitar a 5
        print(f"      • {pdf.name}")
    
    print(f"\n🖼️  Imagens:")
    print(f"   Total extraídas: {len(images)}")
    print(f"   Necessárias no HTML: {images_found}/10")
    
    missing = [name for name in html_images_needed if not (IMAGES_DIR / name).exists()]
    if missing:
        print(f"\n   ⚠️  Faltando ({len(missing)}):")
        for name in missing[:5]:  # Limitar a 5
            print(f"      • {name}")
    
    print(f"\n📄 Relatórios:")
    print(f"   extraction_report.json: {'✅' if extraction_report.exists() else '❌'}")
    print(f"   processing_report.json: {'✅' if processing_report.exists() else '❌'}")
    print(f"   image_mapping_guide.html: {'✅' if mapping_guide.exists() else '❌'}")
    
    print("\n" + "=" * 80)


# ================== EXECUÇÃO ==================

if __name__ == "__main__":
    try:
        workflow_completo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Workflow interrompido pelo usuário.")
        print("   Execute novamente quando desejar continuar.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ ERRO FATAL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
