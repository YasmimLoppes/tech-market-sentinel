-- Criação da tabela Gold para o Dashboard
CREATE TABLE IF NOT EXISTS gpus_market (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco REAL,
    marca TEXT,
    data_coleta DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Exemplo de Query para análise (O que alimenta seu gráfico)
SELECT 
    marca, 
    AVG(preco) as media_preco 
FROM gpus_market 
GROUP BY marca;