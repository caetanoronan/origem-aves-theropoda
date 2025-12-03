@echo off
chcp 65001 > nul
REM Script de Inicialização Rápida
REM Projeto: Origem das Aves em Theropoda

color 0B
title Extração de Imagens - Origem das Aves

echo.
echo ========================================================================
echo.
echo           🦅 EXTRAÇÃO DE IMAGENS DE PDFs CIENTÍFICOS
echo              Origem das Aves em Theropoda
echo.
echo ========================================================================
echo.

REM Verificar se Python está instalado
python --version > nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale Python 3.8 ou superior:
    echo    https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version
echo.

REM Verificar se as dependências estão instaladas
echo 🔍 Verificando dependências...
echo.

python -c "import fitz" > nul 2>&1
if errorlevel 1 (
    echo ⚠️  PyMuPDF não instalado
    echo 📦 Instalando PyMuPDF...
    pip install PyMuPDF
    echo.
)

python -c "from PIL import Image" > nul 2>&1
if errorlevel 1 (
    echo ⚠️  Pillow não instalado
    echo 📦 Instalando Pillow...
    pip install Pillow
    echo.
)

echo ✅ Todas as dependências instaladas
echo.

REM Verificar se os PDFs existem
echo 🔍 Verificando PDFs...
echo.

set PDF_COUNT=0
if exist "Origin of the propatagium in non-avian dinosaurs.pdf" (
    set /a PDF_COUNT+=1
    echo    ✅ Origin of the propatagium...
)
if exist "Decoupling body shape and mass distribution in birds and their dinosaurian ancestors.pdf" (
    set /a PDF_COUNT+=1
    echo    ✅ Decoupling body shape...
)
if exist "'Dinosaur-bird' macroevolution, locomotor modules and the origins of flight.pdf" (
    set /a PDF_COUNT+=1
    echo    ✅ Dinosaur-bird macroevolution...
)
if exist "Re-evaluation of the Haarlem Archaeopteryx and the radiation of maniraptoran theropod dinosaurs.pdf" (
    set /a PDF_COUNT+=1
    echo    ✅ Re-evaluation of Haarlem Archaeopteryx...
)
if exist "Agnoln-Novas2013-Avianancestors.pdf" (
    set /a PDF_COUNT+=1
    echo    ✅ Agnoln-Novas2013...
)

echo.
echo 📄 PDFs encontrados: %PDF_COUNT%/5
echo.

if %PDF_COUNT% LSS 5 (
    echo ⚠️  ATENÇÃO: Nem todos os PDFs foram encontrados.
    echo    Coloque os PDFs científicos na raiz do projeto.
    echo.
)

REM Criar diretórios necessários
if not exist "images" mkdir images
if not exist "scripts" (
    echo ❌ Pasta 'scripts' não encontrada!
    echo    Certifique-se de que os scripts Python estão na pasta 'scripts/'
    echo.
    pause
    exit /b 1
)

echo ========================================================================
echo.
echo 🚀 PRONTO PARA INICIAR!
echo.
echo Escolha uma opção:
echo.
echo    1. Workflow Master (Recomendado)
echo    2. Extrair Imagens dos PDFs
echo    3. Gerar Guia Visual de Mapeamento
echo    4. Renomear Imagens
echo    5. Processar e Otimizar Imagens
echo    6. Abrir Documentação (README)
echo    0. Sair
echo.
echo ========================================================================
echo.

set /p OPCAO="Digite sua escolha: "

if "%OPCAO%"=="1" (
    echo.
    echo 🚀 Iniciando Workflow Master...
    echo.
    cd scripts
    python run_workflow.py
    cd ..
    goto :fim
)

if "%OPCAO%"=="2" (
    echo.
    echo 📄 Extraindo imagens dos PDFs...
    echo.
    cd scripts
    python extract_pdf_images.py
    cd ..
    goto :fim
)

if "%OPCAO%"=="3" (
    echo.
    echo 🗺️ Gerando guia visual...
    echo.
    cd scripts
    python map_pdf_to_html.py
    cd ..
    
    if exist "image_mapping_guide.html" (
        echo.
        echo ✅ Guia gerado com sucesso!
        echo.
        set /p ABRIR="Deseja abrir o guia no navegador? (S/N): "
        if /i "%ABRIR%"=="S" (
            start "" "image_mapping_guide.html"
        )
    )
    goto :fim
)

if "%OPCAO%"=="4" (
    echo.
    echo 🔄 Iniciando renomeação de imagens...
    echo.
    cd scripts
    python rename_images.py
    cd ..
    goto :fim
)

if "%OPCAO%"=="5" (
    echo.
    echo 🎨 Iniciando processamento de imagens...
    echo.
    cd scripts
    python process_images.py
    cd ..
    goto :fim
)

if "%OPCAO%"=="6" (
    echo.
    if exist "README_SCRIPTS.md" (
        start "" "README_SCRIPTS.md"
        echo ✅ Abrindo documentação...
    ) else if exist "QUICK_START.md" (
        start "" "QUICK_START.md"
        echo ✅ Abrindo guia rápido...
    ) else (
        echo ❌ Documentação não encontrada.
    )
    goto :fim
)

if "%OPCAO%"=="0" (
    echo.
    echo 👋 Até logo!
    goto :fim
)

echo.
echo ⚠️  Opção inválida.
echo.

:fim
echo.
echo ========================================================================
echo.
pause
