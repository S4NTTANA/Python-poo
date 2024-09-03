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
    def __str__(self) -> str:
        return f"===== Informações do Funcionário ===== \nNome: {self.nome} \nTelefone: {self.telefone} \nEMAIL: {self.email}\n \n==== Endereço ==== \n{self.endereco} \nSalario: {self.salario}"
    
    @abstractmethod
    def salarioFinal() -> float:
        pass
class Engenheiro(Funcionario): 
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        
    def salarioFinal() -> float:
        pass

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
    
    def salarioFinal() -> float:
        pass
    
    
engenheiro = Engenheiro("Maumau", "(71) 9 8754 5784", "maumau123@gamil.com", 2500.00,
                         Endereco ("Rua a", 412, "ao lado do mercado", "46554-450", "Salvador"))
medico = Medico("Marcos", "(71) 9 8857 2538", "marcos123@gamil.com", 3800.00, 
                Endereco ("Rua b", 235, "Avenida Thomas Purbano Pinto", "50235-020", "Salvador"))


# Instanciar classes.
#funcionario = Funcionario("José", 23, 2500)
print(engenheiro)
print("\n \n")
print(medico)


        
