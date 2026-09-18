# Sistematização — Matemática e Estatística para Computação: Construindo o Seu Laboratório Estatístico

**Aluna:** Maria Mariana Barreto Carvalho — RA/DRT: 72650444
**Disciplina:** Matemática e Estatística para Computação — Turma B - 0726
**Instituição:** UniCEUB

---

## 1. Dataset escolhido e justificativa

**Dataset:** World Happiness Report (2005–presente)
**Fonte:** [Kaggle — World Happiness Report, 2005-Present](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present)

O dataset reúne dados de mais de 2.000 observações (país × ano), medindo o índice de felicidade autorreportado (*Life Ladder*) de cada país ao longo de quase duas décadas, junto com variáveis socioeconômicas explicativas.

**Justificativa da escolha:** o tema "países e pessoas" desperta curiosidade genuína e permite análises ricas — comparações entre nações, evolução temporal e relações causais candidatas (PIB, saúde, liberdade). O dataset atende integralmente aos requisitos do Módulo 0:

- **Registros:** ~2.200 linhas (> 1.000 exigido)
- **Variáveis numéricas (10):** Life Ladder, Log GDP per capita, Social support, Healthy life expectancy at birth, Freedom to make life choices, Generosity, Perceptions of corruption, Positive affect, Negative affect, Confidence in national government
- **Variáveis categóricas (3):** Country name, Regional indicator, Year

## 2. Núcleo estatístico — fórmulas implementadas

Todas as funções abaixo foram implementadas em `src/minhastats.py`, sem uso de bibliotecas prontas de estatística, e validadas contra o NumPy (Módulo 1).

### Média

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

### Mediana

Valor central da lista ordenada (ou média dos dois valores centrais, se `n` for par).

### Moda

Valor(es) de maior frequência na amostra.

### Variância

- **Amostral** (usada por padrão, pois trabalhamos com amostras de uma população maior):

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$$

- **Populacional:**

$$\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}$$

### Desvio padrão

$$s = \sqrt{s^2} \qquad \sigma = \sqrt{\sigma^2}$$

### Amplitude

$$A = x_{max} - x_{min}$$

### Percentil / Quartis

Calculados por interpolação linear na lista ordenada (mesmo método padrão do NumPy), com Q1 = percentil 25, Q2 = percentil 50 (mediana) e Q3 = percentil 75.

### Coeficiente de variação

$$CV = \frac{s}{\bar{x}}$$

### Covariância

$$\text{Cov}(X,Y) = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{n - 1}$$

### Correlação de Pearson

$$r = \frac{\text{Cov}(X,Y)}{s_X \cdot s_Y}$$

### Regressão linear simples (mínimos quadrados)

$$b_1 = \frac{\text{Cov}(X,Y)}{\text{Var}(X)} \qquad b_0 = \bar{y} - b_1 \bar{x}$$

$$\hat{y} = b_1 x + b_0$$

## 3. Validação contra bibliotecas de referência

Todas as 14 funções foram testadas em `testes/test_minhastats.py`, comparando cada resultado com o NumPy (`np.mean`, `np.median`, `np.var`, `np.std`, `np.percentile`, `np.cov`, `np.corrcoef`) e com a biblioteca `statistics` (para moda), usando tolerância numérica de **1e-4**.

**Resultado:** 14/14 testes aprovados (`14 passed`), com diferenças na ordem de 1e-15 (erro de ponto flutuante, sem significância prática).

Exemplo de validação com dados reais (Life Ladder do Brasil, 17 observações):

| Medida | Nossa função | NumPy |
|---|---|---|
| Média | 6.563505817882352 | 6.563505817882352 |
| Mediana | 6.546896935 | 6.546896935 |
| Variância amostral | 0.12093225430199726 | 0.12093225430199725 |
| Desvio padrão amostral | 0.34775315139046153 | 0.34775315139046153 |

## 4. Módulos implementados

