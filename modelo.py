# modelo_avc.py
import joblib
import numpy as np

# Carrega o modelo treinado
modelo = joblib.load("./model/modelo_xgb_otimizado_avc.pkl")

def prever_probabilidade(dados):
    """
    Recebe um dicionário com os dados do formulário e retorna a probabilidade de AVC.
    """

    entrada = [
        {"masculino": 1, "feminino": 0, "outro": 2}[dados["genero"]],
        int(dados["idade"]),
        1 if dados["hipertensao"] == "sim" else 0,
        1 if dados["cardiaca"] == "sim" else 0,
        1 if dados["casado"] == "sim" else 0,
        {"crianca": 4, "funcionario_publico": 0, "nunca_trabalhou": 1, "area_privada": 2, "autonomo": 3}[dados["trabalho"]],
        {"rural": 0, "urbano": 1}[dados["residencia"]],
        int(dados["glicose"]),
        float(dados["imc"]),
        {"ex_fumante": 1, "nunca_fumou": 2, "fuma": 3}[dados["fumante"]]  
    ]

    entrada_array = np.array(entrada).reshape(1, -1)
    probabilidade = modelo.predict_proba(entrada_array)[0][1] * 100
    return round(probabilidade, 2)