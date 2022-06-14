l = ["Bob", "Rolf", "Jeff" ] #lista é mutável
t = ("Bob", "Rolf", "Jeff") #tupla é imutavel
s = {"Bob", "Rolf", "Jeff"} #um conjunto (set) não tem elementos duplicados

print(l[0])

l[0] = "Smith"

print(l)

l.append("Annie") #adicionei annie ao final da lista

print(l)

l.remove("Smith") #removi annie da lista

print(l)

s.add("Smith") #adicionei smith ao conjunto
print(s)

s.add("Smith") #smith não é adicionado pois já existe
print(s)