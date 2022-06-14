amigos = {"Cecilia", "Clara", "Igor"}
viajando = {"Cecilia", "Clara"}

local_friends = amigos.difference(viajando) #calcula a diferença entre os dois conjuntos
print(local_friends)

local = {"Igor"}
viajando = {"Cecilia", "Clara"}
friends = local.union(viajando) #une os conjuntos

print(friends)


art = {"Cecilia", "Clara", "Igor"}
science = {"Cecilia", "Clara", "Pedro"}

ambos = art.intersection(science) #interseção dos conjuntos
print(ambos)

#para declarar uma tupla vazia utilizamos a virgula apos o valor
#ex: tupla = (15,), pois assim o python entende que se trata de uma tabela



