import os
from pathlib import Path
from stt import transcrever_audio
from features import extrair_caracteristicas
import pandas as pd

# -------------------------------------------------------------
#  Pipeline Principal do Projeto de Avaliação de UX em Chatbots de Voz
#  Neste script eu junto todas as etapas do pipeline:
#  1) Carrega os áudios reais dos participantes
#  2) Gera a transcrição com Whisper
#  3) Extrai características prosódicas e emocionais
#  4) Salva tudo organizado em CSV para análises posteriores
#
#  Esse arquivo é o coração do pipeline :)
# -------------------------------------------------------------

# Diretórios importantes do pipeline
RAW_AUDIO_DIR = Path("../data/raw_audio")     # Onde ficam os áudios brutos (.wav)
TRANSCRIPTS_DIR = Path("../data/transcripts") # Onde salvo as transcrições
FEATURES_DIR = Path("../data/features")       # Onde ficará o dataset final

def garantir_pastas():
    """
    Crio automaticamente as pastas necessárias.
    É só pra evitar erro caso alguma pasta ainda não exista.
    """
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    FEATURES_DIR.mkdir(parents=True, exist_ok=True)

def processar_audios():
    """
    Essa função processa TODOS os áudios que estiverem dentro de raw_audio.
    Para cada áudio, eu gero a transcrição, extraio os features
    e depois junto tudo em um dataset final.
    """
    garantir_pastas()  # garante estruturas

    dados = []  # Aqui vou armazenar todos os resultados das features

    # Loop para percorrer todos os arquivos .wav na pasta
    for arquivo in RAW_AUDIO_DIR.glob("*.wav"):
        print(f"\n Processando: {arquivo.name}")

        # ------------------------- 1) TRANSCRIÇÃO -------------------------
        texto = transcrever_audio(str(arquivo))  # Whisper faz a transcrição

        # Salvo a transcrição em .txt separado (útil para conferência depois)
        transcript_path = TRANSCRIPTS_DIR / f"{arquivo.stem}.txt"
        transcript_path.write_text(texto, encoding="utf-8")

        # ------------------------- 2) FEATURES ----------------------------
        # Aqui eu extraio características como pitch, taxa de fala, emoção, etc.
        feats = extrair_caracteristicas(str(arquivo))

        # Adiciono informações complementares
        feats["arquivo"] = arquivo.name
        feats["transcricao"] = texto
        
        # Guardo os dados para o CSV final
        dados.append(feats)

    # ------------------------- 3) DATASET FINAL --------------------------
    df = pd.DataFrame(dados)

    # CSV com todas as informações estruturadas
    df.to_csv(FEATURES_DIR / "dataset_final.csv", index=False, encoding="utf-8")

    print("\n🎉 Pipeline concluído!")
    print("Resultado salvo em: data/features/dataset_final.csv")

if __name__ == "__main__":
    processar_audios()
