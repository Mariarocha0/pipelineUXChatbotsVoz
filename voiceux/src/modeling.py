# -------------------------------------------------------------
#   Módulo de MODELAGEM (IA)
#   Aqui eu defino um modelo SUPER simples de regressão
#   apenas para demonstrar a ideia:
#
#   - treino do modelo
#   - predição de satisfação do usuário
#
#   Obs: Não é para ser um modelo real de produção,
#        é só ilustrativo para o pipeline do TCC.
# -------------------------------------------------------------

import numpy as np
from sklearn.linear_model import LinearRegression

class ModeloSatisfacao:
    """
    Modelo simples de regressão linear
    para prever satisfação (0 a 1)
    usando features numéricas do pipeline.
    """

    def __init__(self):
        self.model = LinearRegression()

    def treinar(self, X: np.ndarray, y: np.ndarray):
        """
        Treina o modelo com features e rótulos.
        """
        print("🤖 Treinando modelo de satisfação...")
        self.model.fit(X, y)
        print("✔️ Modelo treinado!")

    def prever(self, features: dict) -> float:
        """
        Recebe features e retorna uma predição entre 0 e 1.
        """
        vetor = np.array(list(features.values())).reshape(1, -1)
        pred = self.model.predict(vetor)[0]

        # Faço um clamp para garantir que fique entre 0 e 1
        return max(0.0, min(1.0, float(pred)))
