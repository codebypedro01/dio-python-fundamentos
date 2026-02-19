# AND = para ser True, ambas expressões devem ser True
# OR = para ser True, apenas uma das expressões deve ser True
# NOT = inverte o valor lógico da expressão

# Exemplo AND
print(True and True and True)   # True
print(True and False and True)  # False
print(False and False and False) # False

# Exemplo OR
print(True or True or True)     # True
print(True or False or True)    # True
print(False or False or False)  # False

# Exemplo NOT
print(not True)   # False
print(not False)  # True


saldo = 1000
saque = 250
limite = 200
conta_especial = True

resultado = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(resultado)

resultado_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(resultado_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

resultado_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(resultado_3)