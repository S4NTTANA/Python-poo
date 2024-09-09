from enum import Enum
import os 
os.system ("cls || clear")

class Sexo (enumerate):
    """Definindo valores Enum"""
    
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor (enumerate):

    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Pessoa:
    """Construtor"""
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = Setor      
        self.sexo = sexo

    def __str__(self) -> str:
        """ Equivalente ao toString() do java"""
        return (f"\nId: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nsalario: {self.salario}"
                f"\nSetor: {self.setor}"
                f"\nSexo: {self.sexo}"
                )

# Instanciando classe Pessoa.
pessoa_1 = Pessoa (406507, "Marta", 22, 2500.0, Setor.MARKETING, Sexo.FEMININO)

print (pessoa_1)