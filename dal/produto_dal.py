import os
from model.produto import Produto


class ProdutoDal:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def add_produto(self, produto: Produto):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        with open(os.path.join(self.DATA_DIR, "produtos.txt"), "a") as arquivo:
            arquivo.write(f"{produto.nome};{produto.id};{produto.preco};{produto.quantidade};{produto.categoria_id}\n")

    def listar_produtos(self):
        produtos = []
        try:
            with open(os.path.join(self.DATA_DIR, "produtos.txt"), "r") as arquivo:
                for linha in arquivo:
                    nome, id, preco, quantidade, categoria_id = linha.strip().split(";")
                    produtos.append({
                        "nome": nome,
                        "id": id,
                        "preco": preco,
                        "quantidade": quantidade,
                        "categoria_id": categoria_id
                    })
        except FileNotFoundError:
            print("Arquivo produtos.txt não encontrado!")
        return produtos

    def buscar_produto_id(self, id: int):
        produtos = self.listar_produtos()
        for produto in produtos:
            if produto["id"] == str(id):
                return produto
        return None

    def editar_produto(self, id: int, novo_nome: str, novo_preco: float, nova_quantidade: int):
        produtos = self.listar_produtos()
        produto_encontrado = False
        for produto in produtos:
            if produto["id"] == str(id):
                produto["nome"] = novo_nome
                produto["preco"] = str(novo_preco)
                produto["quantidade"] = str(nova_quantidade)
                produto_encontrado = True
                break
        if produto_encontrado:
            with open(os.path.join(self.DATA_DIR, "produtos.txt"), "w") as arquivo:
                for produto in produtos:
                    arquivo.write(
                        f"{produto['nome']};{produto['id']};{produto['preco']};{produto['quantidade']};{produto['categoria_id']}\n")
        return produto_encontrado

    def remover_produto(self, id: int):
        produtos = self.listar_produtos()
        produto_encontrado = False
        for produto in produtos:
            if produto["id"] == str(id):
                produtos.remove(produto)
                produto_encontrado = True
                break
        if produto_encontrado:
            with open(os.path.join(self.DATA_DIR, "produtos.txt"), "w") as arquivo:
                for produto in produtos:
                    arquivo.write(
                        f"{produto['nome']};{produto['id']};{produto['preco']};{produto['quantidade']};{produto['categoria_id']}\n")
        return produto_encontrado