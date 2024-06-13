import pandas as pd
import sqlite3

def aggregate_data():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('crypto_analysis.db')
    print("Conexão com o banco de dados criada com sucesso.")

    # Ler os dados da tabela 'silver' para um DataFrame pandas
    data = pd.read_sql('SELECT * FROM silver', conn)
    print("Dados lidos da tabela 'silver' com sucesso.")

    # Verificar as primeiras linhas dos dados para inspeção
    print(data.head())

    # Agrupar dados por criptomoeda e data e calcular médias
    grouped_data = data.groupby(['Criptomoeda', 'Data']).agg({
        'Abertura': 'mean',
        'Máximo': 'mean',
        'Mínimo': 'mean',
        'Fechamento': 'mean'
    }).reset_index()
    print("Dados agrupados e médias calculadas com sucesso.")

    # Calcular variação percentual
    grouped_data['Variação Diária %'] = (grouped_data['Fechamento'] - grouped_data['Abertura']) / grouped_data['Abertura'] * 100
    print("Variação percentual calculada com sucesso.")

    # Calcular volatilidade diária
    grouped_data['Volatilidade Diária %'] = (grouped_data['Máximo'] - grouped_data['Mínimo']) / grouped_data['Abertura'] * 100
    print("Volatilidade diária calculada com sucesso.")

    # Adicionar preço médio
    grouped_data['Preço Médio'] = (grouped_data['Abertura'] + grouped_data['Máximo'] + grouped_data['Mínimo'] + grouped_data['Fechamento']) / 4
    print("Preço médio calculado com sucesso.")

    # Calcular médias móveis
    grouped_data['Média Móvel de 7 Dias'] = grouped_data.groupby('Criptomoeda')['Fechamento'].rolling(window=7).mean().reset_index(0, drop=True)
    grouped_data['Média Móvel de 30 Dias'] = grouped_data.groupby('Criptomoeda')['Fechamento'].rolling(window=30).mean().reset_index(0, drop=True)
    print("Médias móveis calculadas com sucesso.")

    # Identificar dias de ganho e perda
    grouped_data['Dia de Ganho'] = grouped_data['Fechamento'] > grouped_data['Abertura']
    grouped_data['Dia de Perda'] = grouped_data['Fechamento'] < grouped_data['Abertura']
    print("Identificação de dias de ganho e perda concluída.")

    # Armazenar os dados agregados na tabela 'gold'
    grouped_data.to_sql('gold', conn, if_exists='replace', index=False)
    print("Dados agregados armazenados na tabela 'gold' com sucesso.")

    # Verificar a consistência dos dados na tabela 'gold'
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gold LIMIT 5;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fechar a conexão
    conn.close()
    print("Conexão com o banco de dados fechada com sucesso.")

if __name__ == "__main__":
    aggregate_data()
