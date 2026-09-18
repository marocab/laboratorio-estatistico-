# Laboratório Estatístico Interativo

## Identificação

- **Nome completo:** Maria Mariana Barreto Carvalho
- **RA/Matrícula:** 72650444
- **Disciplina:** Matemática e Estatística para Computação — Turma B - 0726
- **Instituição:** UniCEUB

## Descrição do projeto

Este projeto é um **Laboratório Estatístico Interativo** desenvolvido em Python, que carrega um conjunto de dados reais (World Happiness Report) e permite explorá-lo por meio de:

- Estatística descritiva (tendência central, dispersão, quartis, outliers)
- Simulação de Monte Carlo (Lei dos Grandes Números e Teorema Central do Limite)
- Distribuições teóricas (Normal, Uniforme, Exponencial)
- Correlação e regressão linear com predição interativa

O diferencial do projeto é que **todo o núcleo matemático foi implementado do zero** (arquivo `src/minhastats.py`), sem usar funções prontas de estatística de bibliotecas — cada função foi validada com testes automatizados comparando o resultado com o NumPy.

## Dataset

- **Nome:** World Happiness Report (2005–presente)
- **Fonte original:** [Kaggle — World Happiness Report, 2005-Present](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present)
- **Registros:** ~2.200 linhas (países × anos)
- **Variáveis numéricas:** Life Ladder, Log GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption, Positive affect, Negative affect, Confidence in national government
- **Variáveis categóricas:** Country name, Regional indicator, Year

## Estrutura do repositório

```
laboratorio-estatistico/
├── dados/
│   └── world_happiness.csv       # Dataset original
├── src/
│   ├── __init__.py
│   └── minhastats.py             # Núcleo estatístico implementado do zero
├── testes/
│   └── test_minhastats.py        # Testes automatizados (comparação com NumPy)
├── laboratorio.ipynb             # Aplicação interativa (Jupyter + ipywidgets)
├── app.py                        # Versão alternativa em Streamlit
├── requirements.txt
├── README.md
└── RELATORIO.md                  # Relatório completo da atividade
```

## Como instalar e executar

### 1. Pré-requisitos

- Python 3.9 ou superior

### 2. Clonar o repositório

```bash
git clone https://github.com/marocab/laboratorio-estatistico-.git
cd laboratorio-estatistico-
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

**Opção recomendada — Jupyter Notebook:**

```bash
python3 -m notebook laboratorio.ipynb
```

Isso abre o notebook no navegador. Execute as células em ordem (`Kernel → Restart Kernel and Run All Cells`) para carregar os dados e ativar os menus interativos de cada módulo.

**Opção alternativa — Streamlit:**

```bash
python3 -m streamlit run app.py
```

> Nota: durante o desenvolvimento, a interface em Streamlit apresentou problemas de renderização em algumas máquinas (tela em branco por incompatibilidade de driver gráfico/navegador). Por isso, a entrega principal do projeto foi migrada para Jupyter Notebook com `ipywidgets`, alternativa prevista no próprio enunciado da atividade.

### 5. Rodar os testes automatizados

```bash
python3 -m pytest testes/test_minhastats.py -v
```

Todas as 14 funções do núcleo estatístico são validadas contra o NumPy, com tolerância numérica de `1e-4`.

## Capturas de tela

*(Adicionar aqui prints ou GIF da aplicação em funcionamento antes da entrega final)*

## Relatório

O relatório completo da atividade — com as fórmulas utilizadas, decisões de implementação, resultados da validação e as 3 descobertas estatísticas — está em [`RELATORIO.md`](./RELATORIO.md).
