from dal.cliente_dal import ClienteDal
from model.cliente import Cliente
from reports.relatorio_cliente import RelatorioCliente


class ClienteController:
    @classmethod
    def cadastrar_cliente(cls, nome: str, idade: int, cpf: str):
        if len(nome) > 2 and idade > 12 and len(cpf) == 11:
            try:
                cliente = Cliente(nome, idade, cpf)
                cliente_dal = ClienteDal()
                cliente_dal.add_cliente(cliente)
                return True
            except (IOError, OSError) as e:
                print(f"Erro ao acessar o arquivo: {e}")
                return False
        print("Dados inválidos para cadastro.")
        return False

    @classmethod
    def listar_clientes(cls):
        cliente_dal = ClienteDal()
        return cliente_dal.listar_clientes()

    @classmethod
    def buscar_cliente_cpf(cls, cpf: str):
        cliente_dal = ClienteDal()
        return cliente_dal.buscar_cliente_cpf(cpf)

    @classmethod
    def editar_cliente(cls, cpf: str, novo_nome: str, nova_idade: int):
        cliente_dal = ClienteDal()
        return cliente_dal.editar_cliente(cpf, novo_nome, nova_idade)

    @classmethod
    def remover_cliente(cls, cpf: str):
        cliente_dal = ClienteDal()
        return cliente_dal.remover_cliente(cpf)

    @classmethod
    def relatorio_cliente(cls):
        RelatorioCliente.relatorio_todos_clientes()