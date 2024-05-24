from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Controle_tv(Controle_remoto):
    def ligar(self):
        print("ligando tv")

    def desligar(self):
        print("desligando tv")

class Controle_ar(Controle_remoto):
    def ligar(self):
        return "ligar ar"
    
    def desligar(self):
        return "desliga ar"

controle=Controle_tv()
controle.ligar()
controle.desligar()

con=Controle_ar()
print(con.ligar())
print(con.desligar())