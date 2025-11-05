import unicodedata

def eh_palindromo(texto: str) -> str:
    # Remove acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())

    # Verifica se é palíndromo
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Solicita entrada do usuário
entrada = input("Digite uma palavra ou frase para verificar se é palíndromo: ")
resultado = eh_palindromo(entrada)
print(f"É palíndromo? {resultado}")
