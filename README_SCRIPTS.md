# 🦅 Extração de Imagens de PDFs Científicos
## Projeto: Origem das Aves em Theropoda

---

## 📋 Visão Geral

Este conjunto de scripts Python foi desenvolvido para extrair, processar e organizar imagens de alta qualidade dos PDFs científicos para uso na apresentação web interativa (Reveal.js) sobre a "Origem das Aves em Theropoda".

### ✨ Funcionalidades Principais

1. **Extração Automática de Imagens** - Extrai todas as figuras dos PDFs científicos
2. **Renomeação Inteligente** - Mapeia imagens extraídas para os nomes esperados pelo HTML
3. **Processamento de Imagens** - Otimiza tamanho, formato e qualidade para web
4. **Guia Visual de Mapeamento** - Gera um HTML interativo para facilitar a seleção de imagens

---

## 🔧 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Instalar Dependências

Execute no terminal (PowerShell):

```powershell
pip install -r requirements.txt
```

Ou instale manualmente:

```powershell
pip install PyMuPDF Pillow
```

### Passo 2: Verificar Estrutura do Projeto

Certifique-se de que o projeto tenha a seguinte estrutura:

```
projeto_aves/
│
├── index.html                  # Apresentação Reveal.js
│
├── scripts/                    # Scripts Python
│   ├── extract_pdf_images.py   # Extração de imagens
│   ├── rename_images.py        # Renomeação
│   ├── process_images.py       # Otimização
│   └── map_pdf_to_html.py      # Guia visual
│
├── images/                     # Destino das imagens
│
├── assets/                     # (Opcional) PDFs organizados
│
├── *.pdf                       # PDFs científicos (na raiz)
│
└── requirements.txt            # Dependências Python
```

### Passo 3: Colocar os PDFs na Raiz do Projeto

Certifique-se de que os seguintes PDFs estejam na pasta raiz:

- `Origin of the propatagium in non-avian dinosaurs.pdf`
- `Decoupling body shape and mass distribution in birds and their dinosaurian ancestors.pdf`
- `'Dinosaur-bird' macroevolution, locomotor modules and the origins of flight.pdf`
- `Re-evaluation of the Haarlem Archaeopteryx and the radiation of maniraptoran theropod dinosaurs.pdf`
- `Agnoln-Novas2013-Avianancestors.pdf`

---

## 🚀 Guia de Uso

### Workflow Completo (Passo a Passo)

#### **Etapa 1: Extrair Imagens dos PDFs**

Execute o script de extração:

```powershell
cd scripts
python extract_pdf_images.py
```

**O que acontece:**
- Lê todos os 5 PDFs científicos mapeados
- Extrai imagens com resolução mínima de 400x400 pixels
- Salva na pasta `images/` com nomes organizados por origem
- Gera relatório JSON (`extraction_report.json`)

**Resultado esperado:**
```
📄 Processando: Origin of the propatagium...
   📑 Página 5: 3 imagem(ns) encontrada(s)
      ✅ Extraída: propatagium_p5_img1.png (800x600)
...
✨ Total extraído: 25 imagens
```

---

#### **Etapa 2: Gerar Guia Visual de Mapeamento**

Para facilitar a identificação visual das imagens:

```powershell
python map_pdf_to_html.py
```

**O que acontece:**
- Cria um arquivo HTML (`image_mapping_guide.html`) na raiz do projeto
- Organiza as imagens extraídas por paper científico
- Lista as 10 imagens necessárias para o HTML
- Exibe previews com dimensões e tamanhos

**Como usar o guia:**
1. Abra `image_mapping_guide.html` no navegador
2. Compare as imagens extraídas com as necessidades do HTML
3. Anote quais imagens renomear

---

#### **Etapa 3: Renomear Imagens**

Agora renomeie as imagens para corresponder aos nomes do HTML:

```powershell
python rename_images.py
```

**Modo Interativo (Recomendado):**
- Escolha opção `3` no menu
- Digite o número da imagem origem e do nome destino
- Exemplo: `1 8` renomeia a 1ª imagem extraída para `archaeopteryx.jpg`

**Modo Automático (Sugestões):**
- Escolha opção `4` no menu
- O script renomeia automaticamente baseado em palavras-chave

