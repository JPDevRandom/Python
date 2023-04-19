valor_produto = float(input("Digite o valor do produto: "))

if valor_produto > 50:
    desconto = 0.15  # 10% + 5% de desconto
else:
    desconto = 0.1  # 10% de desconto

valor_com_desconto = valor_produto * (1 - desconto)

print(f"O valor final com desconto é R$ {valor_com_desconto:.2f}")