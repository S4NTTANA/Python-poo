import os 
os.system ("cls || clear")
from abc import ABC, abstractmethod

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        
    def __str__ (self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nCidade: {self.cidade}"


class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.salario = salario
    def __str__(self) -> str:
        return f"===== Informações do Funcionário ===== \nNome: {self.nome} \nEMAIL: {self.email}\n \n==== Endereço ==== \n{self.endereco} \nSalario: {self.salario}"
    
    @abstractmethod
    def salarioFinal() -> float:
        pass

    class Motoboy(Funcionario): 
        def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
            super().__init__(nome, email, salario, endereco)

        
    def salarioFinal() -> float:
        pass

    class Gerente(Funcionario):
        def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
            super().__init__(nome, email, salario, endereco)


    


    



    def salarioFinal() -> float:
        pass