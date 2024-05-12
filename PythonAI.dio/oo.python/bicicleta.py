"""João tem uma bicicletaria e gostaria de registrar as vendas
 de suas bicicletas. Crie um programa onde João 
 informe: cor, modelo, ano e valor da bicicleta vendida. 
 Uma bicicleta pode: buzinar, para e correr.
 Adicione estes comportamentos! """

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
        self.aro=aro

    def buzinar(self):
        return "FiuFiu"
    
    def parar(self):
        return "tapiula"
    
    def correr(self):
        return "sai do mei"
    
    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, ano={self.ano}, modelo={self.modelo}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave,valor in self. __dict__.items()]}"
    



quadro_bola=Bicicleta("vermelha","quadro bola", 1987,450)
fininha=Bicicleta("preta","speed",2023,1600,29)
print(quadro_bola.buzinar())
print(quadro_bola.parar())
print(quadro_bola.correr())

print (quadro_bola.cor, quadro_bola.modelo,quadro_bola.valor)
print(fininha.ano,fininha.cor, fininha.modelo,fininha.valor)

print(quadro_bola)
print(fininha)