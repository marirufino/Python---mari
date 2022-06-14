filmes_assistidos = {"Matrix", "A viagem de Chihiro", "X"}
filme_usuario = input("Digite o filme que voce assistiu: ")

if filme_usuario in filmes_assistidos:
    print("O seu filme está na lista")
else:
    print("O seu filme não está na lista")

number = 7
user_input=input("Enter'y'if you would like to play:").lower()
if user_input == "y":
    user_number = int(input("Guess our number:"))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        #ou podemos usar abs(numer - number) == 1, onde o abs sempre dará o valor absoluto (caso seja -1, se torna 1)
        print("You were off by one.")
    else:
        print("Sorry,it's wrong!")
else:
    print("Be back when you decide to play our game! ;)")