# 🦅 Origem das Aves em Theropoda - Apresentação Interativa

## 📖 Sobre o Projeto

Apresentação web interativa baseada em **Reveal.js** explorando a origem evolutiva das aves modernas a partir de dinossauros Theropoda, com foco nas **modificações do plano corpóreo e metabolismo**.

---

## 🎯 Objetivo Atual: Extração de Imagens Científicas

Este repositório contém scripts Python para **extrair, processar e organizar** imagens de alta qualidade dos PDFs científicos que servem de base para a apresentação.

### 🔬 PDFs Científicos Utilizados

1. **Uno & Hirasawa (2023)** - Origin of the propatagium in non-avian dinosaurs
2. **Macaulay et al. (2023)** - Decoupling body shape and mass distribution
3. **Nebreda et al. (2021)** - Dinosaur-bird macroevolution
4. **Foth & Rauhut (2017)** - Re-evaluation of Haarlem Archaeopteryx
5. **Agnolín & Novas (2013)** - Avian Ancestors

---

## 🚀 Início Rápido

### ⚡ Opção 1: Launcher Automático (Windows)

```powershell
# Clique duplo no arquivo ou execute no terminal:
.\start.bat
```

### ⚡ Opção 2: Workflow Master

```powershell
cd scripts
python run_workflow.py
```

### ⚡ Opção 3: Instalação Manual

```powershell
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar scripts individualmente
cd scripts
python extract_pdf_images.py
python map_pdf_to_html.py
python rename_images.py
python process_images.py
```

---

## 📂 Estrutura do Projeto

```
projeto_aves/
│
├── 📄 index.html                    # Apresentação Reveal.js ⭐
│
├── 🔬 PDFs Científicos (5)
│   ├── Origin of the propatagium...
│   ├── Decoupling body shape...
│   ├── Dinosaur-bird macroevolution...
│   ├── Re-evaluation Haarlem Archaeopteryx...
│   └── Agnoln-Novas2013-Avianancestors.pdf
│
├── 📁 scripts/                      # Scripts Python
│   ├── extract_pdf_images.py        # Extração
│   ├── rename_images.py             # Renomeação
│   ├── process_images.py            # Otimização
│   ├── map_pdf_to_html.py           # Guia visual
│   └── run_workflow.py              # Orquestrador
│
├── 📁 images/                       # Imagens extraídas
│   ├── backup/                      # Backups
│   └── processed/                   # Otimizadas
│
├── 📚 Documentação
│   ├── README.md                    # Este arquivo
│   ├── QUICK_START.md               # Guia rápido
│   ├── README_SCRIPTS.md            # Doc completa
│   └── REFERENCE.md                 # Referência rápida
│
└── ⚙️ Utilitários
    ├── start.bat                    # Launcher Windows
    └── requirements.txt             # Dependências
```

---

## 📋 Workflow de Extração

### Etapa 1: Extração de Imagens dos PDFs

```powershell
python scripts/extract_pdf_images.py
```

**O que faz:**
- Extrai todas as figuras dos 5 PDFs científicos
- Filtra imagens por qualidade (mín. 400×400px)
- Salva na pasta `images/` com nomes organizados
- Gera relatório JSON

**Resultado:** ~20-30 imagens na pasta `images/`

---

### Etapa 2: Geração de Guia Visual

```powershell
python scripts/map_pdf_to_html.py
```

**O que faz:**
- Cria `image_mapping_guide.html` com previews visuais
- Organiza imagens por paper científico
- Lista as 10 imagens necessárias no HTML
- Facilita a identificação visual

**Resultado:** Arquivo HTML interativo para abrir no navegador

---

### Etapa 3: Renomeação de Imagens

```powershell
python scripts/rename_images.py
```

**O que faz:**
- Modo interativo ou automático
- Renomeia imagens para os nomes esperados pelo HTML
- Cria backups automaticamente
- Validação de nomes

**10 Imagens Necessárias:**
1. `intro_aves_dinos.jpg`
2. `respiracao_aves.png`
3. `cladograma_theropoda_aves.png`
4. `archosauria_skull.jpg`
5. `theropoda_overview.jpg`
6. `coelophysis.jpg`
7. `deinonychus.jpg`
8. `archaeopteryx.jpg` ⭐
9. `confuciusornis.jpg`
10. `neornithes_anatomy.jpg`

---

### Etapa 4: Otimização para Web

```powershell
python scripts/process_images.py
```

**O que faz:**
- Redimensiona para dimensões ideais (1200×800px)
- Comprime mantendo qualidade (85% JPEG)
- Aplica melhorias (nitidez, contraste)
- Reduz tamanho em ~50-70%

**Resultado:** Imagens otimizadas prontas para web

---

## 🎨 Conteúdo da Apresentação

### Estrutura da Apresentação (index.html)

1. **Introdução** - Evolução dinossauro → ave
2. **Modificações do Plano Corpóreo** (Foco principal)
   - Sistema respiratório único
   - Pneumaticidade óssea
   - Fusões esqueléticas
3. **Ancestrais Evolutivos** - Timeline de Archosauria a Neornithes
4. **Glossário** - Termos técnicos
5. **Tabela Comparativa** - Theropoda vs Aves
6. **Créditos** - Referências bibliográficas

### 🎯 Opção Escolhida: "D - Modificações do Plano Corpóreo"

A apresentação foca nas adaptações anatômicas e fisiológicas que permitiram a evolução do voo:
- Sacos aéreos e respiração unidirecional
- Redução de peso (ossos pneumáticos)
- Fusões ósseas (pigostilo, sinsacro, fúrcula)
- Modificações dos membros anteriores

