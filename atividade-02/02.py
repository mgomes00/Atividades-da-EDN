# Dados do problema
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Cálculo do desconto e preço final
valor_desconto = (preco_original * percentual_desconto) / 100
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("--- Calculadora de Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print("-" * 31)
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")