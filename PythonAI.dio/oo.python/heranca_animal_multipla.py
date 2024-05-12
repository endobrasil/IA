class Animal:
    def __init__(self,nro_patas):
        self.nro_patas=nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave,valor in self. __dict__.items()]}"
    
        

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo=cor_pelo
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ave(Animal):
    def __init__(self,cor_bico,**kw):
        self.cor_bico=cor_bico
        super().__init__(**kw)

class Ornitorrinco(Mamifero, Ave):
    pass


gato=Gato(cor_pelo="preto",nro_patas=4)
print(gato)

orni=Ornitorrinco(cor_pelo="amarelo",cor_bico="azul",nro_patas=6)
print(orni)