# Projeto de Análise de Preços de Criptomoedas

## Descrição do Projeto

Este projeto consiste na criação de um pipeline de dados escalável para analisar os preços históricos de quatro criptomoedas populares: Bitcoin (BTC), Ethereum (ETH), Ripple (XRP) e Litecoin (LTC). Utilizando dados diários de preços entre 1º de janeiro de 2018 e 31 de maio de 2023, o projeto visa fornecer insights sobre tendências de mercado, volatilidade e desempenho das criptomoedas ao longo do tempo.

## Objetivo

O objetivo principal deste projeto é demonstrar habilidades em engenharia de dados, incluindo ETL (extração, transformação e carga), manipulação e agregação de dados, e visualização de dados. O projeto fornece uma visão abrangente do ciclo de vida dos dados, desde a ingestão de dados brutos até a visualização final em dashboards interativos no Power BI.

## Tecnologias Utilizadas

- **Python:** Para scripts de ETL e manipulação de dados.
- **SQL:** Para manipulação e consulta de dados.
- **Power BI:** Para visualização e criação de dashboards interativos.
- **GitHub:** Para controle de versão e documentação do projeto.
- **VS Code:** Como IDE principal.
- **SQLite:** Para armazenamento inicial dos dados.

## Como configurar o projeto
**Clone o Repositório:**
git clone https://github.com/Lincoln-BS/crypto_analysis.git
cd crypto_analysis

**Crie e Ative um Ambiente Virtual**
python -m venv venv
source venv/bin/activate # Para macOS/Linux
venv\Scripts\activate    # Para Windows

**Instale as Dependências:**
pip install -r requirements.txt

**Crie o Banco de Dados**
python create_database.py

**Carregue os Dados no Banco de Dados**
python load_data.py

**Limpe e Transforme os Dados**
python clean_data.py

**Agregue os Dados**
python aggregate_data.py
 
**Exporte os Dados para CSV**
python export_to_csv.py

