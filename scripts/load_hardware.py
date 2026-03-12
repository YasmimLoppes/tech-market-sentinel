import pandas as pd
import sqlite3
from datetime import datetime

def carregar_para_sql():
    arquivo_origem = 'dados_limpos_gpus.csv'
    nome_banco = 'tech_market.db'
    
    # 1. Lendo os dados limpos
    try:
        df = pd.read_csv(arquivo_origem)
    except FileNotFoundError:
        print("❌ Arquivo limpo não encontrado. Rode o script de transformação primeiro!")
        return

    # 2. Conectando ao banco de dados (se não existir, ele cria na hora)
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    print(f"[{datetime.now()}] Carregando dados para o banco SQL...")

    # 3. Salvando os dados na tabela 'precos_gpus'
    # if_exists='append' serve para você ir acumulando o histórico cada vez que rodar!
    df.to_sql('precos_gpus', conn, if_exists='append', index=False)

    # 4. Verificação simples: qual a média de preço por marca no banco?
    print("\n--- Insight rápido do Banco de Dados ---")
    query = """
        SELECT marca, ROUND(AVG(preco_limpo), 2) as media_preco 
        FROM precos_gpus 
        GROUP BY marca
    """
    resumo = pd.read_sql(query, conn)
    print(resumo)

    conn.close()
    print(f"\n✅ Carga finalizada! Banco de dados '{nome_banco}' atualizado.")

if __name__ == "__main__":
    carregar_para_sql()