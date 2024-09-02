from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario): 
    def calcular_salario(self) -> float:
        # Acréscimo de 20%
        BONIFICACAO = 1.20
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.10
        salario_final = self.salario * BONIFICACAO
        return salario_final
        

# Instanciar classes.
#funcionario = Funcionario("José", 23, 2500)
gerente = Gerente("Carlos", 25, 3000)
motoboy = Motoboy("Luis", 31, 2000, "451235")

print (f"Nome: {gerente.nome}")
print (f"Idade: {gerente.idade}")
print (f"Salário: {gerente.calcular_salario()}")

print (f"\nNome: {motoboy.nome}")
print (f"Idade: {motoboy.idade}")
print (f"Salário: {motoboy.calcular_salario()}")
        
