import re

def eh_palindromo(frase):
    # 1. Deixar tudo em minúsculas
    frase_lower = frase.lower()
    
    # 2. Remover tudo que não for letra ou número (espaços, pontuação, etc.)
    # A expressão regular '[^a-z0-9]' encontra qualquer caractere que NÃO seja uma letra de 'a' a 'z' ou um número de '0' a '9'
    frase_limpa = re.sub(r'[^a-z0-9]', '', frase_lower)
    
    # 3. Comparar a string limpa com a sua versão invertida
    return frase_limpa == frase_limpa[::-1]

# --- Programa Principal ---
texto_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if eh_palindromo(texto_usuario):
    print("Sim")
else:
    print("Não")

# Exemplos de palíndromos para testar:
# Ovo
# Apos a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo