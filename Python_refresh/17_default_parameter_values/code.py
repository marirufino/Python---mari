def add(x, y=8):
    print(x + y)


add(5)
add(x=5, y=10)


default_y = 3

def add(x, y=default_y):
    print(x + y)

add(2)

default_y = 4 #nao mudara o valor de default_y

add(2)