---

## 📚 Documentação Detalhada

### Para Usuários Iniciantes

📖 **[QUICK_START.md](QUICK_START.md)** - Guia rápido de 5 minutos

### Para Desenvolvedores

📘 **[README_SCRIPTS.md](README_SCRIPTS.md)** - Documentação completa dos scripts

### Referência Rápida

📗 **[REFERENCE.md](REFERENCE.md)** - Tabelas, comandos e checklists

---

## 🛠️ Requisitos do Sistema

### Software Necessário

- **Python 3.8+** ([Baixar](https://www.python.org/downloads/))
- **pip** (gerenciador de pacotes Python)

### Bibliotecas Python

```
PyMuPDF >= 1.23.0
Pillow >= 10.0.0
```

**Instalação:**
```powershell
pip install -r requirements.txt
```

---

## 🎓 Uso Acadêmico

### Licença das Imagens

⚠️ **ATENÇÃO:** As imagens extraídas dos PDFs científicos estão sujeitas aos direitos autorais dos respectivos papers. 

**Uso Permitido:**
- ✅ Apresentações acadêmicas
- ✅ Fins educacionais (Fair Use)
- ✅ Pesquisa científica

**Uso NÃO Permitido:**
- ❌ Distribuição comercial
- ❌ Publicação sem citação da fonte
- ❌ Modificação que altere o significado original

### Citação das Fontes

Sempre cite os papers originais:

```
Foth, C., & Rauhut, O. W. (2017). Re-evaluation of the Haarlem Archaeopteryx 
and the radiation of maniraptoran theropod dinosaurs. BMC Evolutionary Biology.

Agnolín, F. L., & Novas, F. E. (2013). Avian ancestors: A review of the 
phylogenetic relationships of the theropods Unenlagiidae, Microraptoria, 
Anchiornis and Scansoriopterygidae.

[... demais papers]
```

---

## 🌐 Fontes Externas Recomendadas

Se os PDFs não contiverem todas as imagens necessárias:

### 🔓 Domínio Público / Creative Commons

- **Wikimedia Commons** - commons.wikimedia.org
- **PhyloPic** - phylopic.org (silhuetas científicas)
- **Smithsonian Open Access** - si.edu/openaccess
- **Natural History Museum** - nhm.ac.uk

### 📚 Bases Científicas

- **ResearchGate** - Solicitar figuras aos autores
- **Google Scholar** - Buscar papers com figuras em acesso aberto

---

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError"

```powershell
pip install --upgrade PyMuPDF Pillow
```

### Nenhuma Imagem Extraída

**Possíveis causas:**
1. PDFs protegidos → Remover proteção
2. Imagens vetoriais → Usar renderização de página completa
3. Dimensões muito pequenas → Reduzir `MIN_WIDTH` no script

### Imagens Não Aparecem no HTML

**Verificar:**
1. Nomes dos arquivos correspondem exatamente
2. Extensões corretas (`.jpg` vs `.png`)
3. Caminho relativo: `../images/nome.jpg`

**Mais soluções:** Ver [README_SCRIPTS.md](README_SCRIPTS.md) seção "Solução de Problemas"

---

## 📊 Status do Projeto

### ✅ Concluído

- [x] Apresentação HTML completa com Reveal.js
- [x] Texto científico fundamentado em papers
- [x] Sistema de navegação por abas
- [x] Glossário interativo
- [x] Tabela comparativa
- [x] Scripts Python completos
- [x] Documentação abrangente

### 🔄 Em Andamento

- [ ] Extração de imagens dos PDFs
- [ ] Seleção e renomeação das 10 imagens principais
- [ ] Busca de imagens externas (se necessário)

### 📅 Próximos Passos

1. Executar workflow de extração
2. Revisar qualidade das imagens
3. Testar apresentação no navegador
4. Ajustes finais de layout
5. Apresentação final

---

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

### Como Contribuir

1. Melhorias nos scripts Python
2. Adição de novas fontes de imagens
3. Correções na documentação
4. Sugestões de otimização

---

## 📧 Contato

**Projeto:** Origem das Aves em Theropoda  
**Tipo:** Apresentação Interativa Web (Reveal.js)  
**Disciplina:** Paleontologia / Biologia Evolutiva  
**Instituição:** UFSC

---

## 📜 Agradecimentos

### Papers Científicos

- Uno & Hirasawa (2023)
- Macaulay et al. (2023)
- Nebreda et al. (2021)
- Foth & Rauhut (2017)
- Agnolín & Novas (2013)

### Ferramentas e Bibliotecas

- **Reveal.js** - Framework de apresentações
- **PyMuPDF** - Manipulação de PDFs
- **Pillow** - Processamento de imagens
- **Python** - Linguagem de programação

---

## 📌 Links Úteis

- **Reveal.js Docs:** https://revealjs.com/
- **PyMuPDF Docs:** https://pymupdf.readthedocs.io/
- **Pillow Docs:** https://pillow.readthedocs.io/
- **Wikimedia Commons - Theropoda:** https://commons.wikimedia.org/wiki/Category:Theropoda
- **PhyloPic:** https://www.phylopic.org/

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0  
**Licença:** Uso Acadêmico / Educacional

---

## 🎉 Comece Agora!

```powershell
# Opção mais rápida:
.\start.bat

# OU
cd scripts
python run_workflow.py
```

**Boa sorte! 🦅🦖**
