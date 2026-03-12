# 🛡️ Tech Market Sentinel: Pipeline de Engenharia de Dados

> Projeto desenvolvido como estudo prático de **Engenharia de Dados**, simulando a construção de uma arquitetura moderna para monitoramento estratégico do mercado de hardware.

---

### 🎯 Contexto e Desafio de Negócio

Este projeto simula um cenário real onde a alta volatilidade de preços de componentes exige um acompanhamento automatizado para otimização de compras. A solução foi desenhada para resolver três dores principais:
* **Fragmentação:** Dados espalhados em diversos e-commerces.
* **Inconsistência:** Preços em formatos variados e dados não estruturados.
* **Latência:** Tempo gasto na coleta manual de informações.

---

### 🏗️ Arquitetura e Pipeline de Dados

O pipeline segue a **Metodologia Medallion**, garantindo que o dado seja refinado e auditável em qualquer etapa do processo:

* **Camada Bronze (Raw):** * **O que acontece:** Extração via Web Scraping salvando os dados brutos.
    * **Propósito:** Manter a "fonte da verdade" intacta. Se houver erro no processamento futuro, podemos reprocessar tudo sem precisar de uma nova coleta.
* **Camada Silver (Trusted):** * **O que acontece:** Limpeza profunda utilizando a biblioteca **Pandas**. 
    * **Detalhes Técnicos:** Conversão de strings de moeda para float, tratamento de valores nulos (NaN) e padronização dos nomes das marcas para evitar duplicidade na análise.
* **Camada Gold (Refined):** * **O que acontece:** Modelagem dos dados transformados em banco de dados **SQLite**.
    * **Propósito:** Estruturar o dado de forma relacional para que ferramentas de BI (Streamlit/Looker) consumam informações já agregadas e performáticas.

---

### 📈 Entrega de Valor (Dashboard Analítico)

Para a visualização, utilizei o **Streamlit** integrado ao **Plotly** para fornecer indicadores que apoiam a tomada de decisão:

<p align="center">
  <img src="dashboard_foto.png" width="95%" style="border-radius: 10px;" />
</p>

* **Análise de Dispersão:** Identificação de modelos com preços fora da curva (Outliers).
* **Market Share por Marca:** Visualização da dominância de estoque entre marcas como NVIDIA e AMD.
* **Linhagem de Dados:** Monitoramento da saúde de cada camada do pipeline.

---

### 🧰 Tecnologias Utilizadas

| Categoria | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.x | Versatilidade para ETL e manipulação de dados. |
| **Processamento** | Pandas | Eficiência no tratamento de grandes volumes de dados. |
| **Banco de Dados** | SQLite3 | Banco relacional leve e portátil para o projeto. |
| **Visualização** | Streamlit | Interface rápida para prototipagem de dashboards. |
| **Versionamento** | Git & GitHub | Controle de versão e documentação técnica. |

---

### 💡 Principais Aprendizados e Evolução

O desenvolvimento deste projeto permitiu a aplicação prática de conceitos de **Engenharia de Software aplicados a Dados**:
* **Modularização:** Separação dos scripts em pastas (`scripts/`, `sql/`) para facilitar a manutenção.
* **Resiliência:** Tratamento de erros durante a extração para evitar quedas no pipeline.
* **SQL DDL:** Criação de esquemas de tabelas que garantem a integridade dos dados na Gold.

---

### 👩‍💻 Autora

**Yasmin Lopes**
*Estudante de ADS com foco em Engenharia de Dados.*