- **Módulo 0 — Dados reais:** carregamento do CSV via `pandas`, normalização de nomes de colunas.
- **Módulo 1 — Núcleo estatístico próprio:** descrito na seção 2.
- **Módulo 2 — Estatística descritiva interativa:** seleção de variável (numérica ou categórica), tabela de frequências (regra de Sturges para número de classes), medidas de tendência central e dispersão, quartis, detecção de outliers pela regra do IQR (`Q1 - 1.5×IQR` a `Q3 + 1.5×IQR`), interpretação automática de assimetria (comparação média × mediana), histograma e boxplot.
- **Módulo 3 — Probabilidade e simulação:**
  - **Lei dos Grandes Números:** simulação de lançamentos de moeda (0/1), com gráfico de convergência da frequência relativa até a probabilidade teórica (0,5), controlado por slider de número de lançamentos.
  - **Teorema Central do Limite:** amostragem repetida de uma variável do dataset, cálculo da média de cada amostra, e histograma da distribuição das médias amostrais — controlado por sliders de número de repetições e tamanho da amostra.
- **Módulo 4 — Distribuições teóricas:** sobreposição da curva Normal (parâmetros estimados dos dados) e de uma segunda distribuição à escolha do usuário (Uniforme ou Exponencial) sobre o histograma real da variável.
- **Módulo 5 — Correlação e regressão linear:** seleção de duas variáveis numéricas (X e Y), diagrama de dispersão com reta de regressão, equação da reta, coeficiente de correlação de Pearson, R², interpretação dos coeficientes, campo de predição interativa (usuário digita X, aplicação retorna Ŷ), e alerta de que correlação não implica causalidade.
- **Módulo 6 — Relatório de descobertas:** descrito na seção 5.

## 5. As 3 descobertas estatísticas mais interessantes

### Descoberta 1 — A felicidade tem geografia: o topo do ranking é dominado por países nórdicos e europeus

Calculando a média histórica de `life_ladder` por país, os cinco primeiros colocados são Dinamarca (7,673), Finlândia (7,619), Noruega (7,482), Suíça (7,474) e Islândia (7,459) — todos países do norte/centro da Europa com sistemas de bem-estar social consolidados. Ao cruzar com o Módulo 5, `social_support` (r = 0,722) e `healthy_life_expectancy_at_birth` (r = 0,713) — fatores fortemente presentes nesses países — estão entre as variáveis mais correlacionadas com a felicidade.

### Descoberta 2 — O Brasil está consistentemente acima da média mundial, com felicidade estável ao longo do tempo

O Brasil registra média de `life_ladder` de **6,564**, contra uma média mundial de **5,479** — quase 1,1 ponto acima, na escala de 0 a 10. O desvio padrão do Brasil ao longo dos 17 anos de observação é de apenas **0,348**, indicando estabilidade na percepção de bem-estar da população, mesmo diante de oscilações político-econômicas conhecidas do período. Em contraste, o Líbano registrou a maior queda de todo o dataset (-3,14 pontos entre o primeiro e o último ano observado), refletindo a grave crise econômica iniciada em 2019, agravada pela explosão no porto de Beirute em 2020 e pela instabilidade política e de segurança posterior.

### Descoberta 3 — O PIB per capita é a variável isoladamente mais correlacionada com a felicidade

Testando a correlação de Pearson entre `life_ladder` e todas as demais variáveis numéricas, `log_gdp_per_capita` apresenta a correlação mais forte (r = 0,785), à frente de `social_support` (0,722) e `healthy_life_expectancy_at_birth` (0,713). A regressão linear simples resultou em:

$$\text{life\_ladder} = 0{,}7634 \times \text{log\_gdp\_per\_capita} - 1{,}6832 \qquad R^2 = 0{,}616$$

Ou seja, **61,6% da variação da felicidade entre países é explicada linearmente apenas pelo PIB**. Importante ressaltar: essa correlação forte não implica causalidade — países ricos tendem a apresentar também maior suporte social, liberdade e expectativa de vida, fatores que caminham juntos e também correlacionam fortemente com a felicidade. A regressão simples usada aqui não isola esses efeitos individuais.

## 6. Conclusão

O desenvolvimento do laboratório estatístico permitiu validar, na prática, que fórmulas estatísticas implementadas manualmente reproduzem com precisão os resultados de bibliotecas consolidadas como o NumPy — reforçando a compreensão matemática por trás de cada cálculo, em vez de tratá-lo como uma "caixa-preta". A aplicação a um dataset real e relevante (felicidade global) tornou possível extrair descobertas concretas e interpretáveis, cumprindo o objetivo central da atividade.
