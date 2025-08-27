def converter_temperatura():
    try:
        temp = float(input("Digite a temperatura: "))
        unidade_origem = input("Qual a unidade de origem? (C, F, K): ").upper()
        unidade_destino = input("Para qual unidade deseja converter? (C, F, K): ").upper()

        if unidade_origem == unidade_destino:
            print(f"A temperatura já está em {unidade_origem}. Valor: {temp:.2f}")
            return

        # Celsius para...
        if unidade_origem == 'C':
            if unidade_destino == 'F':
                resultado = (temp * 9/5) + 32
            elif unidade_destino == 'K':
                resultado = temp + 273.15
            else:
                print("Unidade de destino inválida.")
                return

        # Fahrenheit para...
        elif unidade_origem == 'F':
            if unidade_destino == 'C':
                resultado = (temp - 32) * 5/9
            elif unidade_destino == 'K':
                resultado = (temp - 32) * 5/9 + 273.15
            else:
                print("Unidade de destino inválida.")
                return

        # Kelvin para...
        elif unidade_origem == 'K':
            if unidade_destino == 'C':
                resultado = temp - 273.15
            elif unidade_destino == 'F':
                resultado = (temp - 273.15) * 9/5 + 32
            else:
                print("Unidade de destino inválida.")
                return
        else:
            print("Unidade de origem inválida.")
            return

        print(f"\n{temp:.2f}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}.")

    except ValueError:
        print("Erro: Por favor, insira um valor numérico para a temperatura.")

# Executa a função
converter_temperatura()