import pandas as pd
import sqlite3

def verify_data():
    # Conectar ao banco de dados
    conn = sqlite3.connect('crypto_analysis.db')
    
    # Ler os dados da tabela 'gold'
    data_gold = pd.read_sql('SELECT * FROM gold', conn)
    
    # Exibir as primeiras linhas do DataFrame
    print("Primeiras linhas dos dados agregados (Tabela 'gold'):")
    print(data_gold.head())
    
    # Estatísticas descritivas dos dados
    print("\nEstatísticas descritivas dos dados agregados:")
    print(data_gold.describe())
    
    # Verificar se há valores nulos
    null_values = data_gold.isnull().sum()
    print("\nValores nulos por coluna:")
    print(null_values)
    
    # Fechar a conexão com o banco de dados
    conn.close()

if __name__ == "__main__":
    verify_data()
