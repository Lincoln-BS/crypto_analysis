import sqlite3
import pandas as pd

def export_to_csv():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('crypto_analysis.db')
    
    # Ler os dados da tabela 'gold'
    data = pd.read_sql('SELECT * FROM gold', conn)
    
    # Exportar os dados para um arquivo CSV
    data.to_csv('gold_data.csv', index=False)
    
    # Fechar a conexão
    conn.close()
    
    print("Dados exportados para 'gold_data.csv' com sucesso.")

if __name__ == "__main__":
    export_to_csv()
