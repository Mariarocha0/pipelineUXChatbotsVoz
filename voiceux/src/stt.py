import whisper
import os


# Forço o caminho do ffmpeg manualmente:
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

# -------------------------------------------------------------
#  Módulo de STT (Speech-to-Text)
#  Aqui eu faço toda a parte de transcrição de áudio usando o
#  modelo Whisper. Mantive tudo simples e organizado, para facilitar
#  a integração com o pipeline principal.
# -------------------------------------------------------------

# Carrego o modelo do Whisper apenas uma vez.
# Escolhi o modelo "small" porque oferece boa qualidade sem ficar pesado.
# Obs: se quiser mais precisão, posso trocar para "medium" ou "large".
print("Carregando modelo Whisper...")
model = whisper.load_model("small")
print("✔️ Modelo Whisper carregado!")

def transcrever_audio(caminho_audio: str) -> str:
    """
    Recebe o caminho de um arquivo de áudio (.wav) e retorna
    o texto transcrito.

    Aqui deixei simples: apenas passo o áudio para o Whisper
    e retorno a string final.
    """

    print(f"Transcrevendo áudio: {caminho_audio}")

    # Roda o whisper no áudio
    resultado = model.transcribe(caminho_audio)

    # O whisper já retorna o texto limpinho no campo 'text'
    texto = resultado.get("text", "").strip()

    print("Texto transcrito com sucesso!")
    return texto
