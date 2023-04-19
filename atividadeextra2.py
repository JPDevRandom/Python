import random

numero_correto = random.randint (1, 100)
tentativas_restantes = 10

print("Tente adivinhar o número escolhido pelo programa (entre 1 e 100):")
while tentativas_restantes > 0:
    try:
        palpite = int(input("Digite seu palpite:"))
        print("tentativas restantes:", tentativas_restantes)
    except ValueError:
        print("Digite apenas numeros")
        continue
    if palpite == numero_correto:
        print("Acertou arrombado")
        break
    elif palpite < numero_correto:
        print("seu numero é menor que o numero correto:")
    else:
        print("seu palpite é maior que o numero correto:")
    tentativas_restantes -= 1

if tentativas_restantes == 0:
     print(f"Suas tentativas acabaram. O número correto era {numero_correto}.")