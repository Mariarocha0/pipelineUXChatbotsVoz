# VoiceUX – Pipeline de Avaliação de Experiência do Usuário (UX) em Chatbots de Voz com Inteligência Artificial

## Descrição Geral

O **VoiceUX** é um pipeline desenvolvido para **avaliar a Experiência do Usuário (UX)** em **chatbots de voz (voicebots)**, utilizando técnicas de **Inteligência Artificial** e **análise multimodal de fala**.  
O projeto tem como foco identificar como fatores como **naturalidade da fala**, **tempo de resposta**, **clareza da voz sintetizada** e **emoções do usuário** influenciam na percepção de qualidade durante a interação.

Este trabalho foi desenvolvido no contexto de um **projeto acadêmico de TCC**, com aplicação prática em três chatbots amplamente utilizados: **GPT, Gemini e Copilot**.

---

## Objetivos

- Desenvolver e aplicar um **pipeline automatizado de avaliação UX** em chatbots de voz.  
- Medir **métricas quantitativas e qualitativas** de experiência (taxa de repetição, turnos, naturalidade, emoção, satisfação).  
- Utilizar IA para **analisar e prever a satisfação** do usuário com base em padrões de voz e diálogo.  
- Gerar **relatórios e dashboards interativos** com insights sobre desempenho e usabilidade.

---

## Estrutura do Projeto

voiceux/
│
├── data/
│   ├── raw_audio/             # Áudios originais das interações (usuário + chatbot)
│   ├── transcripts/           # Transcrições geradas por modelos de STT (Whisper, Google)
│   ├── features/              # Características extraídas (pitch, energia, tempo, emoção)
│   └── final_dataset.csv      # Base consolidada com todas as métricas e avaliações
│
├── src/
│   ├── stt.py                 # Transcrição de áudio (Speech-to-Text)
│   ├── features.py            # Extração de características de áudio e texto
│   ├── metrics.py             # Cálculo de métricas de UX (taxa de repetição, turnos, etc.)
│   ├── modeling.py            # Predição de satisfação do usuário com IA
│
├── notebooks/
│   └── analysis.ipynb         # Análises exploratórias e gráficos simples
│
├── docs/
│   └── metodologia_pipeline.md # Descrição técnica e metodológica do pipeline
│
├── logs/
│   └── execution.log          # Registro simples das execuções
│
├── requirements.txt           # Dependências do ambiente Python
└── README.md                  # Documento de apresentação do projeto


## Contato
Maria Luiza Ribeiro Rocha
Linkedin: https://www.linkedin.com/in/marialuizaribeirorocha/
