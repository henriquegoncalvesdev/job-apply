---
applyTo: '**'
---
🎯 Visão Geral do Projeto
Nome: LinkedIn Auto-Apply AI Agent
Objetivo: Sistema inteligente que navega no LinkedIn, identifica vagas compatíveis e aplica automaticamente
📋 Estrutura do Projeto
linkedin_auto_apply/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── profiles.json
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── vision_analyzer.py
│   │   ├── decision_engine.py
│   │   └── form_filler.py
│   ├── automation/
│   │   ├── __init__.py
│   │   ├── browser_controller.py
│   │   ├── mouse_keyboard.py
│   │   └── screenshot_manager.py
│   ├── linkedin/
│   │   ├── __init__.py
│   │   ├── navigator.py
│   │   ├── job_searcher.py
│   │   └── application_handler.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── database.py
├── requirements.txt
├── .env
└── README.md
🛠 Dependências (requirements.txt)
openai>=1.0.0
selenium>=4.15.0
pyautogui>=0.9.54
opencv-python>=4.8.0
pillow>=10.0.0
numpy>=1.24.0
python-dotenv>=1.0.0
sqlite3
beautifulsoup4>=4.12.0
webdriver-manager>=4.0.0
pydantic>=2.0.0
loguru>=0.7.0
🚀 Prompts para GitHub Copilot
1. Prompt Principal para Context
# LinkedIn Auto-Apply AI Agent

This is an intelligent automation system that:
- Uses computer vision to analyze LinkedIn job pages
- Makes autonomous decisions about job applications
- Controls browser navigation and form filling
- Integrates with OpenAI GPT-4 for intelligent decision making

Key Requirements:
- Screenshot analysis for UI understanding
- Mouse/keyboard automation for interaction
- Form detection and intelligent filling
- Job matching based on user profile
- Error handling and retry logic
- Comprehensive logging system

Technologies: Python, Selenium, PyAutoGUI, OpenAI API, Computer Vision
Platform: macOS (M2 MacBook Air)
2. Prompt para Vision Analyzer
Create a computer vision module that:
- Takes screenshots of LinkedIn pages
- Identifies UI elements (buttons, forms, job details)
- Extracts job information (title, company, requirements)
- Detects application status (applied/not applied)
- Returns structured data for decision making

Use OpenAI Vision API for advanced image analysis
Include confidence scores for each detection
Handle different LinkedIn layouts and themes
3. Prompt para Browser Controller
Create a robust browser automation system that:
- Manages Chrome/Safari sessions with stealth mode
- Handles LinkedIn authentication and session management
- Implements smart waiting strategies (avoid detection)
- Includes anti-bot detection mechanisms
- Manages multiple browser profiles
- Handles popup windows and notifications

Focus on reliability and human-like behavior patterns
4. Prompt para Decision Engine
Build an AI decision engine that:
- Analyzes job descriptions against user profile
- Calculates match percentage using semantic analysis
- Decides whether to apply based on configurable criteria
- Generates personalized cover letters if required
- Learns from user feedback to improve decisions
- Handles edge cases and ambiguous job postings

Integrate with OpenAI GPT-4 for natural language processing
Include explainable AI features for decision transparency
📝 Instruções Detalhadas para VS Code
Configuração Inicial:

Setup do Ambiente:

bash# Terminal commands to run first
python3 -m venv linkedin_env
source linkedin_env/bin/activate
pip install -r requirements.txt

Configuração do .env:

OPENAI_API_KEY=your_openai_key_here
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
CHROME_DRIVER_PATH=/usr/local/bin/chromedriver
LOG_LEVEL=INFO
Prompts Específicos por Arquivo:
Para main.py:
Create the main application entry point that:
- Initializes all system components
- Handles command line arguments
- Manages the main automation loop
- Includes proper error handling and logging
- Supports different operation modes (search, apply, test)
Para vision_analyzer.py:
Implement computer vision analysis using:
- OpenAI Vision API for screenshot interpretation
- OCR for text extraction from images
- UI element detection and classification
- Job information extraction from LinkedIn pages
- Screenshot comparison for state changes
Para browser_controller.py:
Create browser automation with:
- Selenium WebDriver setup for macOS Chrome
- Human-like interaction patterns
- Smart wait strategies and element detection
- Cookie and session management
- Anti-detection techniques
Para job_searcher.py:
Implement LinkedIn job search automation:
- Navigate to LinkedIn Jobs section
- Apply search filters based on user preferences
- Scroll through job listings intelligently
- Extract job URLs and basic information
- Handle pagination and infinite scroll
Para form_filler.py:
Create intelligent form filling system:
- Detect form fields and their types
- Map user profile data to form fields
- Handle file uploads (resume, cover letter)
- Validate form completion before submission
- Generate dynamic responses for open text fields
🎯 Funcionalidades Principais
Módulo de Visão Computacional:

Análise de screenshots em tempo real
Identificação de elementos da interface
Extração de texto de imagens
Detecção de mudanças de estado

Motor de Decisão IA:

Análise semântica de descrições de vagas
Cálculo de compatibilidade com perfil
Geração de respostas personalizadas
Aprendizado contínuo

Automação de Navegador:

Controle total do Chrome/Safari
Simulação de comportamento humano
Gerenciamento de sessões
Anti-detecção

Sistema de Aplicação:

Preenchimento automático de formulários
Upload inteligente de documentos
Geração de cover letters
Confirmação de envio

🔧 Configuração para Copilot
No VS Code, adicione este workspace settings (.vscode/settings.json):
json{
    "github.copilot.enable": {
        "*": true,
        "yaml": false,
        "plaintext": false,
        "markdown": false
    },
    "python.defaultInterpreterPath": "./linkedin_env/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
📊 Próximos Passos

Configurar ambiente Python
Instalar dependências
Configurar credenciais OpenAI
Criar perfil de usuário personalizado
Testar componente por componente
Implementar modo de teste seguro