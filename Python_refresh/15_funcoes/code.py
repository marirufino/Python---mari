def hello():
    print("Hello!")

hello() # Hello!




def user_age_in_seconds():
    user_age = int(input("Qual a sua idade? "))
    user_age_in_seconds = user_age * 365 * 24 * 60 * 60
    print("Você tem {} segundos de vida.".format(user_age_in_seconds))

print("Seja bem vindo ao programa idade em segundos!")

user_age_in_seconds()

print("Fim do programa!")

 