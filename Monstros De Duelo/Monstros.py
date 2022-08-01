"""from abc import ABC, abstractmethod

class Monstros(ABC):

    def monstros(self, nome: str, tipo: str, ataque: float, defesa: float):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa

        pass

    # estudar abstrações em python depois
"""

class Cavaleiro():

    def __init__(self, nome: str, tipo: str, ataque: float, defesa: float):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa

        self.ativar_efeito_cavaleiro()

    def efeito_cavaleiro(self):
        efeito = "Cavaleiros ganham 32% do seu ataque em defesa"

        return efeito

    def ativar_efeito_cavaleiro(self):

        efeito = float(self.defesa) + (float(self.ataque * 0.32))
        ganho_efeito = (float(self.ataque * 0.32))
        self.defesa = efeito

        return ganho_efeito


class Dragao():

    def __init__(self, nome: str, tipo: str, ataque: float, defesa: float):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa

        self.ativar_efeito_dragao()

    def efeito_dragao(self):
        efeito = "Dragões ganham mais 15% do valor do seu ataque em ataque"

        return efeito

    def ativar_efeito_dragao(self):

        efeito = float(self.ataque) + (float(self.ataque * 0.15))
        ganho_efeito = (float(self.ataque * 0.15))

        self.ataque = efeito

        return ganho_efeito


class Mago():

    def __init__(self, nome: str, tipo: str, ataque: float, defesa: float):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa

        self.ativar_efeito_mago()


    def efeito_mago(self):

        efeito = "Magos ganham 63% a mais de seu ataque, porem perdem 26% de defesa"

        return efeito

    def ativar_efeito_mago(self):

        efeito = float(self.ataque) + float(self.ataque * 0.63)
        efeito_2 = float(self.defesa) - float(self.defesa * 0.26)
        ganho_efeito = float(self.ataque * 0.63)
        ganho_efeito_text = "Ganhou {value:.2f} de ataque"
        self.ataque = efeito
        self.defesa = efeito_2

        return ganho_efeito_text.format(value = ganho_efeito)


magos = []

magoNegro = Mago(nome = 'Mago Negro', tipo = 'mago', ataque = 2500, defesa = 2200)
magaNegra = Mago(nome = 'Maga Negra', tipo = 'mago', ataque = 2400, defesa = 2100)

magos.append(magoNegro)
magos.append(magaNegra)

for range in magos:
    print(range.nome)
    print(range.tipo)
    print(range.ataque)
    print(range.defesa)
    print(range.efeito_mago())