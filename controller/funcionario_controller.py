from model.funcionario import FuncionarioDal

class FuncionarioController:

    @classmethod
    def cadastrar_funcionario(cls, nome: str, idade: int, cpf: str, total_vendas: int):
        if len(nome) > 2 and idade > 12 and len(cpf) == 11 and total_vendas >= 0:
            try:
                funcionario = FuncionarioDal()
                funcionario.add_funcionario(nome, idade, cpf, total_vendas)
                return True
            except Exception as e:
                print(f"Erro ao cadastrar funcionário: {e}")
                return False
        else:
            print("Dados inválidos para cadastro.")
            return False
        
    @classmethod
    def listar_funcionarios(cls):
        funcionario = FuncionarioDal()
        return funcionario.listar_funcionarios()
    
    @classmethod
    def buscar_funcionario(cls, cpf: str):
        funcionario = FuncionarioDal()
        return funcionario.buscar_funcionario_cpf(cpf)
    
    @classmethod
    def editar_funcionario(cls, cpf: str, novo_nome:str, nova_idade:str, novo_total_vendas:int):
        funcionario = FuncionarioDal()
        return funcionario.editar_funcionario(cpf, novo_nome, nova_idade, novo_total_vendas)
    
    @classmethod
    def remover_funcionario(cls, cpf: str):
        funcionario = FuncionarioDal()
        return funcionario.remover_funcionario(cpf)