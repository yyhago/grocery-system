class FuncionarioDal:

    def add_funcionario(self, funcionario):
        with open("./data/funcionarios.txt", "a") as arquivo:
            arquivo.write(f"{funcionario.nome};{funcionario.idade};{funcionario.cpf};{funcionario.total_vendas}\n")

    def listar_funcionarios(self):
        funcionarios = []
        with open("./data/funcionarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade, cpf, total_vendas = linha.strip().split(";")
                funcionarios.append({"nome": nome, "idade": idade, "cpf": cpf, "total_vendas": total_vendas})
        return funcionarios

    def buscar_funcionario_cpf(self, cpf):
        funcionarios = self.listar_funcionarios()
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                return funcionario
        return None

    def editar_funcionario(self, cpf, novo_nome, nova_idade, novo_total_vendas):
        funcionarios = self.listar_funcionarios()
        funcionario_encontrado = False
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                funcionario["nome"] = novo_nome
                funcionario["idade"] = nova_idade
                funcionario["total_vendas"] = novo_total_vendas
                funcionario_encontrado = True
                break
        if funcionario_encontrado:
            with open("./data/funcionarios.txt", "w") as arquivo:
                for funcionario in funcionarios:
                    arquivo.write(f"{funcionario['nome']};{funcionario['idade']};{funcionario['cpf']};{funcionario['total_vendas']}\n")
        return funcionario_encontrado

    def remover_funcionario(self, cpf):
        funcionarios = self.listar_funcionarios()
        funcionario_encontrado = False
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                funcionarios.remove(funcionario)
                funcionario_encontrado = True
                break
        if funcionario_encontrado:
            with open("./data/funcionarios.txt", "w") as arquivo:
                for funcionario in funcionarios:
                    arquivo.write(f"{funcionario['nome']};{funcionario['idade']};{funcionario['cpf']};{funcionario['total_vendas']}\n")
        return funcionario_encontrado
