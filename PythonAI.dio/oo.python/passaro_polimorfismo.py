class Passaro:
    def voar(self):
        print("voa...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("voa nada :(")

class Aviao(Passaro):
    def voar(self):
        print("avião ta voando...")


def plano_voo(obj):
    obj.voar()

p1=Pardal()
p2=Avestruz()
p3=Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)