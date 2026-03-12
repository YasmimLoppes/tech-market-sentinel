from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import time

def extrair_kabum_direto():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    # Tira o aviso de automação
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    print(f"[{datetime.now()}] Tentando abrir o Edge nativo...")

    try:
        # Aqui não usamos o Service nem o Manager, deixamos o Selenium buscar o driver do sistema
        driver = webdriver.Edge(options=edge_options)

        url = "https://www.kabum.com.br/hardware/placa-de-video-vga"
        driver.get(url)

        print(f"[{datetime.now()}] Site aberto! Aguardando 10 segundos para carregar tudo...")
        
        # Um pequeno "sleep" manual para garantir que o JavaScript da Kabum rode
        time.sleep(10)

        # Busca os elementos pelo nome da classe (que é o padrão da Kabum)
        nomes = driver.find_elements(By.CLASS_NAME, "nameCard")
        precos = driver.find_elements(By.CLASS_NAME, "priceCard")

        lista_final = []
        for n, p in zip(nomes, precos):
            lista_final.append({
                "produto": n.text.strip(),
                "preco": p.text.strip(),
                "data_coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        df = pd.DataFrame(lista_final)
        
        if not df.empty:
            print(f"✅ FINALMENTE VENCEMOS! {len(df)} produtos encontrados.")
            print(df.head(3))
            df.to_csv("dados_brutos_gpus.csv", index=False, encoding='utf-8-sig')
            print("💾 Dados salvos em: dados_brutos_gpus.csv")
        else:
            print("⚠️ O navegador abriu, mas não encontrou os produtos. O site pode estar lento.")
        
        driver.quit()

    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        print("Dica: Verifique se o seu Edge está aberto em outra janela ou se precisa de atualização.")

if __name__ == "__main__":
    extrair_kabum_direto()