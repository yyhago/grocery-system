import os
from model.fornecedor import Fornecedor

class FornecedorDal:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def add_fornecedor(self, fornecedor: Fornecedor):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        with open(os.path.join(self.DATA_DIR, "fornecedores.txt"), "a") as arquivo:
            arquivo.write(f"{fornecedor.nome};{fornecedor.idade};{fornecedor.cpf}\n")

    def listar_fornecedores(self):
        fornecedores = []
        try:
            with open(os.path.join(self.DATA_DIR, "fornecedores.txt"), "r") as arquivo:
                for linha in arquivo:
                    nome, idade, cpf = linha.strip().split(";")
                    fornecedores.append({"nome": nome, "idade": idade, "cpf": cpf})
        except FileNotFoundError:
            print("Arquivo fornecedores.txt não encontrado!")
        return fornecedores

    def buscar_fornecedor_cpf(self, cpf: str):
        fornecedores = self.listar_fornecedores()
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                return fornecedor
        return None

    def editar_fornecedor(self, cpf: str, novo_nome: str, nova_idade: int, novo_cpf: str):
        fornecedores = self.listar_fornecedores()
        fornecedor_encontrado = False
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                fornecedor["nome"] = novo_nome
                fornecedor["idade"] = str(nova_idade)
                fornecedor["cpf"] = novo_cpf
                fornecedor_encontrado = True
                break
        if fornecedor_encontrado:
            with open(os.path.join(self.DATA_DIR, "fornecedores.txt"), "w") as arquivo:
                for fornecedor in fornecedores:
                    arquivo.write(f"{fornecedor['nome']};{fornecedor['idade']};{fornecedor['cpf']}\n")
        return fornecedor_encontrado

    def remover_fornecedor(self, cpf: str):
        fornecedores = self.listar_fornecedores()
        fornecedor_encontrado = False
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                fornecedores.remove(fornecedor)
                fornecedor_encontrado = True
                break
        if fornecedor_encontrado:
            with open(os.path.join(self.DATA_DIR, "fornecedores.txt"), "w") as arquivo:
                for fornecedor in fornecedores:
                    arquivo.write(f"{fornecedor['nome']};{fornecedor['idade']};{fornecedor['cpf']}\n")
        return fornecedor_encontrado