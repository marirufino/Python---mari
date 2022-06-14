name = "mariana"

saudacao = "Hello, bob"

print(saudacao) #aqui o python irá imprimir o nome de bob como foi declarado

saudacao = f"Hello, {name}" #utilizando o f o python nos permite incorporar váriaveis dentro da string 

print(saudacao)

#nesse caso a variavel não mudara dinamicamente, sendo o correto utilizar

name = "joana"

print(f"Hello, {name}")

#.format() para alterar algo dentro da string

name = "mariana"
saudacao = "Hello, {}"
with_name = saudacao.format(name)

print(with_name)


frase_longa = "Hello, {}. Today is {}."
formatado = frase_longa.format("Mariana", "Monday")
print(formatado)