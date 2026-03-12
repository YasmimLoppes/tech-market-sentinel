# 🛡️ Tech Market Sentinel: Pipeline de Engenharia de Dados

> Projeto desenvolvido como estudo prático de **Engenharia de Dados**, simulando a construção de uma arquitetura moderna para monitoramento estratégico do mercado de hardware.

---

### 🎯 Contexto do Projeto

Este projeto simula um cenário real em que a alta volatilidade de preços de componentes exige um acompanhamento automatizado. A proposta foi implementar um pipeline ponta-a-ponta para:

* **Centralizar** dados operacionais coletados via Web Scraping.
* **Automatizar** o processamento e a limpeza de dados brutos.
* **Apoiar** a tomada de decisão estratégica com visualizações analíticas.

---

### 🏗️ Arquitetura e Pipeline de Dados

O pipeline foi construído utilizando a **Metodologia Medallion**, garantindo organização e qualidade em cada etapa:

* **Camada Bronze (Ingestão):** Captura automatizada de dados crus para preservação da fonte original.
* **Camada Silver (Transformação):** Saneamento com **Pandas**, normalização de tipos e tratamento de nulos.
* **Camada Gold (Consumo):** Dados modelados e persistidos em **SQL (SQLite)** para alta performance analítica.

---

### 📊 Dashboard Analítico

Para a entrega de valor, foi desenvolvido um dashboard utilizando **Streamlit**, focado em indicadores de mercado:

<p align="center">
  <img src="dashboard_foto.png" width="95%" style="border-radius: 10px;" />
</p>

O dashboard apresenta métricas como receita média por marca, distribuição de modelos e integridade do pipeline.

---

### 🧰 Tecnologias Utilizadas

| Categoria | Tecnologia |
| :--- | :--- |
| **Linguagem** | Python 3.x |
| **Processamento** | Pandas, NumPy |
| **Banco de Dados** | SQLite3 (SQL) |
| **Visualização** | Streamlit, Plotly |
| **Versionamento** | Git & GitHub |

---

### 💡 Principais Aprendizados

Durante o desenvolvimento, foram explorados conceitos fundamentais da área:
* Construção de pipelines de dados **ETL/ELT**.
* Modelagem relacional e integridade de dados.
* Escalabilidade de scripts de automação.
* Apresentação de métricas de negócio (BI).

---

### 👩‍💻 Autora

**Yasmin Lopes**
*Estudante de ADS com foco em Engenharia de Dados.*