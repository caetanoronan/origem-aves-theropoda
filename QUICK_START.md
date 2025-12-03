# 🚀 Guia Rápido de Início (Quick Start)

## Extração de Imagens para Apresentação Reveal.js

---

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Instalar Dependências

Abra o PowerShell na pasta do projeto e execute:

```powershell
pip install PyMuPDF Pillow
```

### 2️⃣ Organizar PDFs

Certifique-se de que os 5 PDFs científicos estejam na **raiz do projeto**:
- ✅ Origin of the propatagium...
- ✅ Decoupling body shape...
- ✅ Dinosaur-bird macroevolution...
- ✅ Re-evaluation of the Haarlem Archaeopteryx...
- ✅ Agnoln-Novas2013-Avianancestors.pdf

### 3️⃣ Executar Workflow Master

```powershell
cd scripts
python run_workflow.py
```

Escolha:
- **A** = Automático (sem intervenção)
- **B** = Passo a passo (com confirmações)
- **C** = Etapas individuais

**Recomendado para iniciantes:** Opção **B** (Passo a passo)

---

## 📋 Workflow Manual (Etapa por Etapa)

### Etapa 1: Extrair Imagens

```powershell
cd scripts
python extract_pdf_images.py
```

✅ Resultado: Imagens na pasta `images/`

---

### Etapa 2: Gerar Guia Visual

```powershell
python map_pdf_to_html.py
```

✅ Resultado: Arquivo `image_mapping_guide.html` (abra no navegador)

---

### Etapa 3: Renomear Imagens

```powershell
python rename_images.py
```

Escolha no menu:
- **3** = Modo interativo (recomendado)
- **4** = Modo automático

**Imagens necessárias (10):**
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

### Etapa 4: Otimizar Imagens

```powershell
python process_images.py
```

Configurações recomendadas:
- Preset: **1** (Reveal Slide - 1200x800)
- Melhorias: **Sim**
- Recorte: **Não** (preserva contexto científico)

---

## ✅ Verificação Final

### Checklist

- [ ] Pasta `images/` contém imagens extraídas
- [ ] 10 imagens renomeadas conforme HTML
- [ ] Arquivo `image_mapping_guide.html` gerado
- [ ] Imagens otimizadas (< 150KB cada)
- [ ] Testado `index.html` no navegador

---

## 🔍 Comandos de Diagnóstico

### Ver status do projeto

```powershell
cd scripts
python run_workflow.py
# Escolha opção C → 6 (Ver status)
```

### Listar imagens extraídas

```powershell
Get-ChildItem ..\images\*.jpg, ..\images\*.png
```

### Verificar tamanho das imagens

```powershell
Get-ChildItem ..\images\ | Select-Object Name, @{Name="Size(KB)";Expression={[math]::Round($_.Length/1KB,2)}}
```

---

## 🆘 Problemas Comuns

### Nenhuma imagem extraída

**Solução:**
1. Verifique se os PDFs estão na raiz (não em `assets/`)
2. Tente reduzir dimensões mínimas em `extract_pdf_images.py`:
   ```python
   MIN_WIDTH = 300
   MIN_HEIGHT = 300
   ```

### Erro "ModuleNotFoundError"

**Solução:**
```powershell
pip install --upgrade PyMuPDF Pillow
```

### Imagens não aparecem no HTML

**Verifique:**
1. Nomes dos arquivos correspondem exatamente ao HTML
2. Extensões corretas (`.jpg` vs `.png`)
3. Caminho relativo correto: `../images/nome.jpg`

---

## 📚 Documentação Completa

Para informações detalhadas, consulte:
- `README_SCRIPTS.md` - Documentação completa
- Comentários nos scripts Python
- Guia visual: `image_mapping_guide.html`

---

## 🎯 Mapeamento Prioritário

### Imagens CRÍTICAS (buscar primeiro):

| HTML                            | Fonte Prioritária           | Alternativa |
|---------------------------------|----------------------------|-------------|
| `archaeopteryx.jpg`             | Foth & Rauhut (2017) Fig.1-4 | Wikimedia   |
| `cladograma_theropoda_aves.png` | Agnolín & Novas (2013)     | PhyloPic    |
| `respiracao_aves.png`           | Macaulay et al. (2023)     | Benton 2014 |

### Imagens SECUNDÁRIAS (podem usar fontes externas):

- `intro_aves_dinos.jpg` → Arte conceitual (Wikimedia/DeviantArt)
- `coelophysis.jpg` → Wikimedia Commons
- `deinonychus.jpg` → Natural History Museum
- `confuciusornis.jpg` → Wikimedia Commons
- `neornithes_anatomy.jpg` → Diagramas anatômicos (Google Scholar)

---

## 💡 Dicas Finais

1. **Priorize qualidade sobre quantidade** - 10 imagens boas > 50 ruins
2. **Use guia visual** - `image_mapping_guide.html` facilita a seleção
3. **Faça backups** - Scripts criam automaticamente em `images/backup/`
4. **Teste no navegador** - Abra `index.html` após cada etapa
5. **Busque fontes externas** - PDFs podem não ter todas as imagens

---

## 📞 Próximos Passos

Após completar a extração:

1. **Revisar qualidade** - Abrir cada imagem manualmente
2. **Buscar imagens faltantes** - Wikimedia, PhyloPic, etc.
3. **Atualizar HTML** - Se necessário ajustar caminhos
4. **Testar apresentação** - Verificar carregamento nos slides
5. **Comprimir adicionalmente** - Se necessário (TinyPNG, etc.)

---

**Tempo estimado total:** 30-60 minutos  
**Dificuldade:** ⭐⭐☆☆☆ (Intermediário)

Boa sorte! 🦅
