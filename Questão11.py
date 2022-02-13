class Cliente:
     def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta(Cliente):
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)
    def resumo(self):
        print("Nome: %s \n Telefone: %f CC N°%s \n Saldo: %10.2f  \n  " (self.nome, self.telefone, 
        self.número, self.saldo))
    def pode_sacar(self, valor):
        return self.saldo >= valor
    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente")
            return False
        elif (self.saldo >= valor):
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return False
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0],o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)

class ContaEspecial(Conta):
     def __init__(self, clientes, número, saldo = 0, limite=0):
         Conta.__init__(self, clientes, número, saldo)
         self.limite = limite
     def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor
     def saque(self, valor):
         if self.saldo + self.limite >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
               return True
         else:
               return False
     def extrato(self):
        Conta.extrato(self)
        print("\n Limite: %10.2f\n" % self.limite)
        print("\n Disponivel: %10.2f\n" % (self.limite + self.saldo))
