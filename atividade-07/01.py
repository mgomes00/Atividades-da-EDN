import pandas as pd
from typing import Tuple, Optional

def calcular_estatisticas_log(nome_arquivo: str) -> Optional[Tuple[float, float]]:
    try:
        df = pd.read_csv(nome_arquivo)

        if df.empty:
            print("Erro: O arquivo CSV está vazio.")
            return None

        if 'tempo_execucao' not in df.columns:
            print(f"Erro: A coluna 'tempo_execucao' não foi encontrada em '{nome_arquivo}'.")
            return None

        tempos = pd.to_numeric(df['tempo_execucao'], errors='coerce').dropna()

        if tempos.empty:
            print("Erro: Não há dados numéricos válidos na coluna 'tempo_execucao'.")
            return None

        media = tempos.mean()
        desvio_padrao = tempos.std() # ddof=1 por padrão (amostral)
        return media, desvio_padrao

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")
        return None

# Bloco principal de execução
if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo csv: ")
    
    resultados = calcular_estatisticas_log(arquivo)
    
    if resultados:
        media_val, std_val = resultados
        print("\n--- Resultados da Análise ---")
        print(f"Média do tempo de execução: {media_val:.2f}")
        print(f"Desvio padrão do tempo de execução: {std_val:.2f}")