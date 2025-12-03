# 📊 Referência Rápida - Scripts e Arquivos

## 🗂️ Estrutura de Arquivos do Projeto

```
projeto_aves/
│
├── 📄 index.html                          # Apresentação Reveal.js
│
├── 📚 PDFs Científicos (5)
│   ├── Origin of the propatagium...
│   ├── Decoupling body shape...
│   ├── Dinosaur-bird macroevolution...
│   ├── Re-evaluation Haarlem Archaeopteryx...
│   └── Agnoln-Novas2013-Avianancestors.pdf
│
├── 📁 images/                             # Imagens extraídas e processadas
│   ├── backup/                            # Backups automáticos
│   └── processed/                         # Versões otimizadas
│
├── 📁 scripts/                            # Scripts Python
│   ├── extract_pdf_images.py              # Extração de PDFs
│   ├── rename_images.py                   # Renomeação
│   ├── process_images.py                  # Otimização
│   ├── map_pdf_to_html.py                 # Guia visual
│   └── run_workflow.py                    # Workflow master
│
├── 📝 Documentação
│   ├── README_SCRIPTS.md                  # Doc completa
│   ├── QUICK_START.md                     # Início rápido
│   ├── REFERENCE.md                       # Este arquivo
│   └── requirements.txt                   # Dependências
│
├── ⚙️ Utilitários
│   ├── start.bat                          # Launcher Windows
│   └── image_mapping_guide.html           # Guia visual (gerado)
│
└── 📊 Relatórios (gerados)
    ├── extraction_report.json
    ├── processing_report.json
    └── image_mapping.json
```

---

## 🛠️ Tabela de Scripts

| Script                     | Função Principal                      | Entrada                | Saída                  | Tempo  |
|----------------------------|---------------------------------------|------------------------|------------------------|--------|
| `extract_pdf_images.py`    | Extrai imagens dos PDFs               | 5 PDFs                 | `images/*.jpg/png`     | 5 min  |
| `map_pdf_to_html.py`       | Gera guia visual HTML                 | `images/`              | `image_mapping_guide.html` | 1 min  |
| `rename_images.py`         | Renomeia imagens para HTML            | `images/`              | Imagens renomeadas     | 5-10 min |
| `process_images.py`        | Otimiza imagens (resize/compress)     | `images/`              | `images/processed/`    | 2 min  |
| `run_workflow.py`          | Orquestra todo o processo             | Todos os acima         | Projeto completo       | 15-30 min |

---

## 🎯 Imagens Necessárias no HTML

| #  | Nome do Arquivo                    | Descrição                              | Fonte Sugerida              | Status    |
|----|------------------------------------|-----------------------------------------|-----------------------------|-----------|
| 1  | `intro_aves_dinos.jpg`             | Evolução dinossauro → ave               | Archaeopteryx/Arte          | ⚠️ Buscar |
| 2  | `respiracao_aves.png`              | Sistema respiratório (sacos aéreos)     | Macaulay 2023 / Diagramas   | ⚠️ Buscar |
| 3  | `cladograma_theropoda_aves.png`    | Árvore filogenética                     | **Agnolín & Novas 2013** ⭐ | 🔍 PDF    |
| 4  | `archosauria_skull.jpg`            | Crânio com fenestra antorbital          | Diagramas anatômicos        | ⚠️ Buscar |
| 5  | `theropoda_overview.jpg`           | Diversidade de Theropoda                | Nebreda 2021 / Wikimedia    | 🔍 PDF    |
| 6  | `coelophysis.jpg`                  | Coelophysis (Triássico)                 | Wikimedia Commons           | ⚠️ Buscar |
| 7  | `deinonychus.jpg`                  | Deinonychus (Cretáceo)                  | Uno 2023 / Wikimedia        | 🔍 PDF    |
| 8  | `archaeopteryx.jpg`                | Fóssil de Archaeopteryx                 | **Foth & Rauhut 2017** ⭐   | 🔍 PDF    |
| 9  | `confuciusornis.jpg`               | Confuciusornis (ave primitiva)          | Wikimedia Commons           | ⚠️ Buscar |
| 10 | `neornithes_anatomy.jpg`           | Anatomia de ave moderna                 | Macaulay 2023 / Diagramas   | 🔍 PDF    |

