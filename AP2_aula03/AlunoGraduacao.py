from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        print("___GRADUAÇÃO___ \nCódigo: ", self.codigo, "\nNome: ", self.nome, 
                "\nMatricula: ", self.matricula, "\nSemestre: ", self.semestre)