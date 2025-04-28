import os
from model.funcionario import Funcionario

class FuncionarioDal:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def add_funcionario(self, funcionario: Funcionario):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        with open(os.path.join(self.DATA_DIR, "funcionarios.txt"), "a") as arquivo:
            arquivo.write(f"{funcionario.nome};{funcionario.idade};{funcionario.cpf};{funcionario.totalVendas}\n")

    def listar_funcionarios(self):
        funcionarios = []
        try:
            with open(os.path.join(self.DATA_DIR, "funcionarios.txt"), "r") as arquivo:
                for linha in arquivo:
                    nome, idade, cpf, total_vendas = linha.strip().split(";")
                    funcionarios.append({"nome": nome, "idade": idade, "cpf": cpf, "total_vendas": total_vendas})
        except FileNotFoundError:
            print("Arquivo funcionarios.txt não encontrado!")
        return funcionarios

    def buscar_funcionario_cpf(self, cpf: str):
        funcionarios = self.listar_funcionarios()
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                return funcionario
        return None

    def editar_funcionario(self, cpf: str, novo_nome: str, nova_idade: int, novo_total_vendas: float):
        funcionarios = self.listar_funcionarios()
        funcionario_encontrado = False
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                funcionario["nome"] = novo_nome
                funcionario["idade"] = str(nova_idade)
                funcionario["total_vendas"] = str(novo_total_vendas)
                funcionario_encontrado = True
                break
        if funcionario_encontrado:
            with open(os.path.join(self.DATA_DIR, "funcionarios.txt"), "w") as arquivo:
                for funcionario in funcionarios:
                    arquivo.write(f"{funcionario['nome']};{funcionario['idade']};{funcionario['cpf']};{funcionario['total_vendas']}\n")
        return funcionario_encontrado

    def remover_funcionario(self, cpf: str):
        funcionarios = self.listar_funcionarios()
        funcionario_encontrado = False
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                funcionarios.remove(funcionario)
                funcionario_encontrado = True
                break
        if funcionario_encontrado:
            with open(os.path.join(self.DATA_DIR, "funcionarios.txt"), "w") as arquivo:
                for funcionario in funcionarios:
                    arquivo.write(f"{funcionario['nome']};{funcionario['idade']};{funcionario['cpf']};{funcionario['total_vendas']}\n")
        return funcionario_encontrado