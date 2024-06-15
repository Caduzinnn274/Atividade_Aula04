#Questão 5 e 6 e 7
from Atividades_Aula04 import Livro

livro1 = Livro("Guerra e Paz", "  Liev Tolstói",  1869)
livro2 = Livro("Crime e Castigo", "  Fiódor Dostoiévski", 1866)

livro1.emprestar()

print(f"O livro 'Moby Dick' está disponível após o empréstimo? {'Sim' if livro1.disponivel else 'Não'}")

livros_disponiveis_1922 = Livro.verificar_disponibilidade(1922)
for livro in livros_disponiveis_1922:
    print(livro)

livros_disponiveis_1866 = Livro.verificar_disponibilidade(1869)
for livro in livros_disponiveis_1866:
    print(livro)