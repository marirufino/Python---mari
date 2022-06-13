name = input("Digite o seu nome: ") #a função de input sempre retorna uma string
print(name)

### utilizando input para operações matemáticas

size_input = input("How big is your house (in square feet): ")
#square_metres = size_input/10.8 #essa função retornara um erro pois não é possível fazer operações com str + int/float
square_metres = int(size_input)/10.8

print(square_metres)
print(f"{size_input} square feet is {square_metres:.2f} square metres.")