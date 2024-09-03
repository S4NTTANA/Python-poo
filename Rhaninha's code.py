import os
os.system ("cls || clear")
    

class Endereco:
    # Construtor:
    def __init__(self, logradouro: str, numero: str, complemento: str, Cep: str, cidade: str) -> None:
        # Atributos: 
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.Ce = Cep
        self.cidade = cidade

    def __str__ (self) -> str:
         return (f"Logradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.Cep} \nCidade: {self.cidade}")

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
               f"\nTelefone: {self.telefone}"
               f"\nEmail: {self.email}"
               f"\nSalário: {self.salarioFinal()}"
               f"\nEndereço: {self.endereco}"
               )

class Engenheiro(Funcionario):
    def __init__(self, nome: str, idade: int, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, idade, email, endereco)
        self.crea = crea

    def salarioFinal(self) -> float:
        return 2000.0
     

class Medico(Funcionario):
    def __init__(self, nome: str, idade: int, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, idade, email, endereco)
        self.crm = crm
    
    def salarioFinal(self) -> float:
       return 5000.0
    
# engenheiro1 = Engenheiro("Fulano", 26, "71988547203", "fulano@gmail.com", "152638", 
#                         Endereco("Avenida 8", "4", "Ao lado do deposito", "41587-963", "Salvador"))

medico1 = Medico("Ciclano", 45, "71988475693", "ciclano@gmail.com", 745126, 
                Endereco("Rua H", "72", "Em frente a quadra", "41854-697", "Salvador"))


print("\n")
print("Dados do médico: ")
print(medico1)


# print("\n")
# print("Dados do engenheiro: ")
# print(f"Nome: {engenheiro1.nome}")
# print(f"Idade: {engenheiro1.idade}")
# print(f"Telefone: {engenheiro1.telefone}")
# print(f"Email: {engenheiro1.email}")
# print("\n")
# print(f"Dados do endereço fornecido: ")
# print(f"{engenheiro1.endereco}")
# print(f"Salário: {engenheiro1.salario}")
# print(f"CREA: {engenheiro1.crea}")
