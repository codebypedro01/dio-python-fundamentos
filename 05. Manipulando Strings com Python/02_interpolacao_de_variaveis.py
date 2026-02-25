# Tipos de interpolação de variáveis em strings
nome = "Guilherme"
sobrenome = "Silva"
idade = 30

# Interpolação usando o operador %
print("Meu nome é %s %s e tenho %d anos." % (nome, sobrenome, idade))                       # %s para strings, %d para inteiros, %f para floats
print("Meu nome é %s %s e tenho %.2f anos." % (nome, sobrenome, idade))                     # %.2f para formatar o número com 2 casas decimais
print("Meu nome é %s %s e tenho %d anos." % (nome.upper(), sobrenome.lower(), idade + 5))   # Usando expressões dentro da interpolação    

# Interpolação usando o método format()
print("Meu nome é {} {} e tenho {} anos.".format(nome, sobrenome, idade))
print("Meu nome é {0} {1} e tenho {2} anos.".format(nome, sobrenome, idade))                                        # Usando índices para referenciar as variáveis
print("Meu nome é {nome} {sobrenome} e tenho {idade} anos.".format(nome=nome, sobrenome=sobrenome, idade=idade))    # Usando nomes para referenciar as variáveis
print("Meu nome é {0} {sobrenome} e tenho {idade} anos.".format(nome, sobrenome=sobrenome, idade=idade))            # Usando índices e nomes para referenciar as variáveis

# Interpolação usando f-strings (Python 3.6+)
print(f"Meu nome é {nome} {sobrenome} e tenho {idade} anos.")                       # Dentro das chaves, podemos usar expressões, métodos e formatações
print(f"Meu nome é {nome.upper()} {sobrenome.lower()} e tenho {idade + 5} anos.")   # Usando expressões e métodos dentro das chaves
print(f"Meu nome é {nome:>20} {sobrenome:<20} e tenho {idade:^10} anos.")           # Usando formatações para alinhar o texto: > para direita, < para esquerda, ^ para centralizado, seguido do número de caracteres
print(f"Meu nome é {nome:.3} {sobrenome:.3} e tenho {idade:.2f} anos.")             # Usando formatações para limitar o número de caracteres: .3 para strings limita a 3 caracteres, .2f para floats limita a 2 casas decimais
