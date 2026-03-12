import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Tech Market Sentinel", layout="wide")

st.title("🛡️ Tech Market Sentinel")
st.subheader("Monitoramento de Preços de GPUs em Tempo Real")

# Conexão com o banco que você criou
def carregar_dados():
    conn = sqlite3.connect('tech_market.db')
    query = "SELECT * FROM precos_gpus"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = carregar_dados()

# --- KPI's (Destaques) ---
col1, col2, col3 = st.columns(3)
col1.metric("Total de Placas", len(df))
col2.metric("Média de Preço (Geral)", f"R$ {df['preco_limpo'].mean():.2f}")
col3.metric("Placa mais Barata", f"R$ {df['preco_limpo'].min():.2f}")

st.divider()

# --- Gráficos ---
c1, c2 = st.columns(2)

with c1:
    st.write("### Média de Preço por Marca")
    fig_barra = px.bar(df.groupby('marca')['preco_limpo'].mean().reset_index(), 
                       x='marca', y='preco_limpo', color='marca',
                       labels={'preco_limpo': 'Preço Médio (R$)'},
                       color_discrete_map={'NVIDIA': '#76b900', 'AMD': '#ed1c24'})
    st.plotly_chart(fig_barra, use_container_width=True)

with c2:
    st.write("### Distribuição de Marcas no Mercado")
    fig_pizza = px.pie(df, names='marca', color='marca',
                       color_discrete_map={'NVIDIA': '#76b900', 'AMD': '#ed1c24'})
    st.plotly_chart(fig_pizza, use_container_width=True)

# --- Tabela de Dados ---
st.write("### Dados Brutos Analisados")
st.dataframe(df.sort_values(by='preco_limpo'), use_container_width=True)