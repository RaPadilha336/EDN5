from datetime import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação sem considerar anos bissextos
    return idade_dias

# Solicita o ano de nascimento ao usuário
try:
    ano_nascimento = int(input("Digite seu ano de nascimento (ex: 1990): "))
    idade_dias = calcular_idade_em_dias(ano_nascimento)
    print(f"Você tem aproximadamente {idade_dias} dias de vida.")
except ValueError:
    print("Por favor, insira um ano válido (apenas números).")
