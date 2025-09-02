import requests
from datetime import datetime

def consultar_cotacao(codigo_moeda):
    # Formata o código da moeda para o padrão da API (ex: USD-BRL)
    moeda_par = f"{codigo_moeda.upper()}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_par}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        dados = response.json()
        
        # A chave do dicionário é o código sem o hífen (ex: USDBRL)
        chave_api = moeda_par.replace('-', '')
        
        if chave_api not in dados:
            print(f"Moeda '{codigo_moeda.upper()}' não encontrada. Tente USD, EUR, GBP, etc.")
            return

        info_moeda = dados[chave_api]

        # Converte o timestamp para um formato de data e hora legível
        timestamp = int(info_moeda['timestamp'])
        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print(f"\n--- Cotação de {info_moeda['name']} ---")
        print(f"Última atualização: {data_atualizacao}")
        print(f"Valor Atual (Compra): R$ {float(info_moeda['bid']):.4f}")
        print(f"Máxima do Dia: R$ {float(info_moeda['high']):.4f}")
        print(f"Mínima do Dia: R$ {float(info_moeda['low']):.4f}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Código de moeda '{codigo_moeda.upper()}' inválido ou não encontrado na API.")
        else:
            print(f"Erro HTTP ao consultar a API: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao consultar a API: {e}")

# --- Programa Principal ---
moeda = input("Digite o código da moeda para consultar (ex: USD, EUR, BTC): ")
consultar_cotacao(moeda)