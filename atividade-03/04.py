try:
    ano = int(input("Digite um ano para verificar se é bissexto: "))

    # Verifica as condições para ser um ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Erro: Por favor, insira um ano válido (número inteiro).")