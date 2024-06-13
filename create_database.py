import sqlite3

def create_database():
    # Conecta ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect('crypto_analysis.db')
    print("Conexão com o banco de dados criada com sucesso.")

    # Cria um cursor
    cursor = conn.cursor()

    # Cria a tabela 'bronze' se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bronze (
        Criptomoeda TEXT,
        Data TEXT,
        Abertura REAL,
        Máximo REAL,
        Mínimo REAL,
        Fechamento REAL
    )
    ''')
    print("Tabela 'bronze' criada ou já existe.")

    # Fecha a conexão
    conn.close()
    print("Conexão com o banco de dados fechada com sucesso.")

if __name__ == "__main__":
    create_database()
