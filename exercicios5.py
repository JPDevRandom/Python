import math

def menu ():
    print("Escolha uma Forma Geometrica")
    print("1: Quadradro")
    print("2: retangulo")
    print("3: Circulo")

opcao = int(input("Opção:"))


if opcao == 1:
    raio = float(input("Digite um raio do circulo"))
    area = math.pi * raio **2
    print(f"A área do quadrado é {area:.2f}")
elif opcao == 2:
    lado = float(input("Digite o lado do quadrado: "))
    area = lado ** 2
    print(f"A área do quadrado é {area:.2f}")
elif opcao == 3:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = base * altura
    print(f"A área do retângulo é {area:.2f}")
else:
    print("Opção inválida!")


