class FornecedorDal:

    def add_fornecedor(self, fornecedor):
        with open("./data/fornecedores.txt", "a") as arquivo:
            arquivo.write(f"{fornecedor.nome};{fornecedor.idade};{fornecedor.cpf}\n")

    def listar_fornecedores(self):
        fornecedores = []
        with open("./data/fornecedores.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade, cpf = linha.strip().split(";")
                fornecedores.append({"nome": nome, "idade": idade, "cpf": cpf})
        return fornecedores

    def buscar_fornecedor_cpf(self, cpf):
        fornecedores = self.listar_fornecedores()
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                return fornecedor
        return None

    def editar_fornecedor(self, cpf, novo_nome, nova_idade, novo_cpf):
        fornecedores = self.listar_fornecedores()
        fornecedor_encontrado = False
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                fornecedor["nome"] = novo_nome
                fornecedor["idade"] = nova_idade
                fornecedor["cpf"] = novo_cpf
                fornecedor_encontrado = True
                break
        if fornecedor_encontrado:
            with open("./data/fornecedores.txt", "w") as arquivo:
                for fornecedor in fornecedores:
                    arquivo.write(f"{fornecedor['nome']};{fornecedor['idade']};{fornecedor['cpf']}\n")
        return fornecedor_encontrado

    def remover_fornecedor(self, cpf):
        fornecedores = self.listar_fornecedores()
        fornecedor_encontrado = False
        for fornecedor in fornecedores:
            if fornecedor["cpf"] == cpf:
                fornecedores.remove(fornecedor)
                fornecedor_encontrado = True
                break
        if fornecedor_encontrado:
            with open("./data/fornecedores.txt", "w") as arquivo:
                for fornecedor in fornecedores:
                    arquivo.write(f"{fornecedor['nome']};{fornecedor['idade']};{fornecedor['cpf']}\n")
        return fornecedor_encontrado