# Projeto CIC901 – Geolocalização e Mapas Digitais 

- ### Luigi Guimarães Trevisan - 22.01102-0
- ### Vitor Moretti Negresiolo - 22.01049-0

## Tema
**Análise de preços de aluguéis residenciais na cidade de São Paulo.** 

## Fontes de dados
- https://www.kaggle.com/datasets/markfinn1/bairros-de-so-paulo/
- https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices

## Ferramentas e Tecnologias

- **Python 3.11** com bibliotecas:
  - `matplotlib`
  - `pandas`
  - `geopandas`
  - `folium`
  - `branca`
  - `requests`
- **Jupyter Notebook**

## Como Executar

### 1. Preparar o ambiente Python com as bibliotecas corretas
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Executar o script em Python para coletar os dados
```bash
python coleta_dados.py
```

### 3. Executar o script do Jupyter Notebook
```bash
jupyter notebook analise.ipynb
```

## Proposta de Análise Final

#### Esta análise terá como objetivo principal investigar os motivos que levam às discrepâncias significativas nos preços médios de imóveis entre diferentes regiões e propor estratégias para promover uma maior uniformidade nos valores praticados. Para isso, serão considerados diversos fatores que influenciam diretamente o valor dos imóveis, aplicando técnicas de análise espacial para identificar padrões relevantes.

#### Objetivos Específicos:
- Identificar os fatores que impactam os preços dos imóveis em cada região, avaliando como a presença de infraestrutura urbana, como estabelecimentos comerciais, parques, avenidas e outros serviços, contribui para a valorização ou desvalorização das residências.

- Analisar o perfil dos imóveis disponíveis, diferenciando entre casas e apartamentos, número de quartos, número de vagas de garagem e a quantidade total de unidades em oferta em cada localidade.

- Detectar padrões de agrupamento espacial com base nos preços e na localização dos imóveis utilizando o algoritmo de clustering DBSCAN (Density-Based Spatial Clustering of Applications with Noise).
