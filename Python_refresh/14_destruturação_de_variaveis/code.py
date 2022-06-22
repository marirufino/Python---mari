x, y = 5, 15


frequencia_estudantes = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(frequencia_estudantes.items())) #transforma numa lista de tuplas

for student, frequencia in frequencia_estudantes.items():
    print(f"{student}: {frequencia}")

pessoas = [("Bob", 42, "Mecanico"), ("Anne", 24, "Artista"), ("Harry", 32, "Escritor")]
#ao inves de um dicionario cada pessoa tem uma tupla com tres valores

for name, age, profession in pessoas:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

for pessoa in pessoas:
    print(f"Name: {pessoa[0]}, Age: {pessoa[1]}, Profession: {pessoa[2]}")


pessoa = ("Bob", 42, "Mecanico")
name, _, profession = pessoa #utilizamos o _ quando não queremos utilizar o valor
print(name, profession)


#separar valores em duas listas

head, *tail = [1, 2, 3, 4, 5] #head *tail é a sintaxe para coletar, ela coletara todos os valores desestruturados nessa variável
#todos os valores que não correspondem a nenhum dos outros valores desestruturados

print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5] #aqui ele coletara quase todos os valores da lista, deixando apenas um para tail

print(*head)
print(tail)
