import os
import time
import subprocess
import sys

def rodar_script(caminho_script):
    """Função para rodar os scripts e garantir que o Python use o ambiente correto"""
    print(f"--- Executando: {caminho_script} ---")
    resultado = subprocess.run([sys.executable, caminho_script], capture_output=False)
    return resultado.returncode

def iniciar_pipeline():
    print("🚀 [PIPELINE] Iniciando Fluxo de Engenharia de Dados...")
    
    # 1. EXTRAÇÃO (BRONZE)
    if rodar_script("scripts/extract_hardware.py") == 0:
        print("✅ [EXTRAÇÃO] Dados brutos capturados com sucesso.")
    else:
        print("❌ [ERRO] Falha na extração. Verifique o navegador.")
        return

    time.sleep(2)

    # 2. TRANSFORMAÇÃO (SILVER)
    if rodar_script("scripts/transform_hardware.py") == 0:
        print("✅ [TRANSFORMAÇÃO] Dados limpos e padronizados.")
    else:
        print("❌ [ERRO] Falha na transformação dos dados.")
        return

    time.sleep(2)

    # 3. CARGA (GOLD)
    if rodar_script("scripts/load_hardware.py") == 0:
        print("✅ [CARGA] Dados inseridos no banco SQL com sucesso.")
    else:
        print("❌ [ERRO] Falha ao carregar dados no SQLite.")
        return

    print("\n" + "="*30)
    print("🏆 PIPELINE FINALIZADO COM SUCESSO!")
    print("Agora você pode atualizar seu Dashboard Streamlit.")
    print("="*30)

if __name__ == "__main__":
    iniciar_pipeline()