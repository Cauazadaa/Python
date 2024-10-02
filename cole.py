class Material:
    def __init__(self,titulo,autor) -> None:
        self.autor = autor
        self.titulo = titulo
        exibir_informacoes()


def exibir_informacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')

class Livro(Material):
     def __init__(self,titulo,autor,genero) -> None:
        super().__init__(titulo,autor,genero)
        self.genero = genero

def exibir_informacoes(self):
     super().exibir_informacoes()
     print(f'Gênero: {self.genero}')

class Revista(Material):
     def __init__(self, titulo,autor, edicao) -> None:
          super().__init__(titulo,autor,edicao)    
          self.edicao = edicao    
def exibir_informacoes(self):
     super().exibir_informacoes()
     print(f'Edição: {self.edicao}')
    

livro1=Livro('o ego e seu inimigo','Ryan Holiday','psicologia')
revista1=Revista('o grande brasil','Rommel SIlva','nona_ediçao')


print("Informações do Livro:")
livro1.exibir_informacoes()

print("\nInformações da Revista:")
revista1.exibir_informacoes()