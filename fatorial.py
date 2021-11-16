def fatorial():
    n = num()
    y = 1
    i = 1
    if n == 0:
        print("O fatorial de 0 é 1.")
    while i <= n:
        y = y * i
        i += 1
    print("O fatorial de %d é %d." %(n, y))

def num():
    x = int(input("Digite um número inteiro e positivo: "))
    while x < 0:
       x = int(input("Digite um valor válida (inteiro e positivo): "))
    return x 

fatorial()