**Imagens esperadas pelo HTML:**
1. `intro_aves_dinos.jpg`
2. `respiracao_aves.png`
3. `cladograma_theropoda_aves.png`
4. `archosauria_skull.jpg`
5. `theropoda_overview.jpg`
6. `coelophysis.jpg`
7. `deinonychus.jpg`
8. `archaeopteryx.jpg`
9. `confuciusornis.jpg`
10. `neornithes_anatomy.jpg`

---

#### **Etapa 4: Processar e Otimizar Imagens**

Otimize as imagens para web (redimensionar e comprimir):

```powershell
python process_images.py
```

**Opções no menu:**
- **Opção 1:** Processar todas para slides Reveal.js (1200x800px)
- **Opção 2:** Processar para cards (600x450px)
- **Opção 3:** Processar imagem individual (interativo)

**Configurações recomendadas:**
- Preset: `reveal_slide` (para imagens grandes)
- Aplicar melhorias: **Sim** (aumenta nitidez e contraste)
- Recorte inteligente: **Não** (para preservar contexto científico)

**Resultado esperado:**
```
✅ archaeopteryx.jpg
   1600x1200 → 1200x900
   245.3KB → 89.7KB (63.4% redução)
```

---

## 📂 Estrutura de Arquivos Gerados

Após executar todos os scripts:

```
projeto_aves/
│
├── images/
│   ├── intro_aves_dinos.jpg          # ✅ Renomeada
│   ├── archaeopteryx.jpg              # ✅ Renomeada
│   ├── cladograma_theropoda_aves.png  # ✅ Renomeada
│   ├── ...                            # Outras imagens renomeadas
│   │
│   ├── backup/                        # Backups originais
│   │   └── *.jpg
│   │
│   └── processed/                     # Versões otimizadas
│       └── *.jpg
│
├── extraction_report.json             # Relatório de extração
├── processing_report.json             # Relatório de processamento
└── image_mapping_guide.html           # Guia visual
```

---

## 🎯 Mapeamento Sugerido (Imagens ↔ PDFs)

### 📄 **Uno & Hirasawa (2023)** - Propatágio

**Figuras relevantes:**
- Fig. 2: Microraptor e Caudipteryx com tecidos moles

**Usar para:**
- `intro_aves_dinos.jpg` (transição evolutiva)
- `deinonychus.jpg` (tecidos moles em Theropoda)

---

### 📄 **Macaulay et al. (2023)** - Centro de Massa

**Figuras relevantes:**
- Fig. 1-2: Mudança do Centro de Massa (CoM)

**Usar para:**
- `respiracao_aves.png` (modificações anatômicas)
- `neornithes_anatomy.jpg` (anatomia comparativa)

---

### 📄 **Nebreda et al. (2021)** - Macroevolução

**Figuras relevantes:**
- Gráficos de disparidade de membros

**Usar para:**
- `theropoda_overview.jpg` (visão geral evolutiva)

---

### 📄 **Foth & Rauhut (2017)** - Archaeopteryx

**Figuras relevantes:**
- Fósseis de Archaeopteryx de Haarlem (Ostromia)
- Comparações manuais e esqueléticas

**Usar para:**
- `archaeopteryx.jpg` ⭐ (prioridade máxima)
- `intro_aves_dinos.jpg` (alternativa)

---

### 📄 **Agnolín & Novas (2013)** - Filogenia

**Figuras relevantes:**
- Cladogramas de Avialae e Paraves
- Detalhes ósseos comparativos

**Usar para:**
- `cladograma_theropoda_aves.png` ⭐ (prioridade máxima)

---

## 🔍 Fontes Externas para Imagens Faltantes

Se alguns PDFs não contiverem as imagens necessárias, busque em:

### Bancos de Imagens Científicas (Domínio Público/Creative Commons)

