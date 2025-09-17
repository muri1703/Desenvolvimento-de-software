from datetime import date

# Interface Transacao
class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Método abstrato. Deve ser implementado nas subclasses.")


# Subclasses de Transacao
class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

# Classe Conta
class Conta:
    def __init__(self, cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self) -> float:
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite: float = 1000.0, limite_saques: int = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

# Classe Cliente
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

# Classe PessoaFisica
class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
