import json
from typing import Dict, Any, Optional

def escrever_dados_json(nome_arquivo: str, dados: Dict) -> bool:
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Erro de E/S ao escrever no arquivo: {e}")
        return False

def ler_dados_json(nome_arquivo: str) -> Optional[Dict]:
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido ou está corrompido.")
        return None

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    # Dados de exemplo
    dados_para_salvar = {
        "nome": "Mariana",
        "idade": 29,
        "cidade": "Recife",
        "ativa": True,
        "cursos": ["Python", "Ciência de Dados"]
    }
    
    arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")
    
    # --- Demonstração de Escrita ---
    print(f"\nTentando salvar os dados em '{arquivo}'...")
    sucesso_escrita = escrever_dados_json(arquivo, dados_para_salvar)
    
    if sucesso_escrita:
        print("✅ Dados salvos com sucesso!")
    else:
        print("❌ Falha ao salvar os dados.")

    # --- Demonstração de Leitura ---
    if sucesso_escrita: # Só tenta ler se a escrita deu certo
        print(f"\nLendo os dados de '{arquivo}'...")
        dados_lidos = ler_dados_json(arquivo)
        
        if dados_lidos:
            print("✅ Dados lidos com sucesso:")
            # Exibe os dados de forma mais organizada
            for chave, valor in dados_lidos.items():
                print(f"  - {chave.capitalize()}: {valor}")
        else:
            print("❌ Falha ao ler os dados.")