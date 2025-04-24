from model.produto import ProdutoDal

class ProdutoController:

    @classmethod
    def cadastrar_produto(cls, nome: str, id: int, preco: float, quantidade:int, categoria_id: int):
        produto_dal = ProdutoDal()
        return produto_dal.cadastrar_produto(nome, id, preco, quantidade, categoria_id)
    
    @classmethod
    def listar_produtos(cls):
        produto_dal = ProdutoDal()
        return produto_dal.listar_produtos()

    @classmethod
    def buscar_produto_id(cls, id: int):
        produto_dal = ProdutoDal()
        return produto_dal.buscar_produto_id(id)

    @classmethod
    def editar_produto(cls, id: int, novo_nome: str, novo_preco: float, nova_quantidade: int):
        produto_dal = ProdutoDal()
        return produto_dal.editar_produto(id, novo_nome, novo_preco, nova_quantidade)

    @classmethod
    def remover_produto(cls, id: int):
        produto_dal = ProdutoDal()
        return produto_dal.remover_produto(id)    