class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def __del__(self):
        print("removendo instancia da classe")

    def latir(self):
        print("aAwAw")

    def dormir(self):
        self.acordado=False
        print("Zzzzz...")

cao_1=Cachorro("cha","caramelo",False)
cao_2=Cachorro("Ala","branco")

cao_1.latir()

swl cao_1
print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
