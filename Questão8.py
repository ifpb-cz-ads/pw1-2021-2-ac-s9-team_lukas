
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def populacaoEstado(self):
        populacao = 0
        for cidade in self.cidades:
            populacao += cidade.populacao
        return populacao

sousa = Cidade("Sousa", 50000)
cajazeiras = Cidade("Cajazeiras", 80000)
paraiba = Estado("Paraíba", "PB", [sousa, cajazeiras])

juazeiro = Cidade("Juazeiro do Norte", 500000)
fortaleza = Cidade("Fortaleza", 1000000)
ceara = Estado("Ceará", "CE", [juazeiro, fortaleza])

rio = Cidade("Rio de Janeiro", 7000000)
belford = Cidade("Belford Roxo", 500000)
rj= Estado("Rio de Janeiro", "RJ", [rio, belford])

