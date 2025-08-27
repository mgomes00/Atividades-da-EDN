# Solicita peso e altura ao usuário
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Determina a classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe o resultado
print("\n--- Resultado do IMC ---")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")