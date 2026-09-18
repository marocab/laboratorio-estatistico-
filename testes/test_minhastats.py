"""
test_minhastats.py
Testes automatizados que comparam nossas funções feitas "na mão"
com os resultados do NumPy e da biblioteca padrão `statistics`.

Para rodar os testes, no terminal (dentro da pasta do projeto):
    python3 -m pytest testes/test_minhastats.py -v
"""

import statistics
import numpy as np

from src.minhastats import (
    media,
    mediana,
    moda,
    variancia,
    desvio_padrao,
    amplitude,
    percentil,
    quartis,
    coeficiente_variacao,
    covariancia,
    correlacao_pearson,
)

TOLERANCIA = 1e-4

DADOS_TESTE = [10, 12, 23, 23, 16, 23, 21, 16]
# Segunda lista, do mesmo tamanho, pra testar covariância/correlação
DADOS_TESTE_Y = [5, 8, 15, 14, 10, 13, 12, 9]


def test_media():
    assert abs(media(DADOS_TESTE) - np.mean(DADOS_TESTE)) < TOLERANCIA


def test_mediana():
    assert abs(mediana(DADOS_TESTE) - np.median(DADOS_TESTE)) < TOLERANCIA


def test_moda():
    resultado_statistics = statistics.mode(DADOS_TESTE)
    assert resultado_statistics in moda(DADOS_TESTE)


def test_variancia_amostral():
    assert abs(variancia(DADOS_TESTE, populacional=False) - np.var(DADOS_TESTE, ddof=1)) < TOLERANCIA


def test_variancia_populacional():
    assert abs(variancia(DADOS_TESTE, populacional=True) - np.var(DADOS_TESTE, ddof=0)) < TOLERANCIA


def test_desvio_padrao_amostral():
    assert abs(desvio_padrao(DADOS_TESTE, populacional=False) - np.std(DADOS_TESTE, ddof=1)) < TOLERANCIA


def test_desvio_padrao_populacional():
    assert abs(desvio_padrao(DADOS_TESTE, populacional=True) - np.std(DADOS_TESTE, ddof=0)) < TOLERANCIA


def test_amplitude():
    assert abs(amplitude(DADOS_TESTE) - (np.max(DADOS_TESTE) - np.min(DADOS_TESTE))) < TOLERANCIA


def test_percentil_25():
    assert abs(percentil(DADOS_TESTE, 25) - np.percentile(DADOS_TESTE, 25)) < TOLERANCIA


def test_percentil_75():
    assert abs(percentil(DADOS_TESTE, 75) - np.percentile(DADOS_TESTE, 75)) < TOLERANCIA


def test_quartis():
    q = quartis(DADOS_TESTE)
    assert abs(q["Q1"] - np.percentile(DADOS_TESTE, 25)) < TOLERANCIA
    assert abs(q["Q2"] - np.percentile(DADOS_TESTE, 50)) < TOLERANCIA
    assert abs(q["Q3"] - np.percentile(DADOS_TESTE, 75)) < TOLERANCIA


def test_coeficiente_variacao():
    cv_nosso = coeficiente_variacao(DADOS_TESTE, populacional=False)
    cv_numpy = np.std(DADOS_TESTE, ddof=1) / np.mean(DADOS_TESTE)
    assert abs(cv_nosso - cv_numpy) < TOLERANCIA


def test_covariancia():
    cov_nosso = covariancia(DADOS_TESTE, DADOS_TESTE_Y, populacional=False)
    # np.cov retorna uma matriz 2x2; a covariância entre x e y está em [0][1]
    cov_numpy = np.cov(DADOS_TESTE, DADOS_TESTE_Y, ddof=1)[0][1]
    assert abs(cov_nosso - cov_numpy) < TOLERANCIA


def test_correlacao_pearson():
    corr_nosso = correlacao_pearson(DADOS_TESTE, DADOS_TESTE_Y)
    # np.corrcoef retorna uma matriz 2x2; a correlação está em [0][1]
    corr_numpy = np.corrcoef(DADOS_TESTE, DADOS_TESTE_Y)[0][1]
    assert abs(corr_nosso - corr_numpy) < TOLERANCIA
