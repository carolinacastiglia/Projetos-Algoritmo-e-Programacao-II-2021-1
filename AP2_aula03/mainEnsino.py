from Aluno import Aluno
from AluEnsinoMedio import AluEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

class mainEnsino:

    aluno = Aluno(123, "João", 90)
    aluno.imprimir()

    alunoEM = AluEnsinoMedio(555, "Maria", 87, 2020)
    alunoEM.imprimir()

    alunoGR = AlunoGraduacao(987, "Henrique", 234, 4)
    alunoGR.imprimir()