# 🛡️ Tech Market Sentinel: Monitoramento Inteligente de Hardware

Este repositório contém um pipeline de **Engenharia de Dados** desenvolvido para automatizar a captura, o tratamento e a análise de preços de GPUs no mercado brasileiro.

---

### 🎯 Proposta do Projeto
Em um cenário de alta flutuação de preços no setor de hardware, este projeto surge para substituir a coleta manual por um fluxo automatizado. 

* **Centralização:** Dados consolidados em um único repositório.
* **Automação:** Processamento ponta-a-ponta (Scraping ao Dashboard).
* **Inteligência:** Transformação de dados brutos em métricas estratégicas.

---

### 📈 Entrega de Valor (Dashboard)
<p align="center">
  <img src="dashboard_foto.png" width="100%" alt="Dashboard Sentinel" />
</p>

---

### 🏗️ Arquitetura e Fluxo de Dados
O projeto utiliza a **Metodologia Medallion**, garantindo o refinamento do dado:

1.  **Camada Bronze (Ingestão):** Captura direta via Web Scraping (Dados Brutos).
2.  **Camada Silver (Tratamento):** Saneamento com **Pandas** (Limpeza e Tipagem).
3.  **Camada Gold (Consumo):** Modelagem em **SQLite** otimizada para análise.

---

### 🧰 Toolbox Tecnológica
* **Linguagem:** Python 🐍
* **Bibliotecas:** Pandas, Streamlit, SQLite3
* **Infraestrutura:** Git, GitHub, VS Code

---

### 💡 Evolução e Insights
O desenvolvimento permitiu a consolidação de conceitos fundamentais como:
* Implementação de fluxos **ETL/ELT**.
* Aplicação prática de **Camadas de Dados**.
* Persistência em ambientes relacionais (**SQL**).

---
**Desenvolvido por Yasmin Lopes** *Estudante de ADS com foco em Engenharia de Dados.*