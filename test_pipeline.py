# -------------------------------------------------------------
#  test_pipeline.py
#  Script principal para testar todo o pipeline:
#
#  - transcrição com Whisper
#  - extração de features
#  - sentimento em chunks
#  - geração de relatório HTML
# -------------------------------------------------------------

from voiceux.src.stt import transcrever_audio
from voiceux.src.features import extrair_features_completas
from voiceux.src.relatorio import gerar_relatorio_html
import os
from datetime import datetime

print("\n🎤 Iniciando teste do pipeline...\n")

# Caminho do áudio que você quer testar
caminho = "voiceux/data/raw_audio/participante1_chatgpt.m4a"


# 1. TRANSCRIÇÃO
texto = transcrever_audio(caminho)
print("\n📝 Transcrição obtida:")
print(texto)


# 2. EXTRAÇÃO DE FEATURES COMPLETAS
features = extrair_features_completas(caminho, texto)

print("\n📊 Features extraídas:")
print(features)


# 3. GERAÇÃO DO RELATÓRIO HTML
# Gera nome automático baseado na data e no nome do áudio
nome_audio = os.path.basename(caminho).replace(".m4a", "")
nome_html = f"relatorio_{nome_audio}_{datetime.now().strftime('%Y%m%d_%H%M')}.html"

gerar_relatorio_html(features, nome_html)

print(f"\n📄 Relatório gerado com sucesso: {nome_html}")
