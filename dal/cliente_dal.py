import os
from model.cliente import Cliente


class ClienteDal:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def add_cliente(self, cliente: Cliente):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        with open(os.path.join(self.DATA_DIR, "clientes.txt"), "a") as arquivo:
            arquivo.write(f"{cliente.nome};{cliente.idade};{cliente.cpf}\n")

    def listar_clientes(self):
        clientes = []
        try:
            with open(os.path.join(self.DATA_DIR, "clientes.txt"), "r") as arquivo:
                for linha in arquivo:
                    nome, idade, cpf = linha.strip().split(";")
                    clientes.append({"nome": nome, "idade": idade, "cpf": cpf})
        except FileNotFoundError:
            print("Arquivo clientes.txt não encontrado!")
        return clientes

    def buscar_cliente_cpf(self, cpf: str):
        clientes = self.listar_clientes()
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                return cliente
        return None

    def editar_cliente(self, cpf: str, novo_nome: str, nova_idade: int):
        clientes = self.listar_clientes()
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                cliente["nome"] = novo_nome
                cliente["idade"] = str(nova_idade)
                cliente_encontrado = True
                break
        if cliente_encontrado:
            with open(os.path.join(self.DATA_DIR, "clientes.txt"), "w") as arquivo:
                for cliente in clientes:
                    arquivo.write(f"{cliente['nome']};{cliente['idade']};{cliente['cpf']}\n")
        return cliente_encontrado

    def remover_cliente(self, cpf: str):
        clientes = self.listar_clientes()
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                clientes.remove(cliente)
                cliente_encontrado = True
                break
        if cliente_encontrado:
            with open(os.path.join(self.DATA_DIR, "clientes.txt"), "w") as arquivo:
                for cliente in clientes:
                    arquivo.write(f"{cliente['nome']};{cliente['idade']};{cliente['cpf']}\n")
        return cliente_encontrado