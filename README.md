# 🛡️ Tech Market Sentinel: Pipeline de Engenharia de Dados

> Projeto integrador desenvolvido como estudo prático de **Engenharia de Dados**, focado na construção de uma arquitetura ponta-a-ponta para monitoramento estratégico do mercado de hardware.

---

### 🎯 Contexto do Projeto

Este projeto simula um cenário real de negócio onde a empresa necessitava monitorar a volatilidade de preços de GPUs para otimização de estoque e compras. 
A solução desenvolvida permite:
* **Centralizar** dados provenientes de fontes externas (Web).
* **Automatizar** o processamento de dados brutos para análise rápida.
* **Garantir a qualidade** das informações através de camadas de validação.
* **Apoiar a tomada de decisão** com indicadores visuais dinâmicos.

---

### 🔌 Conexão e Exploração de Dados

O pipeline inicia com a etapa de **Data Ingestion** via Web Scraping. Diferente de bases prontas, aqui foi necessário lidar com dados não estruturados.
Nessa etapa foram realizadas:
* Mapeamento de seletores dinâmicos para captura de preços.
* Tratamento de requisições para garantir a estabilidade da coleta.
* Exploração inicial da consistência dos dados (Data Discovery).
* Definição de tipos primitivos para a primeira persistência.

---

### 🔄 Pipeline de Dados (ELT)

O pipeline segue a abordagem **ELT (Extract, Load, Transform)** e utiliza a **Arquitetura Medallion** para o refinamento:

1.  **Camada Bronze (Ingestão):** Persistência dos dados brutos em CSV. O objetivo é manter o histórico fiel da fonte para possíveis auditorias ou reprocessamentos.
2.  **Camada Silver (Trusted):** Etapa de saneamento utilizando **Pandas**. Foram implementadas lógicas de:
    * Regex para limpeza de símbolos monetários e conversão para Float.
    * Padronização de nomes de marcas e modelos (Data Cleaning).
    * Remoção de registros duplicados e tratamento de valores ausentes.
3.  **Camada Gold (Refined):** Carga dos dados limpos em banco **SQLite**. Os dados são modelados de forma relacional para garantir consultas rápidas pelo dashboard.

---

### 📈 Dashboard Analítico

Para a camada de entrega (Data Visualization), utilizei o **Streamlit** integrado ao **Plotly**. O foco foi transformar tabelas em insights de negócio:
* **Métricas KPI:** Preço médio, menor preço e variação por marca.
* **Análise de Market Share:** Distribuição de modelos disponíveis.
* **Status do Pipeline:** Visualização da integridade da última carga.

<p align="center">
  <img src="dashboard_foto.png" width="95%" />
</p>

---

### 🧰 Tecnologias Utilizadas

* **Linguagem:** Python (Scraping e ETL)
* **Manipulação:** Pandas & NumPy
* **Banco de Dados:** SQLite (SQL)
* **Visualização:** Streamlit & Plotly
* **Versionamento:** Git & GitHub

---

### 💡 Principais Aprendizados

O desenvolvimento permitiu explorar conceitos fundamentais da Engenharia de Dados:
* **Modularização de Pipelines:** Separação clara entre scripts de extração, transformação e carga.
* **Qualidade de Dados:** Implementação de regras de limpeza na camada Silver.
* **Modelagem Relacional:** Estruturação de tabelas SQL para consumo analítico.
* **Storytelling de Dados:** Foco em transformar dados técnicos em valor de negócio.

---

### 👩‍💻 Autora

**Yasmin Lopes**
*Estudante de ADS com foco em Engenharia de Dados.*