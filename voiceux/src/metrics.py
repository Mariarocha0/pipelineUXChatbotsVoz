# -------------------------------------------------------------
#   Módulo de MÉTRICAS DE UX
#   Aqui eu calculo medidas simples baseadas na transcrição,
#   úteis para entender o comportamento do usuário no chatbot.
#
#   - número de turnos
#   - palavras por minuto
#   - taxa de repetição
#   - tamanho médio das mensagens
# -------------------------------------------------------------

import re

def contar_turnos(transcricao: str) -> int:
    """
    Conta quantas 'falas' existem na transcrição.
    Eu considero cada linha como um turno.
    """
    if not transcricao:
        return 0

    linhas = [l.strip() for l in transcricao.split("\n") if l.strip()]
    return len(linhas)


def palavras_por_minuto(transcricao: str, duracao_audio: float) -> float:
    """
    Cálculo bem simples:
    total_de_palavras / (duracao_em_minutos)
    """
    if not transcricao or duracao_audio <= 0:
        return 0.0

    palavras = transcricao.split()
    minutos = duracao_audio / 60
    return len(palavras) / minutos


def taxa_de_repeticao(transcricao: str) -> float:
    """
    Mede repetição de palavras:
    (palavras repetidas / total_de_palavras)
    """
    if not transcricao:
        return 0.0

    palavras = [p.lower() for p in re.findall(r"\w+", transcricao)]
    total = len(palavras)
    if total == 0:
        return 0.0

    repetidas = [p for p in set(palavras) if palavras.count(p) > 1]
    return len(repetidas) / total


def tamanho_medio_mensagem(transcricao: str) -> float:
    """
    Média de palavras por turno.
    """
    if not transcricao:
        return 0.0

    linhas = [l.strip() for l in transcricao.split("\n") if l.strip()]
    if not linhas:
        return 0.0

    return sum(len(l.split()) for l in linhas) / len(linhas)


def calcular_metricas_completas(transcricao: str, duracao_audio: float) -> dict:
    """
    Retorna todas métricas juntas.
    """
    return {
        "turnos": contar_turnos(transcricao),
        "ppm": palavras_por_minuto(transcricao, duracao_audio),
        "taxa_repeticao": taxa_de_repeticao(transcricao),
        "tamanho_medio_msg": tamanho_medio_mensagem(transcricao),
    }
