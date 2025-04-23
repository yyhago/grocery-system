class Venda:
    def __init__(self, id, produto_id, quantidade, preco_unitario, total, data, cliente_id):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total = total
        self.data = data
        self.cliente_id = cliente_id

    def __str__(self):
        return (f"Venda -> ID: {self.id} | Produto ID: {self.produto_id} | Quantidade: {self.quantidade} | "
                f"Preço Unitário: {self.preco_unitario} | Total: {self.total} | Data: {self.data} | Cliente ID: {self.cliente_id}")
