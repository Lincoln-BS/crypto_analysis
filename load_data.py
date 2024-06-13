import pandas as pd
import sqlite3

def load_data():
    # Lê o arquivo CSV usando pandas
    data = pd.read_csv('crypto_combine.csv')
    print("Dados do CSV carregados com sucesso.")

    # Renomear colunas para português
    data.rename(columns={
        'Crypto': 'Criptomoeda',
        'Date': 'Data',
        'Open': 'Abertura',
        'High': 'Máximo',
        'Low': 'Mínimo',
        'Close': 'Fechamento'
    }, inplace=True)

    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('crypto_analysis.db')
    print("Conexão com o banco de dados criada com sucesso.")

    # Carrega os dados na tabela 'bronze'
    data.to_sql('bronze', conn, if_exists='replace', index=False)
    print("Dados carregados na tabela 'bronze' com sucesso.")

    # Verifica se os dados foram carregados corretamente
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bronze LIMIT 5;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fecha a conexão
    conn.close()
    print("Conexão com o banco de dados fechada com sucesso.")

if __name__ == "__main__":
    load_data()
