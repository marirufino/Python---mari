#podemos utilizar loops para repetir um código quantas vezes quiser (ex 100 vezes)
#ou para executar o código enquanto a condição for verdadeira


##while

number = 7
user_input = input("Whould you like to play? (Y/n)")


while user_input != "n": #se esse booleano for verdadeiro, ele vai executar o código novamente até o usuário digitar outro valor
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        #ou podemos usar abs(numer - number) == 1, onde o abs sempre dará o valor absoluto (caso seja -1, se torna 1)
        print("You were off by one.")
    else:
        print("Sorry,it's wrong!")
    

while True:
    user_input = input("Whould you like to play? (Y/n)")    
    
    if user_input == n:
        break
    
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        #ou podemos usar abs(numer - number) == 1, onde o abs sempre dará o valor absoluto (caso seja -1, se torna 1)
        print("You were off by one.")
    else:
        print("Sorry,it's wrong!")

##for

amigos = ["Mariana", "Cecília", "Clara", "Igor"]

for amigo in amigos:
    print(f"{amigos} é meu amigo(a).")

print("FIM")

for friend in range(4):
    print(f"{amigos} é meu amigo(a).")
