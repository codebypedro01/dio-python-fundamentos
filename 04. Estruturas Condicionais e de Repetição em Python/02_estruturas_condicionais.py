# if = estrutura condicional simples
# if...else = estrutura condicional composta
# if...elif...else = estrutura condicional encadeada

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente para realizar o saque.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

else:
    print("Tipo de conta não reconhecido.")



# Operador ternário
# condição if...else em uma única linha
resultado = "Saque realizado com sucesso!" if saldo >= saque else "Saldo insuficiente para realizar o saque."
print(resultado)

# exemplo de uso do operador ternário com múltiplas condições
resultado = "Saque realizado com sucesso!" if saldo >= saque else "Saque realizado com uso do cheque especial!" if saque <= (saldo + cheque_especial) else "Saldo insuficiente para realizar o saque."
print(resultado)