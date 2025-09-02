import random
import string

def gerar_senha_segura(tamanho):
    # O tamanho mínimo agora é 4, pois precisamos garantir 4 tipos de caracteres.
    if tamanho < 4:
        return None

    # 1. Define os conjuntos de caracteres SEPARADAMENTE
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # 2. Garante pelo menos um caractere de CADA um dos 4 conjuntos
    senha_parcial = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Junta todos os caracteres para preencher o resto da senha
    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos
    
    # 3. Preenche o restante da senha (tamanho - 4, pois já temos 4)
    for _ in range(tamanho - 4):
        senha_parcial.append(random.choice(todos_caracteres))

    # Embaralha a lista para garantir que a ordem seja aleatória
    random.shuffle(senha_parcial)

    # Une a lista em uma string final
    return "".join(senha_parcial)

# Bloco principal de execução
if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")
    try:
        tamanho_desejado = int(input("Digite o tamanho da senha desejada (mínimo 4): "))
        
        senha = gerar_senha_segura(tamanho_desejado)
        
        if senha:
            print(f"\n✅ Senha gerada com sucesso: {senha}")
        else:
            # CORREÇÃO: A mensagem de erro agora corresponde ao mínimo de 4.
            print("\n❌ Tamanho inválido. A senha deve ter no mínimo 4 caracteres.")
            
    except ValueError:
        print("\n❌ Erro: Entrada inválida. Por favor, digite um número inteiro.")