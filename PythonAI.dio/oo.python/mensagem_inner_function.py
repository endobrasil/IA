#funções chamando funções
def mensagem(nome):
    print('executando nome')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('mensagem longa')
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

#definindo funções internas
def principal():
    print('executando a função principal')

    def funcao_interna():
        print('executando a função interna')

    def funcao_2():
        print("executando a função 2")

    funcao_interna()
    funcao_2()

#função retornando função
def Calculadora(op):
    def soma(a,b):
        return a+b
    
    def subtracao(a,b):
        return a-b
    
    def divisao(a,b):
        return a/b
    
    def multiplicacao(a,b):
        return a*b

    match op:
        case "+":
            return soma
        case "-":
            return subtracao
        case "/":
            return multiplicacao
        case "*":
            return divisao

print(executar(mensagem, 'Jao'))
print(executar(mensagem_longa, 'Jao'))

principal()

print(Calculadora("+")(10,2))
print(Calculadora("*")(11,21))
print(Calculadora("-")(12,22))
print(Calculadora("/")(100,2))