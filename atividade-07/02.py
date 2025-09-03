import csv

def escrever_csv_dict(nome_arquivo, dados, cabecalho):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # 1. Cria um DictWriter especificando os nomes das colunas (fieldnames)
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
            
            # 2. Escreve o cabeçalho
            escritor.writeheader()
            
            # 3. Escreve todas as linhas de dados de uma vez
            escritor.writerows(dados)
            
            return f"Dados salvos em {nome_arquivo} com sucesso!"
    except IOError as e: # Capturando um erro mais específico
        return f"Erro de E/S ao escrever no arquivo: {e}"

# Os dados agora são uma lista de dicionários.
cabecalho_info = ['Nome', 'Idade', 'Cidade']
dados_dict = [
    {'Nome': 'Ana', 'Idade': 18, 'Cidade': 'João Pessoa'},
    {'Nome': 'Joaquim', 'Idade': 35, 'Cidade': 'São Paulo'},
    {'Nome': 'Maicon Jebson', 'Idade': 20, 'Cidade': 'Caicó'}
]

# Bloco principal
if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo (ex: pessoas.csv): ")
    print(escrever_csv_dict(nome_do_arquivo, dados_dict, cabecalho_info))