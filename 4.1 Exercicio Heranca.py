from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__ (self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCep: {self.cep} \nCidade: {self.cidade}"


class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Engenheiro(Funcionario): 
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        
    def calcular_salario(self) -> float:
        # Acréscimo de 20%
        BONIFICACAO = 1.20
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Medico(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.10
        salario_final = self.salario * BONIFICACAO
        return salario_final
        

# Instanciar classes.
#funcionario = Funcionario("José", 23, 2500)
engenheiro = Engenheiro()
medico = Medico()


        
