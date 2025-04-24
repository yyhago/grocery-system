from model.produto import Produto

class ProdutoDal:
    
    def add_produto(self,produto: Produto):
        with open("./data/produtos.txt", "a") as arquivo:
            arquivo.write(f"{produto.nome};{produto.id};{produto.preco};{produto.quantidade};{produto.categoria_id}\n")

    def listar_produtos(self):
        produtos = []        
        with open("./data/produtos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, id, preco, quantidade, categoria_id = linha.strip().split(";")
                produtos.append({"nome": nome, "id": id, "preco": preco, "quantidade": quantidade, "categoria_id": categoria_id})
        return produtos
    
    def buscar_produto_id(self, id):
        produtos = self.listar_produtos()
        for produto in produtos:
            if produto["id"] == id:
                return produto
        return None 
    
    def editar_produto(self, id, novo_nome, novo_preco, nova_quantidade):
        produtos = self.listar_produtos()
        produto_encontrado = False
        for produto in produtos:
            if produto["id"] == id:
                produto["nome"] = novo_nome
                produto["preco"] = novo_preco
                produto["quantidade"] = nova_quantidade
                produto_encontrado = True
                break
        if produto_encontrado:
            with open("./data/produtos.txt", "w") as arquivo:
                for produto in produtos:
                    arquivo.write(f"{produto['nome']};{produto['id']};{produto['preco']};{produto['quantidade']};{produto['categoria_id']}\n")
        return produto_encontrado
    
    def remover_produto(self, id):
        produtos = self.listar_produtos()
        produto_encontrado = False
        for produto in produtos:
            if produto["id"] == id:
                produtos.remove(produto)
                produto_encontrado = True
                break
        if produto_encontrado:
            with open("./data/produtos.txt", "w") as arquivo:
                for produto in produtos:
                    arquivo.write(f"{produto['nome']};{produto['id']};{produto['preco']};{produto['quantidade']};{produto['categoria_id']}\n")
        return produto_encontrado