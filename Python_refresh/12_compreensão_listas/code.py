numeros = [1, 3, 5]
doubled = [x * 2 for x in numeros] #operação com compreensao

for num in numeros:
    doubled.append(num * 2) #operação normal




amigos = ["Rolf", "Sam", "Samantha", "Sarah", "Jen"]
comeca_com_s = []

for amigo in amigos:
    if amigo.startswith("S"):
        comeca_com_s.append(amigo) #operação normal

print(comeca_com_s)


amigos = ["Rolf", "Sam", "Samantha", "Sarah", "Jen"]
comeca_com_s = [amigo for amigo in amigos if amigo.startswith("S")]

print(comeca_com_s)


print( "Friends: ", id(amigos), "começa_com_s: ", id(comeca_com_s))
#id mostra a identidade do objeto, seu espaço de memoria
