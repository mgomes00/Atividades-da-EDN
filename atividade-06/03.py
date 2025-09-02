import requests

def consultar_cep(cep):
    # Remove caracteres não numéricos do CEP
    cep = ''.join(filter(str.isdigit, cep))

    if len(cep) != 8:
        print("CEP inválido. O CEP deve conter 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        # ViaCEP retorna um erro no próprio JSON se o CEP não for encontrado
        if 'erro' in dados:
            print(f"Não foi possível encontrar o endereço para o CEP {cep}.")
        else:
            print("\n--- Endereço Encontrado ---")
            print(f"CEP: {dados.get('cep', 'N/A')}")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")

# --- Programa Principal ---
cep_usuario = input("Digite o CEP que deseja consultar: ")
consultar_cep(cep_usuario)