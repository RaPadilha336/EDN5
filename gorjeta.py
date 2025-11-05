def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)

# Solicita os valores ao usuário
try:
    valor_conta = float(input("Digite o valor da conta (R$): "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))

    gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Gorjeta: R$ {gorjeta:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")

