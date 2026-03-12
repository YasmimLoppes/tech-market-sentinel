## 🛡️ Tech Market Sentinel: Monitoramento Inteligente de Hardware

Este repositório contém um pipeline de **Engenharia de Dados** desenvolvido para automatizar a captura, o tratamento e a análise de preços de GPUs no mercado brasileiro.

### 🎯 Proposta do Projeto

Em um cenário de alta flutuação de preços no setor de hardware, este projeto surge para substituir a coleta manual por um fluxo automatizado. A solução foca em:
* **Centralização:** Consolidar dados de preços em um único repositório estruturado.
* **Automação:** Eliminar processos manuais de busca em e-commerces.
* **Inteligência:** Transformar dados brutos em métricas visuais para facilitar decisões de compra.

### 🏗️ Arquitetura e Fluxo de Dados

O projeto segue a **Metodologia Medallion**, garantindo que o dado passe por um processo de refinamento antes de chegar ao usuário final:

1. **Camada Bronze (Ingestão):** Captura direta dos dados via Web Scraping. Aqui, o dado é mantido em seu estado original para auditoria.
2. **Camada Silver (Tratamento):** Utilização da biblioteca **Pandas** para saneamento dos dados (ajuste de tipos, limpeza de caracteres especiais e remoção de duplicatas).
3. **Camada Gold (Consumo):** Armazenamento em **SQLite**, onde o dado é modelado em tabelas SQL otimizadas para leitura e BI.

### 🔌 Exploração Técnica

A fase inicial envolveu o mapeamento de seletores CSS e a lógica de navegação para garantir que a extração fosse resiliente. Durante o desenvolvimento, foquei em:
* Identificar padrões de nomenclatura de produtos.
* Validar a integridade dos preços capturados.
* Estruturar a base de dados de forma relacional.

### 📈 Entrega de Valor (Dashboard)

A camada de visualização foi construída com **Streamlit**, oferecendo uma interface limpa para análise de mercado. As principais métricas monitoradas são:
* **Média de Preços:** Comparativo entre as principais marcas.
* **Market Share:** Distribuição de modelos disponíveis no monitoramento.
* **Integridade:** Status do processamento de cada camada do pipeline.

> *Visualize o dashboard em:* `dashboard_foto.png`

### 🛠️ Toolbox Tecnológica

* **Linguagem:** Python
* **Bibliotecas:** Pandas, Streamlit, SQLite3
* **Ferramentas:** Git, VS Code

### 💡 Evolução e Insights

O desenvolvimento deste pipeline permitiu a consolidação de conceitos fundamentais para um Engenheiro de Dados:
* Implementação de fluxos de ETL/ELT.
* Aplicação de camadas de dados (Medallion).
* Persistência de dados em ambientes relacionais.
* Pensamento analítico voltado para solução de problemas de negócio.

---
**Desenvolvido por Yasmin Lopes**
*Estudante de Análise e Desenvolvimento de Sistemas com foco em Engenharia de Dados.*