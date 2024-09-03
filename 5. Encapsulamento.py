import os 
os.system("cls || clear")

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise f"saldo insuficiente" # Lançando um erro.
        self._saldo -= valor
        return self._saldo
    
    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

# Adicionando valor a atributo protegido 
conta_corrente._saldo -= 200

print (conta_corrente.sacar(200))
