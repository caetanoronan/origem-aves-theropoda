# 🦅 Cladograma Interativo: Evolução de Theropoda → Aves

## 📋 Visão Geral

Um cladograma interativo responsivo que apresenta a evolução dos dinossauros Theropoda até as aves modernas, baseado em dados filogenéticos científicos e fósseis transicionais.

**Acesse aqui:** [cladograma_aves_theropoda.html](./cladograma_aves_theropoda.html)

---

## 🦕 Táxons Inclusos

### 1. **Euparkeria** (~245 Ma)
- **Localização:** Triássico Médio, África do Sul
- **Tamanho:** ~60 cm
- **Descrição:** Arcossauromorfo basal representante primitivo da linhagem que levaria aos crocodilianos e dinossauros
- **Características:** Características cranianas únicas, postura semi-ereta

### 2. **Marasuchus** (~235 Ma)
- **Localização:** Triássico Médio, Argentina
- **Tamanho:** ~40 cm
- **Descrição:** Dinossauromorfo basal, um dos primeiros representantes da linhagem que levou aos dinossauros verdadeiros
- **Características:** Membros posteriores alongados, postura completamente bípede

### 3. **Guaibasaurus** (~225 Ma)
- **Localização:** Triássico Superior, Brasil
- **Tamanho:** ~2-3 metros
- **Descrição:** Um dos primeiros saurópodomomorfos e importante representante da diversificação inicial dos dinossauros
- **Características:** Características transicionais entre terópodes e saurópodes

### 4. **Coelophysis** (~215 Ma)
- **Localização:** Triássico Superior, América do Norte
- **Tamanho:** ~2-3 metros
- **Descrição:** Um dos dinossauros celurosauro mais antigos conhecidos
- **Características:** Predador ativo, corpo esbelto, membros delgados, cauda longa

### 5. **Archaeopteryx** (~150 Ma)
- **Localização:** Jurássico Superior, Alemanha
- **Tamanho:** ~50-60 cm
- **Descrição:** O fóssil transicional mais famoso da paleontologia
- **Características:** Combina características de dinossauros terópodes com características avianas avançadas

### 6. **Confuciusornis** (~125 Ma)
- **Localização:** Cretáceo Inferior, China
- **Tamanho:** ~25-30 cm
- **Descrição:** Ave primitiva que representa um estágio intermediário importante na evolução aviana
- **Características:** Penas bem-desenvolvidas, bico queratinoso sem dentes, garras nas asas

### 7. **Neornithes** (0 Ma - Presente)
- **Localização:** Distribuição global
- **Diversidade:** >10.000 espécies viventes
- **Descrição:** Aves modernas que representam a culminação de ~150 milhões de anos de evolução
- **Características:** Esqueleto pneumático, sistema respiratório unidirecional, asas especializadas

---

## 🎨 Características Técnicas

### Design
- ✅ **Responsivo:** Funciona em desktop, tablet e mobile
- ✅ **Modo Escuro/Claro:** Toggle de tema com preferência salva
- ✅ **D3.js v7:** Visualização dinâmica baseada em dados
- ✅ **SVG Escalável:** Qualidade em qualquer resolução

### Interatividade
- ✅ **Cliques Interativos:** Clique em táxons para ver detalhes
- ✅ **Painéis de Informação:** Descrições científicas atualizáveis
- ✅ **Imagens de Alta Qualidade:** Fosseis e reconstruções artísticas
- ✅ **Timeline Geológica:** Idades em milhões de anos (Ma)

### Responsividade
- **Desktop (> 1200px):** Layout lado a lado com cladograma e painel de detalhes
- **Tablet (768px - 1200px):** Layout em coluna com scroll adaptativo
- **Mobile (< 768px):** Elementos reduzidos, navegação otimizada

---

## 📁 Estrutura de Arquivos

```
Aves/
├── cladograma_aves_theropoda.html          # Arquivo principal
├── CLADOGRAM_README.md                     # Este arquivo
└── images/
    ├── theropoda_overview.jpg              # Imagem inicial
    ├── Euparkeria_capensis.png             # Euparkeria
    ├── Marasuchus_lilloensis.jpg           # Marasuchus
    ├── Guaibasaurus_candelariensis.jpg     # Guaibasaurus
    ├── Coelophysis_bauri.jpg               # Coelophysis
    ├── Archaeopteryx_caçando_um_jovem.jpg  # Archaeopteryx
    ├── Life reconstruction of Confuciusornis shifan..jpg  # Confuciusornis
    └── Neornithes_species.png              # Aves modernas
```

