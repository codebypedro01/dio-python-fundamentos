# for = estrutura de repetição que permite iterar sobre elementos de uma sequência (como listas, tuplas, strings, etc.)

# Exemplo de uso do for com uma lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Exemplo de uso do for com uma string
palavra = "Python"
for letra in palavra:
    print(letra)

# Exemplo de uso do for com range()
for i in range(5):
    print(i)

# Exemplo de uso do for com range() e passo
for i in range(0, 10, 2):
    print(i)
    
# Exemplo de uso do for com range() e passo negativo
for i in range(10, 0, -2):
    print(i)    
    
# while = estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira

# Exemplo de uso do while
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador para evitar loop infinito
    
# Exemplo de uso do while com uma condição de parada
senha_correta = "1234"
senha_usuario = ""
while senha_usuario != senha_correta:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == senha_correta:
        print("Acesso concedido!")
    else:
        print("Senha incorreta. Tente novamente.")
        
# Exemplo de uso do while com uma condição de parada e contagem de tentativas
senha_correta = "1234"
senha_usuario = ""
tentativas = 0
while senha_usuario != senha_correta and tentativas < 3:
    senha_usuario = input("Digite a senha: ")
    tentativas += 1
    if senha_usuario == senha_correta:
        print("Acesso concedido!")
    else:
        print("Senha incorreta. Tente novamente.")
if tentativas == 3:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")

# Exemplo de uso do while com uma condição de parada e contagem de tentativas usando operador ternário
senha_correta = "1234"
senha_usuario = ""
tentativas = 0
while senha_usuario != senha_correta and tentativas < 3:
    senha_usuario = input("Digite a senha: ")
    tentativas += 1
    resultado = "Acesso concedido!" if senha_usuario == senha_correta else "Senha incorreta. Tente novamente."
    print(resultado)
if tentativas == 3:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")    
    
    
# while True = estrutura de repetição que executa um bloco de código indefinidamente, até que uma condição de parada seja atingida (geralmente usando break)    
while True:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == "1234":
        print("Acesso concedido!")
        break  # Encerra o loop quando a senha correta é digitada
    else:
        print("Senha incorreta. Tente novamente.")

# Exemplo de uso do while True com uma condição de parada usando operador ternário
while True:
    senha_usuario = input("Digite a senha: ")
    resultado = "Acesso concedido!" if senha_usuario == "1234" else "Senha incorreta. Tente novamente."
    print(resultado)
    if senha_usuario == "1234":
        break  # Encerra o loop quando a senha correta é digitada   

# Exemplo de uso do while True com uma condição de parada usando operador ternário e contagem de tentativas
tentativas = 0
while True:
    senha_usuario = input("Digite a senha: ")
    resultado = "Acesso concedido!" if senha_usuario == "1234" else "Senha incorreta. Tente novamente."
    print(resultado)
    if senha_usuario == "1234":
        break  # Encerra o loop quando a senha correta é digitada
    tentativas += 1
    if tentativas == 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break  # Encerra o loop quando o número máximo de tentativas é atingido

    