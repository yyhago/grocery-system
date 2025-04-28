from dal.funcionario_dal import FuncionarioDal
from model.funcionario import Funcionario


class FuncionarioController:
    @classmethod
    def cadastrar_funcionario(cls, nome: str, idade: int, cpf: str, totalVendas: float):
        if len(nome) > 2 and idade > 12 and len(cpf) == 11 and totalVendas >= 0:
            try:
                funcionario = Funcionario(nome, idade, cpf, totalVendas)
                funcionario_dal = FuncionarioDal()
                funcionario_dal.add_funcionario(funcionario)
                return True
            except (IOError, OSError) as e:
                print(f"Erro ao acessar o arquivo: {e}")
                return False
        print("Dados inválidos para cadastro.")
        return False

    @classmethod
    def listar_funcionarios(cls):
        funcionario_dal = FuncionarioDal()
        return funcionario_dal.listar_funcionarios()

    @classmethod
    def buscar_funcionario_cpf(cls, cpf: str):
        funcionario_dal = FuncionarioDal()
        return funcionario_dal.buscar_funcionario_cpf(cpf)

    @classmethod
    def editar_funcionario(cls, cpf: str, novo_nome: str, nova_idade: int, novo_totalVendas: float):
        funcionario_dal = FuncionarioDal()
        return funcionario_dal.editar_funcionario(cpf, novo_nome, nova_idade, novo_totalVendas)

    @classmethod
    def remover_funcionario(cls, cpf: str):
        funcionario_dal = FuncionarioDal()
        return funcionario_dal.remover_funcionario(cpf)