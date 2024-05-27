from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.__endereco=endereco
        self.__contas=[]

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.__contas.append(conta)

class Pesssoa_fisica(Cliente):
    def __init__(self, nome, data_nascimento,cpf,endereco)
        super().__init__(endereco)
        self.__nome=nome
        self.__data_nascimento=data_nascimento
        self.__cpf=cpf

class Conta:
    def __init__(self,numero,cliente):
        self._saldo=0
        self._numero=numero
        self._agencia='0001'
        self._cliente=cliente 
        self._historico=Historico()

        @classmethod
        def nova_conta(cls, cleinte, numero):
            return cls(numero,cliente)
        
        @property
        def saldo(self):
            return self._saldo
        
        @property
        def numero(self):
            return self._numero
        
        @property
        def agencia(self):
            return self._agencia
        
        @property
        def cliente(self):
            return self._cliente
        
        @property
        def historico(self):
            return self._historico
        
        def sacar(self, valor):
            saldo=self._saldo
            excedeu_saldo=valor>saldo

            if excedeu_saldo:
                print("\n@@@ op falhou, não tem saldo suficiente @@@")

            
            elif valor>0:
                self._saldo-=valor
                print("\n=== saque realziado com sucesso!!! ===")
                return True
            
            else:
                print("\n### Operação falhou, valor inválido ###")
            
            return False
            
        def depositar(self,valor):
            if valor>0:
                self._saldo+=valor
                print("\n=== deposito realziado com sucesso ===")
                return True

            else:
                print("\n@@@ Operação falhou! o valor informado é invaĺido")
                return False
      
def Conta_corrente(Conta):
    def __init__(self,numero,cliente,limite=500,limite_saques=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques=limite_saques

    def sacar(self,valor):
        numero_saques=len(
            [trancaocao for transacao in self.historico.trancaocao if transacao["tipo"]==Saque.__name__]
        )

        excedeu_limite=valor>self.limite
        excedeu_saques=numero_saques>=self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou, o valor do saque excede o limite. @@@")
            
        elif excedeu_saques:
            print("\n@@@ Operação falhou, npumero máximo de saques excedido. @@@")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            c\c:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self._transacoes

    @property
    def transacoes(self):
        return self._transacoes[]
    
    def adicionar_transacoes(self,transacao):
        self._transacoes.append(
            "tipo": transacao.__class.__.__nome__,
            "valor":transacao.valor,
            "data":datetime.now().strftime(
                "%d-%m-%Y Ḧ:%M:%s"
            )
        )

class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor=valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao=conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Depositar(Transacao):
    def __init__(self,valor):
        self._valor=valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao=conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
