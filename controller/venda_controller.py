from dal.venda_dal import VendaDal
from model.venda import Venda
from reports.relatorio_venda import RelatorioVenda


class VendaController:
    @classmethod
    def criar_venda(cls, id: int, produto_id: int, quantidade: int, preco_unitario: float, total: float, data: str,
                    cliente_id: int):
        try:
            venda = Venda(id, produto_id, quantidade, preco_unitario, total, data, cliente_id)
            venda_dal = VendaDal()
            venda_dal.add_venda(venda)
            return True
        except (IOError, OSError) as e:
            print(f"Erro ao acessar o arquivo: {e}")
            return False

    @classmethod
    def listar_vendas(cls):
        venda_dal = VendaDal()
        return venda_dal.listar_vendas()

    @classmethod
    def buscar_venda_id(cls, id: int):
        venda_dal = VendaDal()
        return venda_dal.buscar_venda_id(id)

    @classmethod
    def atualizar_venda(cls, id: int, nova_quantidade: int, novo_preco_unitario: float, novo_total: float):
        venda_dal = VendaDal()
        return venda_dal.editar_venda(id, nova_quantidade, novo_preco_unitario, novo_total)

    @classmethod
    def deletar_venda(cls, id: int):
        venda_dal = VendaDal()
        return venda_dal.remover_venda(id)

    @classmethod
    def relatorio_venda(cls):
        RelatorioVenda.relatorio_todos_transacts()