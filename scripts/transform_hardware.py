import pandas as pd
import os

def transformar_dados():
    arquivo_origem = 'dados_brutos_gpus.csv'
    arquivo_destino = 'dados_limpos_gpus.csv'
    
    if not os.path.exists(arquivo_origem):
        print("❌ Arquivo bruto não encontrado! Rode o extrator primeiro.")
        return

    # 1. Carrega os dados
    df = pd.read_csv(arquivo_origem)
    print(f"--- Iniciando Transformação de {len(df)} registros ---")

    # 2. Limpeza do Preço: Remove 'R$', espaços e pontos, troca vírgula por ponto
    # Exemplo: "R$ 2.599,99" -> 2599.99
    df['preco_limpo'] = df['preco'].str.replace('R$', '', regex=False)
    df['preco_limpo'] = df['preco_limpo'].str.replace('.', '', regex=False)
    df['preco_limpo'] = df['preco_limpo'].str.replace(',', '.', regex=False).str.strip()
    
    # Converte para número (float)
    df['preco_limpo'] = pd.to_numeric(df['preco_limpo'])

    # 3. Criar uma coluna simples para a Marca (opcional, mas profissional)
    df['marca'] = df['produto'].apply(lambda x: 'NVIDIA' if 'RTX' in x or 'GTX' in x else 'AMD' if 'RX' in x else 'Outra')

    # Salva o novo CSV (Camada Silver)
    df.to_csv(arquivo_destino, index=False, encoding='utf-8-sig')
    
    print("✅ Transformação concluída!")
    print(df[['produto', 'preco_limpo', 'marca']].head())
    print(f"💾 Arquivo salvo: {arquivo_destino}")

if __name__ == "__main__":
    transformar_dados()