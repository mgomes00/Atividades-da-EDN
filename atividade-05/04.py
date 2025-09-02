from datetime import datetime

def calcular_dias_de_vida(data_nascimento_str):
    try:
        # Converte a string da data de nascimento em um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
        
        # Pega a data e hora atuais
        data_hoje = datetime.now()
        
        # Calcula a diferença entre as duas datas
        diferenca = data_hoje - data_nascimento
        
        # Retorna apenas o número de dias da diferença
        return diferenca.days
    except ValueError:
        # Retorna None se a data inserida não estiver no formato correto
        return None

# --- Programa Principal ---
nascimento_input = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")

dias_vividos = calcular_dias_de_vida(nascimento_input)

if dias_vividos is not None:
    if dias_vividos >= 0:
        print(f"\nAté o dia de hoje, você viveu {dias_vividos} dias.")
    else:
        print("A data de nascimento inserida é no futuro. Por favor, insira uma data passada.")
else:
    print("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")