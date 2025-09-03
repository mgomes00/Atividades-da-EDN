import csv
from typing import List, Dict, Optional
from tabulate import tabulate

def ler_csv_para_dict(nome_arquivo: str) -> Optional[List[Dict]]:
    dados = []
    try:
        # Abre o arquivo em modo de leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            # DictReader usa a primeira linha como as chaves dos dicionários
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    # Pede ao usuário o nome do arquivo
    arquivo = input("Digite o nome do arquivo CSV para ler: ")
    
    # Chama a função para ler os dados do arquivo
    lista_de_pessoas = ler_csv_para_dict(arquivo)
    
    # Verifica se a função retornou dados com sucesso
    if lista_de_pessoas:
        print("\n--- Dados Encontrados ---")
        
        # Usa a função tabulate para criar e imprimir a tabela
        # - O primeiro argumento é a lista de dicionários (os dados).
        # - headers="keys" diz para usar as chaves do dicionário como cabeçalho.
        # - tablefmt="grid" define o estilo da tabela com bordas.
        print(tabulate(lista_de_pessoas, headers="keys", tablefmt="grid"))