def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# --- Programa Principal ---
try:
    conta = float(input("Digite o valor total da conta: R$ "))
    percentual = float(input("Digite a porcentagem da gorjeta desejada (ex: 15): "))

    valor_da_gorjeta = calcular_gorjeta(conta, percentual)
    valor_total_com_gorjeta = conta + valor_da_gorjeta

    print("\n--- Recibo ---")
    print(f"Valor da conta: R$ {conta:.2f}")
    print(f"Gorjeta ({percentual}%): R$ {valor_da_gorjeta:.2f}")
    print(f"Valor total a pagar: R$ {valor_total_com_gorjeta:.2f}")

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")