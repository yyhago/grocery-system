from dal.cliente_dal import ClienteDal

class RelatorioCliente:
    @classmethod
    def relatorio_todos_clientes(cls):
        cliente_dal = ClienteDal()
        clientes = cliente_dal.listar_clientes()

        if not clientes:
            print("\nNenhum cliente cadastrado.")
            return

        print("\nRELATÓRIO GERAL DE CLIENTES")
        print("-" * 60)
        for cliente in clientes:
            print(f"Nome: {cliente['nome']} | Idade: {cliente['idade']} | CPF: {cliente['cpf']}")
        print("-" * 60)