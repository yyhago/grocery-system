from dal.produto_dal import ProdutoDal
from model.produto import Produto
from reports.relatorio_produto import RelatorioProduto


class ProdutoController:
    @classmethod
    def cadastrar_produto(cls, nome: str, id: int, preco: float, quantidade: int, categoria_id: int):
        try:
            produto = Produto(nome, id, preco, quantidade, categoria_id)
            produto_dal = ProdutoDal()
            produto_dal.add_produto(produto)
            return True
        except (IOError, OSError) as e:
            print(f"Erro ao acessar o arquivo: {e}")
            return False

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

    @classmethod
    def relatorio_produto(cls):
        RelatorioProduto.relatorio_todos_produtos()