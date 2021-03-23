from Aluno import Aluno

class AluEnsinoMedio(Aluno):

    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print("___ENSIMO MÉDIO___ \nCódigo: ", self.codigo, "\nNome: ", self.nome, 
                "\nMatricula: ", self.matricula, "\nAno: ", self.ano)