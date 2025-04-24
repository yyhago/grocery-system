from model.venda import Venda

class VendaController:

    @classmethod
    def criar_venda(cls, id: int, produto_id: int, quantidade:int, preco_unitario:float, total:float, data: str, cliente_id: int):
        venda_dal = Venda()
        return venda_dal.criar_venda(id, produto_id, quantidade, preco_unitario, total, data, cliente_id)
    
    @classmethod
    def listar_vendas(cls):
        venda_dal = Venda()
        return venda_dal.listar_vendas()
    
    @classmethod
    def buscar_venda(cls, id: int):
        venda_dal = Venda()
        return venda_dal.buscar_venda(id)
    
    @classmethod
    def atualizar_venda(cls, id: int, produto_id: int, quantidade:int, preco_unitario:float, total:float, data: str, cliente_id: int):
        venda_dal = Venda()
        return venda_dal.atualizar_venda(id, produto_id, quantidade, preco_unitario, total, data, cliente_id)
    
    @classmethod
    def deletar_venda(cls, id: int):
        venda_dal = Venda()
        return venda_dal.deletar_venda(id)