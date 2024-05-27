def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero*2

for i in meu_gerador(numeros=[1,3,5,7,9]):
    print(i)
