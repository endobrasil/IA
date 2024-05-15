class Conta:
    def __init__(self, nro_agencia,saldo=0):
        self._saldo=saldo
        self.nro_agencia=nro_agencia

    def depositar(self,valor):
        self._saldo+valor

    def sacar(self,valor):
        self._saldo-valor

conta=Conta(1,100)
print(f"ag: {conta.nro_agencia} saldo: {conta._saldo}")
conta._saldo=1000000
print(conta._saldo)
