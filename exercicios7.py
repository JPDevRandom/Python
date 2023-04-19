print("Bem-vindo ao sistema de consulta de aposentadoria")

total_consultas = 0

while True:
    print(f"Esta é a consulta número {total_consultas + 1}")

    nome = input("Digite o seu nome: ")
    sexo = input("Digite o seu sexo (M ou F): ")
    idade = int(input("Digite a sua idade: "))
    tempo_contribuicao = int(input("Digite o tempo de contribuição em anos: "))

    if (sexo.upper() == "F" and idade >= 55 and tempo_contribuicao >= 30) or (sexo.upper() == "M" and idade >= 60 and tempo_contribuicao >= 35):
        print(f"{nome} pode requerer a aposentadoria.")
    else:
        print(f"{nome} não pode requerer a aposentadoria.")

    total_consultas += 1

    opcao = input("Deseja fazer outra consulta? (S/N) ")

    if opcao.upper() == "N":
        break