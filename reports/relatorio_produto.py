from dal.produto_dal import ProdutoDal

class RelatorioProduto:
    @classmethod
    def relatorio_todos_produtos(cls):
        produto_dal = ProdutoDal()
        produtos = produto_dal.listar_produtos()

        if not produtos:
            print("\nNenhum produto cadastrado.")
            return

        print("\nRELATÓRIO GERAL DE PRODUTOS")
        print("-" * 80)
        for produto in produtos:
            print(f"ID Produto: {produto['id']} | Nome: {produto['nome']} | "
                  f"Preço: R${float(produto['preco']):.2f} | Quantidade em Estoque: {produto['quantidade']} | "
                  f"Categoria ID: {produto['categoria_id']}")
        print("-" * 80)