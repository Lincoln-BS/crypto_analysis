import pandas as pd
import sqlite3

def clean_data():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('crypto_analysis.db')
    print("Conexão com o banco de dados criada com sucesso.")

    # Ler os dados da tabela 'bronze' para um DataFrame pandas
    data = pd.read_sql('SELECT * FROM bronze', conn)
    print("Dados lidos da tabela 'bronze' com sucesso.")

    # Imprimir os nomes das colunas do DataFrame
    print("Colunas do DataFrame:", data.columns)

    # Renomear colunas para português
    data.rename(columns={
        'Crypto': 'Criptomoeda',
        'Date': 'Data',
        'Open': 'Abertura',
        'High': 'Máximo',
        'Low': 'Mínimo',
        'Close': 'Fechamento'
    }, inplace=True)

    # Remover valores nulos
    data.dropna(inplace=True)
    print("Valores nulos removidos com sucesso.")

    # Corrigir formatação de datas
    data['Data'] = pd.to_datetime(data['Data'])
    print("Formatação de datas corrigida com sucesso.")

    # Armazenar os dados limpos na tabela 'silver'
    data.to_sql('silver', conn, if_exists='replace', index=False)
    print("Dados limpos armazenados na tabela 'silver' com sucesso.")

    # Verificar a consistência dos dados na tabela 'silver'
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM silver LIMIT 5;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fechar a conexão
    conn.close()
    print("Conexão com o banco de dados fechada com sucesso.")

if __name__ == "__main__":
    clean_data()
