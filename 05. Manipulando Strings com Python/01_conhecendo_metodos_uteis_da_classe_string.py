nome = "gUiLHeRMe"


print(nome.upper())             # Deixa todas as letras maiúsculas 
print(nome.lower())             # Deixa todas as letras minúsculas
print(nome.capitalize())        # Deixa a primeira letra maiúscula e o restante minúscula
print(nome.title())             # Deixa a primeira letra de cada palavra maiúscula e o restante minúscula
print(nome.strip())             # Remove os espaços em branco no início e no final da string
print(nome.lstrip())            # Remove os espaços em branco no início da string
print(nome.rstrip())            # Remove os espaços em branco no final da string
print(nome.replace("e", "3"))   # Substitui todas as ocorrências de "e" por "3"
print(nome.ljust(20, "*"))      # Alinha a string à esquerda em um campo de largura 20, preenchendo com "*"
print(nome.rjust(20, "*"))      # Alinha a string à direita em um campo de largura 20, preenchendo com "*"
print(nome.center(20, "*"))     # Centraliza a string em um campo de largura 20, preenchendo com "*"
print(nome.split())             # Divide a string em uma lista de palavras
print(nome.split("l"))          # Divide a string em uma lista de palavras usando "l" como separador
print(nome.find("e"))           # Retorna o índice da primeira ocorrência de "e" na string
print(nome.find("x"))           # Retorna -1 se "x" não for encontrado na string
print(nome.count("e"))          # Conta o número de ocorrências de "e" na string
print(nome.startswith("g"))     # Verifica se a string começa com "g"
print(nome.endswith("e"))       # Verifica se a string termina com "e"
print(nome.isalpha())           # Verifica se a string contém apenas letras
print(nome.isdigit())           # Verifica se a string contém apenas dígitos
print(nome.isalnum())           # Verifica se a string contém apenas letras e dígitos    