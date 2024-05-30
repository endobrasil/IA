"""Desafio
Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

Entrada
Nome do usuário, número de telefone e plano.

Saída
Mensagem indicando que o usuário foi criado com sucesso.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Ana
(11) 91111-1111             Usuário Ana criado com sucesso.
Plano Essencial Fibra

Sofia
(22) 92222-2222             Usuário Sofia criado com sucesso.
Plano Prata Fibra	


Pedro
(33) 93333-3333             Usuário Pedro criado com sucesso.
Plano Premium Fibra




# TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.


        
    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
      

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome=nome
        self._numero=numero
        self._plano=plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero(self):
        return self._numero
    
    @property
    def plano(self):
        return self._plano


    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = "andre input()  "
numero = "85 input()"  
plano = "plano input() " 
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome,numero,plano)
print(usuario)
"""

"""
Desafio II
Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser 
verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe 
PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. 
Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada'
 para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

Entrada
Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

Saída
Mensagem personalizada de acordo o saldo do cliente.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas 
respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
João                Seu saldo está baixo. Recarregue e use os serviços do seu plano.
Essencial      
9


Debora
Prata                	Seu saldo está razoável. Aproveite o uso moderado do seu plano.
11

Catarina
Premium                 Parabéns! Continue aproveitando seu plano sem preocupações.
50



# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self,nome,saldo=0):
        self._nome=nome
        self._saldo=saldo

    @property
    def nome(self):
        return self._nome
    
    @property
    def saldo(self):
        return self._saldo

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
    def verificar_saldo(self):
        if self._saldo>=50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        elif self._saldo<10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:
    def mensagem_personalizada(self):
        return self.verificar_saldo()
    

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def saldo(self):
        return self.plano.verificar_saldo()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
#saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
#print(mensagem_usuario)
print(usuario.saldo())

"""


"""
Desafio III
Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, 
que realizar chamadas para outros usuários. Cada chamada terá uma duração 
em minutos e o custo será deduzido do saldo do usuário, suponha o custo de
 $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir 
 que o usuário faça a chamada, ele vai receber o destinatario e duracao como 
 parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto
   'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo
     do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

Entrada
Número do usuário, número do telefone, saldo inicial, número do destinatário e a 
duração da chamada em minutos.

Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas 
respectivas saídas esperadas. Certifique-se de testar seu programa com esses 
exemplos e com outros casos possíveis.

Entrada	Saída
Rodrigo
(00) 90000-0000
10.00
(33) 93333-3333
60

Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00

Yule
(11) 91111-1111
30.00
(00) 90000-0000
240	Chamada para (00) 90000-0000 realizada com sucesso. Saldo: $6.00

Amelia
(33) 93333-3333
10.00
(11) 91111-1111
120
"""

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self,destino,duracao):
        
        

# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo=self.plano.custo_chamada(duracao)

# TODO: Verifique se o saldo do plano é suficiente para a chamada.
        saldo_suficiente= custo<=self.plano.verificar_saldo()

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
        if saldo_suficiente:
            self.plano.deduzir_saldo(duracao)
            return f"Chamada para {destino.numero} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self,minuto):
        return minuto*0.1


# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self,minuto):
        self.saldo-=self.custo_chamada(minuto)


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = UsuarioPrePago(nome, numero, saldo_inicial)
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))