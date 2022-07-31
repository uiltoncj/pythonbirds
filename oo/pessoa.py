class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls}- olhos{cls.olhos}'


if __name__ == '__main__':
    renzo = Pessoa(nome="renzo")
    zezito = Pessoa(nome='zezito')
    luciano = Pessoa(renzo, zezito, nome='Luciano')
    print(luciano.nome)
    print(luciano.filhos)
    for filho in luciano.filhos:
        print(filho.nome)
    print(Pessoa.olhos)
    del luciano.filhos
    luciano.olhos = 1
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe())