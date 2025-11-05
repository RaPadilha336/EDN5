def calcular_preco_com_desconto(preco: float, desconto_percentual: float) -> float:
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

# Solicita os valores ao usuário
try:
    preco = float(input("Digite o preço original do produto (R$): "))
    desconto = float(input("Digite o percentual de desconto (%): "))

    preco_final = calcular_preco_com_desconto(preco, desconto)
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
