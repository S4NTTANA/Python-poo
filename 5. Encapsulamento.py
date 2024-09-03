import os 
os.system("cls || clear")

# TRATAMENTO DE EXCEÇÕES 

# Criando exceção
class SaldoInsuficienteError(Exception):
    pass
class valorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        try:
            self.verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
    
    def verificar_sacar(self, valor):  # Método privado 
        # try - except
        if valor > self.saldo:
            raise SaldoInsuficienteError ("Saldo Insuficiente!") # Lançando um erro.

    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except valorNegativoError as error:
            return f"Erro: {error}"
        
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0:
            raise valorNegativoError("Não é possível depositar valor negativo!")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

# Adicionando valor a atributo protegido 
#conta_corrente._saldo -= 200

print (conta_corrente.saldo)
print (conta_corrente.sacar(200))
print (conta_corrente.depositar(-200))