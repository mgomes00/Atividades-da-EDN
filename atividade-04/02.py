notas = []
soma_das_notas = 0

print("--- Calculadora de Média da Turma ---")
print("Digite as notas dos alunos. Digite 'fim' para calcular a média.")

while True:
    entrada = input("Digite a nota do aluno: ")

    if entrada.lower() == 'fim':
        break
    
    try:
        nota = float(entrada)
        if 0 <= nota <= 10: # Validação opcional da nota
            notas.append(nota)
            soma_das_notas += nota
        else:
            print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas: # Verifica se a lista de notas não está vazia
    media = soma_das_notas / len(notas)
    print("\n--- Resultados ---")
    print(f"Total de notas inseridas: {len(notas)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota foi inserida.")