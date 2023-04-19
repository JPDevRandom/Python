salario = float(input("Informe o salário do funcionário: "))

if salario <= 1000:
    imposto = 0
elif salario <= 2000:
    imposto = salario * 0.1
else:
    imposto = salario * 0.2

print("O valor do imposto a ser pago é R$ {:.2f}".format(imposto))