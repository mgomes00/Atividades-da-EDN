# Funções para as operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

# Loop principal da calculadora
while True:
    print("\n--- Calculadora Digital ---")
    print("Escolha a operação:")
    print("1: Somar")
    print("2: Subtrair")
    print("3: Multiplicar")
    print("4: Dividir")
    print("0: Sair")

    escolha = input("Digite o número da sua opção: ")

    if escolha == '0':
        print("Encerrando a calculadora...")
        break
    
    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")
    else:
        print("Opção inválida! Por favor, escolha uma opção de 0 a 4.")