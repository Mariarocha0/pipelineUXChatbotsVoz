import librosa
import numpy as np
from transformers import pipeline

# -------------------------------------------------------------
#   Módulo de EXTRAÇÃO DE FEATURES
#   Aqui eu concentro tudo o que o pipeline precisa em termos
#   de métricas numéricas extraídas do áudio e da transcrição.
#
#   - Pitch (F0)
#   - Energia / Intensidade
#   - Velocidade de fala
#   - Duração do áudio
#   - Sentimento do texto usando IA
# -------------------------------------------------------------

# Carrego o modelo de sentimento apenas uma vez.
# Escolhi 'distilbert-base-uncased-finetuned-sst-2-english'
# por ser leve, rápido e já conhecido na literatura.
print("🔍 Carregando modelo de análise de sentimento...")
sentiment_model = pipeline("sentiment-analysis")
print("✔️ Modelo de sentimento carregado!")


def extrair_features_audio(caminho_audio: str) -> dict:
    """
    Extrai métricas diretamente do arquivo de áudio (.wav)

    Retorna:
      - duracao
      - taxa_de_fala (estimada)
      - pitch_medio
      - energia_media
    """

    print(f"🎧 Carregando áudio: {caminho_audio}")

    # Carrega o áudio com a taxa padrão do librosa (22.050 Hz)
    sinal, sr = librosa.load(caminho_audio, sr=None)

    # ----------------------
    # 1. DURAÇÃO DO ÁUDIO
    # ----------------------
    duracao = librosa.get_duration(y=sinal, sr=sr)

    # ----------------------
    # 2. ENERGIA / INTENSIDADE
    # ----------------------
    # Energia média = média da amplitude ao quadrado
    energia_media = float(np.mean(sinal**2))

    # ----------------------
    # 3. PITCH (F0)
    # ----------------------
    # O método yin é simples e funciona bem para voz humana
    try:
        pitches = librosa.yin(
            y=sinal,
            fmin=50,
            fmax=300,
            sr=sr
        )
        pitch_medio = float(np.mean(pitches))
    except:
        pitch_medio = 0.0  # fallback caso o áudio seja silencioso demais

    # ----------------------
    # 4. TAXA DE FALA (estimada)
    # ----------------------
    # Aqui faço algo simples: identifico picos de energia
    # como "pedaços falados", depois divido pela duração.
    frames = librosa.onset.onset_detect(y=sinal, sr=sr)
    taxa_de_fala = len(frames) / duracao if duracao > 0 else 0

    print("📊 Features de áudio extraídas!")
    return {
        "duracao": duracao,
        "energia_media": energia_media,
        "pitch_medio": pitch_medio,
        "taxa_de_fala": taxa_de_fala,
    }


def dividir_em_chunks(texto, max_palavras=120):
    """
    Divido o texto em pequenos blocos (chunks),
    porque o modelo de sentimento não aceita textos grandes demais.
    """
    palavras = texto.split()
    for i in range(0, len(palavras), max_palavras):
        yield " ".join(palavras[i:i + max_palavras])


def extrair_sentimento(texto: str) -> dict:
    """
    Agora faço:
      - Divisão do texto em blocos menores
      - Avaliação de sentimento por bloco
      - Média dos scores
      - Determinação do sentimento final
    """

    if not texto.strip():
        return {"sentimento": "neutro", "score": 0.0, "chunks": 0}

    print("💬 Analisando sentimento em blocos...")

    chunks = list(dividir_em_chunks(texto, max_palavras=120))
    resultados = []
    labels = []

    for ch in chunks:
        try:
            r = sentiment_model(ch)[0]
            resultados.append(r["score"])
            labels.append(r["label"])
        except:
            resultados.append(0.0)
            labels.append("neutral")

    # Score médio
    score_medio = float(np.mean(resultados))

    # Sentimento final = o que mais apareceu
    sentimento_final = max(set(labels), key=labels.count)

    return {
        "sentimento": sentimento_final,
        "score": score_medio,
        "chunks": len(chunks)
    }

def extrair_features_completas(caminho_audio: str, texto_transcrito: str) -> dict:
    """
    Função principal que junta TUDO:
      - features do áudio
      - features do texto (sentimento)
    """
    dados_audio = extrair_features_audio(caminho_audio)
    dados_sentimento = extrair_sentimento(texto_transcrito)

    # Junto tudo em um único dicionário limpinho
    return {
        **dados_audio,
        **dados_sentimento
    }

