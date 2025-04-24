from model.fornecedor import FornecedorDal

class FornecedorController:

    @classmethod
    def cadastrar_fornecedor(cls, nome: str, idade: int, cpf: str):
        if len(nome) > 2 and idade > 12 and len(cpf) == 11:
            try:
                fornecedor_dal = FornecedorDal()
                fornecedor_dal.add_fornecedor(nome, idade, cpf)
                return True
            except Exception as e:
                print(f"Erro ao cadastrar fornecedor: {e}")
                return False
        else:
            print("Dados inválidos para cadastro.")
            return False
        
    @classmethod
    def listar_fornecedores(cls):
        fornecedor_dal = FornecedorDal()
        return fornecedor_dal.listar_fornecedores()

    @classmethod
    def buscar_fornecedor(cls, cpf: str):
        fornecedor_dal = FornecedorDal()
        return fornecedor_dal.buscar_fornecedor_cpf(cpf)
    
    @classmethod
    def editar_fornecedor(cls, cpf: str, novo_nome: str, nova_idade: int, novo_cpf: str):
        fornecedor_dal = FornecedorDal()
        return fornecedor_dal.editar_fornecedor(cpf, novo_nome, nova_idade, novo_cpf)
    
    @classmethod
    def remover_fornecedor(cls, cpf: str):
        fornecedor_dal = FornecedorDal()
        return fornecedor_dal.remover_fornecedor(cpf)