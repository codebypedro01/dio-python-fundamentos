# Fatiamento de string
nome = "Pedro de Almeida Lourenço"

print(nome[0])              # Retorna o primeiro caractere da string
print(nome[5])              # Retorna o sexto caractere da string
print(nome[-1])             # Retorna o último caractere da string
print(nome[0:5])            # Retorna os caracteres do índice 0 ao 4 (5 não é incluído)
print(nome[6:11])           # Retorna os caracteres do índice 6 ao 10 (11 não é incluído)
print(nome[:5])             # Retorna os caracteres do início da string até o índice 4
print(nome[6:])             # Retorna os caracteres do índice 6 até o final da string
print(nome[::2])            # Retorna os caracteres da string pulando de 2 em 2 (ou seja, retorna os caracteres nos índices 0, 2, 4, etc.)
print(nome[1::2])           # Retorna os caracteres da string pulando de 2 em 2, começando do índice 1 (ou seja, retorna os caracteres nos índices 1, 3, 5, etc.)
print(nome[::-1])           # Retorna a string invertida (ou seja, começa do final e vai até o início, pulando  de 1 em 1)
print(nome[::3])            # Retorna os caracteres da string pulando de 3 em 3 (ou seja, retorna os caracteres nos índices 0, 3, 6, etc.)
print(nome[1:10:3])         # Retorna os caracteres do índice 1 ao 9, pulando de 3 em 3 (ou seja, retorna os caracteres nos índices 1, 4, 7)    
print(nome[10:1:-1])        # Retorna os caracteres do índice 10 ao 2, invertidos (ou seja, retorna os caracteres nos índices 10, 9, 8, etc.)
print(nome[10:1:-2])        # Retorna os caracteres do índice 10 ao 2, pulando de 2 em 2 e invertidos (ou seja, retorna os caracteres nos índices 10, 8, 6, etc.)