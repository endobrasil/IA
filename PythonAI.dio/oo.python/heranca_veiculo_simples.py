class Veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor=cor
        self.placa = placa
        self.numero_rodas=numero_rodas

    def ligar_motor(self):
        return "TanaNnaNnaNnaNnaN"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave,valor in self. __dict__.items()]}"
       

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor,placa,numero_rodas)
        self.carregado=carregado

    def esta_carregado(self):
        
        return f"{'Sim' if self.carregado else 'Não'} estou carregado"

    


moto = Motocicleta("verde lodo","oin3456",2)
carro = Carro("azul","oiu78965",4)
caminhao=Caminhao("lilaz",'oiyt67',16)

print("moto "+moto.ligar_motor())
print("carro "+carro.ligar_motor())
print("caminhao "+caminhao.ligar_motor())
print(moto)
print(carro)
print(caminhao)
print(caminhao.esta_carregado())
caminhao.esta_carregado=True
print(caminhao.esta_carregado())