---

## 🚀 Como Usar

### Localmente
1. Baixe ou clone o repositório
2. Abra `cladograma_aves_theropoda.html` em um navegador web
3. Clique nos táxons para explorar informações

### Online
- Acesse através do GitHub Pages (quando configurado)
- Compatível com navegadores modernos (Chrome, Firefox, Safari, Edge)

### Servidores de Teste
```bash
# Python 3
python -m http.server 8000

# Node.js
http-server

# Live Server (VS Code)
# Pressione F1 > Live Server: Open with Live Server
```

---

## 🔬 Bases Científicas

Este cladograma foi baseado em:

1. **Foth & Rauhut (2017)** - Re-evaluation of Haarlem Archaeopteryx
2. **Agnolín & Novas (2013)** - Avian Ancestors
3. **Macaulay et al. (2023)** - Decoupling body shape and mass distribution
4. **Uno & Hirasawa (2023)** - Origin of the propatagium in non-avian dinosaurs
5. **Nebreda et al. (2021)** - Dinosaur-bird macroevolution

---

## 🛠️ Tecnologias

- **HTML5** - Estrutura semântica
- **CSS3** - Estilos responsivos com custom properties
- **JavaScript (ES6+)** - Lógica interativa
- **D3.js v7** - Visualização de dados
- **Git & GitHub** - Controle de versão

---

## 🎯 Grupos Taxonômicos

```
Archosauromorpha (245-190 Ma)
│
├─ Euparkeria
└─ [branching] →
    │
    ├─ Dinosauromorpha (235-225 Ma)
    │  │
    │  ├─ Marasuchus
    │  └─ Guaibasaurus
    │
    └─ Theropoda (215 Ma - Presente)
       │
       ├─ Coelophysis (Terópode basal)
       │
       ├─ Archaeopteryx (Fóssil transicional)
       │
       ├─ Confuciusornis (Ave primitiva)
       │
       └─ Neornithes (Aves modernas - 10.000+ espécies)
```

---

## 📊 Timeline Geológico

| Táxon | Período | Idade (Ma) | Ambiente |
|-------|---------|-----------|----------|
| Euparkeria | Triássico Médio | 245 | Semi-aquático |
| Marasuchus | Triássico Médio | 235 | Terrestre |
| Guaibasaurus | Triássico Superior | 225 | Terrestre |
| Coelophysis | Triássico Superior | 215 | Desértico |
| Archaeopteryx | Jurássico Superior | 150 | Florestal |
| Confuciusornis | Cretáceo Inferior | 125 | Lacustre |
| Neornithes | Cretáceo Superior-Presente | 0 | Global |

---

## 💡 Recursos Educacionais

- **Modo Escuro:** Reduz fadiga visual em ambientes com pouca luz
- **Descrições Científicas:** Adaptadas para público educacional
- **Imagens de Qualidade:** Fosseis reais e reconstruções artísticas validadas
- **Timeline Visual:** Facilita compreensão de escala temporal

---

## 🔄 Atualizações Futuras

- [ ] Adicionar mais táxons intermediários
- [ ] Integrar dados de caracteres morfológicos
- [ ] Adicionar áudio com explicações
- [ ] Versão interativa com zoom
- [ ] Exportar como PDF/SVG

---

## 👤 Autor

**Caetano Ronan**  
Universidade Federal de Santa Catarina (UFSC)  
Projeto: Origem das Aves em Theropoda

---

## 📜 Licença

Este projeto é parte do repositório `origem-aves-theropoda`.  
Consulte o LICENSE principal para detalhes.

---

## 🔗 Referências Externas

- [D3.js Documentation](https://d3js.org)
- [The Theropod Dinosaur Database](http://www.theropoddatabase.com/)
- [Avibase - Bird Checklists](https://avibase.bsc-eoc.org/)

---

## 📧 Contato

Para sugestões, correções ou colaborações, entre em contato através do GitHub Issues.

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0.0
