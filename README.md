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

### 2. Rodar o script em Python para coletar os dados
```bash
python coleta_dados.py
```

### 3. Rodar o script do Jupyter Notebook


## Proposta de Análise Final

#### Análisar porque as regiões apresentadas possuem tanta diferença nos preços médios e propostas para balancear os valores. 
#### Considerando os seguintes pontos:
- Estabelecimentos próximos 
- Parques próximos
- Avenidas próximas
- Qual tipo de moradia: Casa ou Apartamento
- Número de quartos da residência 
- Número de vagas de garagem 
- Quantidade de residências disponíveis


