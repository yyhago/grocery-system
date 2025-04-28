class Produto:
    def __init__(self, nome: str, id: int, preco: float, quantidade: int, categoria_id: int):
        self.nome = nome
        self.id = id
        self.preco = preco
        self.quantidade = quantidade
        self.categoria_id = categoria_id

    def __str__(self):
        return f"Produto -> ID: {self.id} | Nome: {self.nome} | Preço: {self.preco} | Quantidade: {self.quantidade} | Categoria ID: {self.categoria_id}"