**Legenda:**
- 🔍 PDF = Priorizar extração dos PDFs científicos
- ⚠️ Buscar = Buscar em fontes externas (Wikimedia, PhyloPic, etc.)
- ⭐ = **CRÍTICA** - Prioridade máxima

---

## 📚 Mapeamento PDF → Imagens

### 📄 Uno & Hirasawa (2023) - Propatágio

**Figuras-chave:**
- Fig. 2: Microraptor e Caudipteryx (tecidos moles)

**Usar para:**
- `deinonychus.jpg` (tecidos moles em Dromaeosauridae)
- `intro_aves_dinos.jpg` (transição evolutiva)

**Comando de extração:**
```python
output_prefix = "propatagium"
```

---

### 📄 Macaulay et al. (2023) - Centro de Massa

**Figuras-chave:**
- Fig. 1: Mudança do Centro de Massa (CoM)
- Fig. 2: Comparação de posturas

**Usar para:**
- `respiracao_aves.png` (modificações corporais)
- `neornithes_anatomy.jpg` (anatomia comparativa)

**Comando de extração:**
```python
output_prefix = "body_shape"
```

---

### 📄 Nebreda et al. (2021) - Macroevolução

**Figuras-chave:**
- Fig. 1-3: Gráficos de disparidade de membros

**Usar para:**
- `theropoda_overview.jpg` (visão geral evolutiva)

**Comando de extração:**
```python
output_prefix = "macroevolution"
```

---

### 📄 Foth & Rauhut (2017) - Archaeopteryx ⭐

**Figuras-chave:**
- Fig. 1-4: Fóssil de Haarlem (Ostromia)
- Comparações manuais e esqueléticas

**Usar para:**
- `archaeopteryx.jpg` ⭐⭐⭐ **(PRIORIDADE MÁXIMA)**

**Comando de extração:**
```python
output_prefix = "archaeopteryx"
```

---

### 📄 Agnolín & Novas (2013) - Filogenia ⭐

**Figuras-chave:**
- Cladogramas de Avialae, Paraves, Eumaniraptora
- Detalhes ósseos comparativos

**Usar para:**
- `cladograma_theropoda_aves.png` ⭐⭐⭐ **(PRIORIDADE MÁXIMA)**
- `archosauria_skull.jpg` (comparações cranianas)

**Comando de extração:**
```python
output_prefix = "cladogram"
```

---

## 🔧 Comandos Úteis (PowerShell)

### Instalação Completa

```powershell
# Clonar/baixar projeto
cd "C:\Users\caetanoronan\OneDrive - UFSC\Área de Trabalho\Aves"

# Instalar dependências
pip install -r requirements.txt

# Verificar instalação
python -c "import fitz, PIL; print('✅ OK')"
```

### Execução Rápida

```powershell
# Launcher interativo
.\start.bat

# OU workflow master
cd scripts
python run_workflow.py
```

### Extração Individual

```powershell
cd scripts

# Apenas extração
python extract_pdf_images.py

# Apenas renomeação
python rename_images.py

# Apenas processamento
python process_images.py
```

### Diagnóstico

```powershell
# Listar imagens extraídas
Get-ChildItem images\*.jpg, images\*.png | Select-Object Name, Length

# Verificar imagens necessárias
$needed = @("intro_aves_dinos.jpg", "respiracao_aves.png", "cladograma_theropoda_aves.png", "archaeopteryx.jpg")
$needed | ForEach-Object { if (Test-Path "images\$_") { "✅ $_" } else { "❌ $_" } }

# Contar imagens
(Get-ChildItem images\*.jpg, images\*.png).Count
```

---

## 📊 Presets de Processamento

| Preset           | Dimensões  | Qualidade | Formato | Uso Recomendado                |
|------------------|------------|-----------|---------|--------------------------------|
| `reveal_slide`   | 1200×800   | 85%       | JPEG    | Slides full-width              |
| `card_image`     | 600×450    | 85%       | JPEG    | Cards de duas colunas          |
| `thumbnail`      | 300×200    | 80%       | JPEG    | Miniaturas                     |
| `high_quality`   | 2000×1500  | 95%       | PNG     | Impressão / Apresentações 4K   |

