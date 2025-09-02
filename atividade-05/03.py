def calcular_preco_final(preco_original, percentual_desconto):
    if preco_original < 0 or percentual_desconto < 0:
        return (0.0, preco_original)
        
    valor_do_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_do_desconto
    return (valor_do_desconto, preco_final)

# --- Programa Principal ---
try:
    preco_str = input("Digite o preço original do produto: R$ ")
    desconto_str = input("Digite a porcentagem de desconto (ex: 20): ")

    # Substitui vírgula por ponto para aceitar ambos os formatos
    preco_original = float(preco_str.replace(',', '.'))
    percentual_desconto = float(desconto_str.replace(',', '.'))
    
    # Chama a função para obter os valores calculados
    valor_desconto, final_price = calcular_preco_final(preco_original, percentual_desconto)
    
    print("\n--- Detalhes da Compra ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
    print(f"Preço Final: R$ {final_price:.2f}")

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")