class Estudante:
    escola ="DIO"

    def __init__(self, nome, mtr):
        self.nome=nome
        self.mtr=mtr

    def __str__(self) -> str:
        return f"{self.nome} - {self.mtr} - {self.escola}"
    

    def mostrar_valores(*objs):
        for obj in objs:
            print(obj)


aluno_1=Estudante("gui",1)
aluno_2=Estudante("pgui",2)

mostrar_valores(aluno_1, aluno_2)

print(aluno_1)
print(aluno_2)