**Como aplicar:**

```python
# Em process_images.py
process_all_images(
    preset="reveal_slide",  # Escolher preset
    enhance=True,           # Melhorias de qualidade
    crop=False,             # Recorte inteligente
    backup=True             # Criar backup
)
```

---

## 🌐 Fontes Externas de Imagens

### 🔓 Domínio Público / Creative Commons

| Fonte                        | URL                                  | Tipo de Conteúdo          |
|------------------------------|--------------------------------------|---------------------------|
| **Wikimedia Commons**        | commons.wikimedia.org                | Fósseis, reconstruções    |
| **PhyloPic**                 | phylopic.org                         | Silhuetas científicas     |
| **Smithsonian Open Access**  | si.edu/openaccess                    | Espécimes de museu        |
| **Natural History Museum**   | nhm.ac.uk                            | Coleções paleontológicas  |
| **Berkeley UCMP**            | ucmp.berkeley.edu                    | Bancos de imagens         |

### 🔍 Busca Avançada no Google

```
"Archaeopteryx" site:commons.wikimedia.org filetype:jpg
"Theropoda phylogeny" site:researchgate.net filetype:pdf
"avian respiratory system" site:edu filetype:png
```

### ⚖️ Licenças Recomendadas

- **CC0** (Domínio Público)
- **CC BY** (Atribuição)
- **CC BY-SA** (Atribuição-CompartilhaIgual)

⚠️ **Sempre citar a fonte na apresentação!**

---

## 📋 Checklist de Finalização

### Antes de Apresentar

- [ ] 10/10 imagens presentes na pasta `images/`
- [ ] Todas as imagens < 200KB (otimizadas)
- [ ] Testado `index.html` em diferentes navegadores
- [ ] Imagens carregam corretamente nos slides
- [ ] Fontes citadas na seção "Créditos" do HTML
- [ ] Guia visual (`image_mapping_guide.html`) revisado
- [ ] Relatórios JSON salvos para referência

### Qualidade das Imagens

- [ ] Resolução adequada (mínimo 800×600 para slides)
- [ ] Sem artefatos de compressão excessivos
- [ ] Legendas/texto legíveis
- [ ] Fundo adequado (sem ruído visual)
- [ ] Proporções corretas (sem distorção)

### Documentação

- [ ] `README_SCRIPTS.md` lido e compreendido
- [ ] Scripts executados sem erros
- [ ] Backups criados em `images/backup/`
- [ ] Relatórios de extração e processamento salvos

---

## ⏱️ Estimativas de Tempo

| Tarefa                          | Tempo Estimado | Dificuldade |
|---------------------------------|----------------|-------------|
| Instalação de dependências      | 2-5 min        | ⭐☆☆☆☆      |
| Extração de imagens             | 5-10 min       | ⭐⭐☆☆☆     |
| Geração de guia visual          | 1 min          | ⭐☆☆☆☆      |
| Renomeação (interativa)         | 10-20 min      | ⭐⭐⭐☆☆    |
| Processamento de imagens        | 2-5 min        | ⭐⭐☆☆☆     |
| Busca de imagens externas       | 30-60 min      | ⭐⭐⭐⭐☆   |
| **TOTAL (com busca externa)**   | **50-100 min** | ⭐⭐⭐☆☆    |

---

## 🆘 Suporte e Contatos

### Documentação

- **README Completo:** `README_SCRIPTS.md`
- **Guia Rápido:** `QUICK_START.md`
- **Esta Referência:** `REFERENCE.md`

### Recursos Online

- **PyMuPDF Docs:** https://pymupdf.readthedocs.io/
- **Pillow Docs:** https://pillow.readthedocs.io/
- **Reveal.js Docs:** https://revealjs.com/

### Comunidades

- **Stack Overflow:** Tag `python-imaging-library`, `pymupdf`
- **Reddit:** r/python, r/learnpython

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0  
**Projeto:** Origem das Aves em Theropoda (Reveal.js)
