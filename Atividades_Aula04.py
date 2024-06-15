#Questão 1
# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#Questão 2

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

# livro1 = Livro("Guerra e Paz", "  Liev Tolstói",  1869)
# livro2 = Livro("Crime e Castigo", "  Fiódor Dostoiévski", 1866)

# print(livro1)
# print(livro2)

# #Questão 3

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

#     def emprestar(self):
#         self.disponivel = False

# livro = Livro("Guerra e Paz", "  Liev Tolstói",  1869)

# livro.emprestar()

# print(f"O livro está disponível? {'Sim' if livro.disponivel else 'Não'}")

#Questão 4

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

livro1 = Livro("Guerra e Paz", "  Liev Tolstói",  1869)
livro2 = Livro("Crime e Castigo", "  Fiódor Dostoiévski", 1866)
livro3 = Livro("Em Busca do Tempo Perdido", " Marcel Proust", 1913)
livro4 = Livro("Ulisses", " James Joyce", 1922)

livro1.emprestar()

livros_disponiveis_1922 = Livro.verificar_disponibilidade(1922)
for livro in livros_disponiveis_1922:
    print(livro)

livros_disponiveis_1866 = Livro.verificar_disponibilidade(1866)
for livro in livros_disponiveis_1866:
    print(livro)
