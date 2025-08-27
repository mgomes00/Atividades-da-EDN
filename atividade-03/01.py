# Solicita a idade ao usuário
idade = int(input("Digite sua idade: "))

# Classifica a idade
if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"

# Exibe o resultado
print(f"Com {idade} anos, você é classificado como: {categoria}.")