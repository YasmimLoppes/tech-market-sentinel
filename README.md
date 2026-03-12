# 🛡️ Tech Market Sentinel
> **Pipeline de Engenharia de Dados para Monitoramento de Mercado**

<p align="center">
  <img src="https://img.shields.io/badge/Status-Functional-31c854?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Medallion-blue?style=for-the-badge" />
</p>

---

### 🖼️ Preview do Dashboard
<p align="center">
  <img src="dashboard_print.png" width="100%" />
</p>

### 🏗️ Arquitetura do Fluxo (Medallion)

```mermaid
graph TD
    A[🛒 Extração: Selenium] --> B{Camada Bronze}
    B --> C[⚙️ Processamento: Pandas]
    C --> D{Camada Silver}
    D --> E[🗄️ Persistência: SQL]
    E --> F{Camada Gold}
    F --> G[📊 Dashboard: Streamlit]

    style B fill:#CD7F32,stroke:#333,color:#fff
    style D fill:#C0C0C0,stroke:#333,color:#000
    style F fill:#FFD700,stroke:#333,color:#000