pares = 0
impares = 0

print("--- Contador de Números Pares e Ímpares ---")
print("Digite números inteiros. Digite 0 para finalizar.")

while True:
    try:
        numero = int(input("Digite um número: "))

        if numero == 0:
            break
        
        # Verifica se é par ou ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n--- Fim da Análise ---")
print(f"Total de números PARES inseridos: {pares}")
print(f"Total de números ÍMPARES inseridos: {impares}")