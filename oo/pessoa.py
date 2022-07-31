class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    renzo = Pessoa(nome="renzo")
    zezito = Pessoa(nome='zezito')
    luciano = Pessoa(renzo, zezito, nome='Luciano')
    print(luciano.nome)
    print(luciano.filhos)
    for filho in luciano.filhos:
        print(filho.nome)
