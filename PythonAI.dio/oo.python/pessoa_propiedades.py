class Pessoa:
    def __init__(self, nome, ano_nasmcimento):
       
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atuel=2022
        return _ano_atuel- self._ano_nascimento


pessoa = Pessoa("andre", 1985)
print(f"nome {pessoa.nome} \tIdade: {pessoa.idade}")