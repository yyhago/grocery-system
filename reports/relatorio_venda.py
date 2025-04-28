from dal.venda_dal import VendaDal

class RelatorioVenda:
    @classmethod
    def relatorio_todos_transacts(cls):
        venda_dal = VendaDal()
        vendas = venda_dal.listar_vendas()

        if not vendas:
            print("\nNenhuma venda registrada.")
            return

        print("\nRELATÓRIO GERAL DE VENDAS")
        print("-" * 80)
        total_geral = 0
        for venda in vendas:
            print(f"ID Venda: {venda['id']} | Produto ID: {venda['produto_id']} | "
                  f"Quantidade: {venda['quantidade']} | Preço Unitário: R${float(venda['preco_unitario']):.2f} | "
                  f"Total: R${float(venda['total']):.2f} | Data: {venda['data']} | Cliente ID: {venda['cliente_id']}")
            total_geral += float(venda['total'])
        print("-" * 80)
        print(f"Receita Total: R${total_geral:.2f}")
        print("-" * 80)