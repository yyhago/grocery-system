class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Cliente -> Nome: {self.nome} (CPF: {self.cpf} | Idade: {self.idade})"