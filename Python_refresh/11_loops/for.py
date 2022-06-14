##for

amigos = ["Mariana", "Cecília", "Clara", "Igor"]

for amigo in amigos: #ele pegara a variavel amigo e percorrerá até o fim da lista
    print(f"{amigos} é meu amigo(a).")

print("FIM")

for friend in range(4): #aqui com o range criamos uma espécie de lista que será executada no número de vezes que definimos 
    print(f"{amigos} é meu amigo(a).")


grades = [10, 30, 40, 50, 60]
total = 0
amount = len(grades) #duração da lista

for grade in grades:
    total += grade

print(total / amount)


##ou podemos utilizar a função sum 

grades = [10, 30, 40, 50, 60]
total = sum(grades) #soma todos os elementos dentro da lista
amount = len(grades)

print(total/amount)


