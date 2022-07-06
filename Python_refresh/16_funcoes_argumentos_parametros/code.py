def add(x, y): #possui dois parametros
    result = x + y
    print(result)

add(4, 5) #argumentos


def say_hello(name, sobrenome):
    print(f"Hello! {name} {sobrenome}")

nome = input("Qual o seu nome? ")
sobrenome = input("Qual o seu sobrenome? ")

say_hello(nome, sobrenome) #argumento posicional 

say_hello(name="Rufino", sobrenome="Mariana")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("Divisor não pode ser zero!")

divide(15, 5)

