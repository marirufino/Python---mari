idades_amigos = {"Rolf": 24, "Adam": 30, "Anne": 27}
idades_amigos["Adam"]

idades_amigos["Bob"] = 20
idades_amigos["Rolf"] = 30


print(idades_amigos["Adam"])
print(idades_amigos)


friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 34},
    {"name": "Anne", "age": 44},
]

print(friends)

print(friends[1])
print(friends[1]["name"])


frequencia_estudantes = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in frequencia_estudantes:
    print(student) #aqui conseguimos imprimir a chave do dicionario
    print(f"{student}: {frequencia_estudantes[student]}")


for student, frequencia in frequencia_estudantes.items():
    print(f"{student}: {frequencia}") #melhor maneira de fazer


frequencia_valores = frequencia_estudantes.values()
print(sum(frequencia_valores)/ len(frequencia_valores)) #pegando a média