1. **Wikimedia Commons**
   - [Archaeopteryx](https://commons.wikimedia.org/wiki/Category:Archaeopteryx)
   - [Theropoda](https://commons.wikimedia.org/wiki/Category:Theropoda)

2. **Phylopic** (Silhuetas de organismos)
   - https://www.phylopic.org/
   - Buscar: "Archaeopteryx", "Coelophysis", "Deinonychus"

3. **Smithsonian Open Access**
   - https://www.si.edu/openaccess
   - Fósseis e reconstruções paleontológicas

4. **Natural History Museum (Londres)**
   - https://www.nhm.ac.uk/discover/dinosaurs.html

---

## ⚙️ Configurações Avançadas

### Personalizar Extração de Imagens

Edite `extract_pdf_images.py`:

```python
# Alterar dimensões mínimas
MIN_WIDTH = 400   # Padrão: 400px
MIN_HEIGHT = 400  # Padrão: 400px

# Alterar DPI de renderização
target_dpi = 300  # Padrão: 300 DPI
```

### Adicionar Novos PDFs

Edite a seção `PDF_MAPPING` em `extract_pdf_images.py`:

```python
PDF_MAPPING = {
    "novo_paper.pdf": {
        "description": "Descrição do paper",
        "target_figures": ["Fig. 1", "Fig. 2"],
        "keywords": ["palavra-chave1", "palavra-chave2"],
        "output_prefix": "novo_paper"
    }
}
```

### Criar Novos Presets de Processamento

Edite `process_images.py`:

```python
PROCESSING_PRESETS = {
    "custom_preset": {
        "max_width": 1000,
        "max_height": 800,
        "quality": 90,
        "format": "PNG",
        "description": "Meu preset personalizado"
    }
}
```

---

## 🐛 Solução de Problemas

### Erro: `ModuleNotFoundError: No module named 'fitz'`

**Solução:**
```powershell
pip install --upgrade PyMuPDF
```

---

### Erro: `Permission denied` ao salvar imagens

**Solução:**
1. Feche o arquivo HTML se estiver aberto
2. Execute o PowerShell como Administrador
3. Verifique permissões da pasta `images/`

---

### Nenhuma imagem extraída dos PDFs

**Possíveis causas:**
1. PDFs protegidos por senha → Desbloquear antes
2. Imagens muito pequenas → Reduzir `MIN_WIDTH` e `MIN_HEIGHT`
3. Imagens como vetores → Usar renderização de página completa:

```python
# Descomentar em extract_pdf_images.py (linha ~220)
rendered_images = extract_images_high_resolution(
    str(pdf_path),
    output_prefix=f"{output_prefix}_fullpage",
    target_dpi=300
)
```

---

### Imagens distorcidas após processamento

**Solução:**
- Use `maintain_aspect=True` (padrão)
- Evite `crop=True` para imagens científicas
- Use preset `high_quality` para preservar detalhes

---

## 📚 Referências dos Scripts

### `extract_pdf_images.py`
- **Biblioteca:** PyMuPDF (fitz)
- **Método 1:** Extrai imagens embutidas diretamente
- **Método 2:** Renderiza páginas como imagens (alta resolução)

### `rename_images.py`
- **Modos:** Interativo, Automático, JSON
- **Funcionalidades:** Backup automático, validação de nomes

### `process_images.py`
- **Biblioteca:** Pillow (PIL)
- **Operações:** Resize, crop inteligente, compressão, melhorias

### `map_pdf_to_html.py`
- **Saída:** HTML com previews visuais
- **Organização:** Por paper científico

---

## 📝 Checklist Final

Antes de finalizar o projeto:

- [ ] Todos os 5 PDFs foram processados
- [ ] 10 imagens renomeadas conforme HTML
- [ ] Imagens otimizadas (< 150KB cada)
- [ ] Testado `index.html` no navegador
- [ ] Imagens carregam corretamente nos slides
- [ ] Guia visual (`image_mapping_guide.html`) gerado
- [ ] Backups salvos na pasta `images/backup/`

---

## 📧 Suporte

Para dúvidas ou problemas:
1. Verifique a seção **Solução de Problemas**
2. Revise os comentários nos scripts Python
3. Consulte a documentação das bibliotecas:
   - [PyMuPDF Docs](https://pymupdf.readthedocs.io/)
   - [Pillow Docs](https://pillow.readthedocs.io/)

---

## 📜 Licença

Scripts desenvolvidos para uso educacional no projeto "Origem das Aves em Theropoda".

**PDFs Científicos:** Respeite os direitos autorais dos papers originais. Use as imagens apenas para fins acadêmicos conforme as políticas de Fair Use.

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0  
**Autor:** Sistema de Extração Automática
