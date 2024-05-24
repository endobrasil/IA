class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    @classmethod
    def criar_apartir_nascimento(cls, ano, mes, dia, nome):
        idade=2024-ano
        return cls(nome,idade)
    @staticmethod
    def e_maior(idade):
        return idade>=18
    


p=Pessoa("jao",38)
print(p.nome, p.idade)

p2=Pessoa.criar_apartir_nascimento(1985,3,21,"Andre")

print(p2.nome, p2.idade)

print(Pessoa.e_maior(18))
print(Pessoa.e_maior(8))