# Strings múltiplas linhas (triple quotes)
# As strings de múltiplas linhas são criadas usando três aspas simples (''') ou três aspas duplas ("""). 
# Elas permitem que a string seja escrita em várias linhas, sem a necessidade de usar caracteres de escape para as quebras de linha. 
nome = "Pedro de Almeida Lourenço"

mensagem = f"""
Olá, meu nome é {nome}.
Estou aprendendo Python.
Esta é uma string de múltiplas linhas.
"""

print(mensagem)

# As strings de múltiplas linhas também preservam os espaços em branco e as quebras de linha, o que pode ser útil para formatar mensagens ou textos longos.
mensagem_formatada = f"""
    Olá, meu nome é {nome}.
    Estou aprendendo Python.
    Esta é uma string de múltiplas linhas.
"""
print(mensagem_formatada)

