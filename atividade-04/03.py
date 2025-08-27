def verificar_senha(senha):
    # a - Verificar o comprimento
    tem_tamanho_minimo = len(senha) >= 8
    
    # b - Verificar se contém pelo menos um número
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    return tem_tamanho_minimo and tem_numero

# Programa principal
print("--- Verificador de Senha Segura ---")
print("Critérios: Mínimo de 8 caracteres e pelo menos 1 número.")
senha_usuario = input("Digite uma senha para verificar: ")

if verificar_senha(senha_usuario):
    print("✅ Senha segura! Atende aos critérios.")
else:
    print("❌ Senha insegura. Verifique os critérios e tente novamente.")