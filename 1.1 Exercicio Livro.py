import os

os.system ("cls || clear")

class Livro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numero_paginas} \nPreço: R${self.preco}"

livro = Livro("Hamlet", "William shakespeare", 160, 39.12)

print (livro.exibir_dados())