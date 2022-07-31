class Pessoa:
    def __init__(self, nome = None, idade=35 ):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(p.nome)
