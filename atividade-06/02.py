import requests

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url)
        # Lança uma exceção se a resposta da API for um erro (ex: 404, 500)
        response.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = response.json()
        
        # Extrai as informações desejadas
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibe as informações
        print("\n--- Perfil de Usuário Aleatório Gerado ---")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

# --- Programa Principal ---
gerar_perfil_usuario()