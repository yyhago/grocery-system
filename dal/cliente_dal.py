class ClienteDal:
    
    def add_cliente(self, cliente):
        with open("./data/clientes.txt", "a") as arquivo:
            arquivo.write(f"{cliente.nome};{cliente.idade};{cliente.cpf}\n")

    def listar_clientes(self):
        clientes = []
        with open("./data/clientes.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade, cpf = linha.strip().split(";")
                clientes.append({"nome": nome, "idade": idade, "cpf": cpf})
        return clientes

    def buscar_cliente_cpf(self, cpf):
        clientes = self.listar_clientes()
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                return cliente
        return None

    def editar_cliente(self, cpf, novo_nome, nova_idade):
        clientes = self.listar_clientes()
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                cliente["nome"] = novo_nome
                cliente["idade"] = nova_idade
                cliente_encontrado = True
                break
        if cliente_encontrado:
            with open("./data/clientes.txt", "w") as arquivo:
                for cliente in clientes:
                    arquivo.write(f"{cliente['nome']};{cliente['idade']};{cliente['cpf']}\n")
        return cliente_encontrado
    
    def remover_cliente(self, cpf):
        clientes = self.listar_clientes()
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                clientes.remove(cliente)
                cliente_encontrado = True
                break
        if cliente_encontrado:
            with open("./data/clientes.txt", "w") as arquivo:
                for cliente in clientes:
                    arquivo.write(f"{cliente['nome']};{cliente['idade']};{cliente['cpf']}\n")
        return cliente_encontrado