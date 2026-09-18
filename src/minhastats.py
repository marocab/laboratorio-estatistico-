"""
minhastats.py
Núcleo estatístico implementado "na mão" (sem usar funções prontas
de estatística de bibliotecas como numpy, scipy ou statistics).

Cada função aqui será validada em testes/test_minhastats.py,
comparando o resultado com o NumPy/SciPy.
"""


def media(dados):
    """Calcula a média aritmética de uma lista de números."""
    return sum(dados) / len(dados)


def mediana(dados):
    """Calcula a mediana de uma lista de números."""
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2

    if n % 2 == 0:
        return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
    else:
        return dados_ordenados[meio]


def moda(dados):
    """
    Calcula a(s) moda(s) de uma lista de números.
    Retorna uma lista, pois pode haver mais de uma moda (multimodal).
    """
    contagem = {}
    for valor in dados:
        contagem[valor] = contagem.get(valor, 0) + 1

    frequencia_maxima = max(contagem.values())
    modas = [valor for valor, freq in contagem.items() if freq == frequencia_maxima]

    return sorted(modas)


def variancia(dados, populacional=False):
    """
    Calcula a variância de uma lista de números.

    populacional=False (padrão): variância AMOSTRAL, divide por (n-1)
    populacional=True: variância POPULACIONAL, divide por n
    """
    n = len(dados)
    media_dados = media(dados)
    soma_dos_quadrados = sum((x - media_dados) ** 2 for x in dados)

    if populacional:
        return soma_dos_quadrados / n
    else:
        return soma_dos_quadrados / (n - 1)


def desvio_padrao(dados, populacional=False):
    """
    Calcula o desvio padrão de uma lista de números.
    É simplesmente a raiz quadrada da variância.
    """
    return variancia(dados, populacional=populacional) ** 0.5


def amplitude(dados):
    """Calcula a amplitude (diferença entre o maior e o menor valor)."""
    return max(dados) - min(dados)


def percentil(dados, p):
    """
    Calcula o percentil p (0 a 100) de uma lista de números,
    usando interpolação linear (mesmo método padrão do NumPy).
    """
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    posicao = (p / 100) * (n - 1)
    posicao_inferior = int(posicao)
    posicao_superior = min(posicao_inferior + 1, n - 1)
    fracao = posicao - posicao_inferior

    valor_inferior = dados_ordenados[posicao_inferior]
    valor_superior = dados_ordenados[posicao_superior]

    return valor_inferior + fracao * (valor_superior - valor_inferior)


def quartis(dados):
    """
    Retorna um dicionário com Q1 (25%), Q2 (50%, = mediana) e Q3 (75%).
    Útil para detectar outliers com a regra do IQR (Q3 - Q1).
    """
    return {
        "Q1": percentil(dados, 25),
        "Q2": percentil(dados, 50),
        "Q3": percentil(dados, 75),
    }


def coeficiente_variacao(dados, populacional=False):
    """
    Calcula o coeficiente de variação (CV): desvio padrão / média.
    Útil para comparar a dispersão de variáveis com escalas diferentes.
    """
    return desvio_padrao(dados, populacional=populacional) / media(dados)


def covariancia(dados_x, dados_y, populacional=False):
    """
    Calcula a covariância entre duas listas de números de mesmo tamanho.
    Mede como duas variáveis variam juntas.
    """
    n = len(dados_x)
    media_x = media(dados_x)
    media_y = media(dados_y)

    soma_produtos = sum(
        (x - media_x) * (y - media_y) for x, y in zip(dados_x, dados_y)
    )

    if populacional:
        return soma_produtos / n
    else:
        return soma_produtos / (n - 1)


def correlacao_pearson(dados_x, dados_y):
    """
    Calcula o coeficiente de correlação de Pearson entre duas variáveis.
    Varia de -1 (negativa perfeita) a +1 (positiva perfeita).
    0 significa que não há correlação linear.
    """
    cov = covariancia(dados_x, dados_y, populacional=False)
    desvio_x = desvio_padrao(dados_x, populacional=False)
    desvio_y = desvio_padrao(dados_y, populacional=False)

    return cov / (desvio_x * desvio_y)
