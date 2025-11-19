# -------------------------------------------------------------
#   Módulo de RELATÓRIO HTML
#   - Gera um arquivo HTML com as métricas do participante
#   - Mostra a transcrição
#   - Abre automaticamente no navegador padrão
# -------------------------------------------------------------

import os
import webbrowser

def gerar_relatorio_html(features: dict, texto: str, saida="reports/relatorio.html"):
    """
    Gera um arquivo HTML apresentando:
      - métricas extraídas do áudio
      - sentimento médio
      - transcrição completa
    E abre automaticamente no navegador.
    """

    # Garante que a pasta existe
    pasta = os.path.dirname(saida)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)

    # Criação do HTML
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Relatório do Pipeline de UX</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 20px;
                background: #f4f4f4;
            }}
            h1 {{
                color: #333;
            }}
            table {{
                border-collapse: collapse;
                width: 60%;
                margin-bottom: 30px;
            }}
            table, th, td {{
                border: 1px solid #777;
            }}
            th {{
                background: #444;
                color: white;
                padding: 8px;
            }}
            td {{
                padding: 8px;
            }}
            .box {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>

    <body>
        <div class="box">
            <h1>Relatório da Análise do Chatbot</h1>

            <h2>Métricas Extraídas</h2>
            <table>
                <tr><th>Métrica</th><th>Valor</th></tr>
                <tr><td>Pitch médio</td><td>{features.get("pitch_medio", 0):.2f} Hz</td></tr>
                <tr><td>Energia média</td><td>{features.get("energia_media", 0):.6f}</td></tr>
                <tr><td>Duração</td><td>{features.get("duracao", 0):.2f} s</td></tr>
                <tr><td>Taxa de fala</td><td>{features.get("taxa_de_fala", 0):.2f} eventos/s</td></tr>
                <tr><td>Sentimento</td><td>{features.get("sentimento", "N/A")}</td></tr>
                <tr><td>Score</td><td>{features.get("score", 0):.2f}</td></tr>
                <tr><td>Chunks avaliados</td><td>{features.get("chunks", 1)}</td></tr>
            </table>

            <h2>Transcrição Completa</h2>
            <p>{texto}</p>
        </div>
    </body>
    </html>
    """

    # Salva o HTML
    with open(saida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f" Relatório gerado: {saida}")

    # Abre o arquivo no navegador
    caminho_absoluto = os.path.abspath(saida)
    webbrowser.open(f"file:///{caminho_absoluto}")

    print(" Relatório aberto no navegador!")


