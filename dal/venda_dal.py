class VendaDal:
    
    def add_venda(self, venda):
        with open("./data/vendas.txt", "a") as arquivo:
            arquivo.write(f"{venda.id};{venda.produto_id};{venda.quantidade};{venda.preco_unitario};{venda.total};{venda.data};{venda.cliente_id}\n")

    def listar_vendas(self):
        vendas = []        
        with open("./data/vendas.txt", "r") as arquivo:
            for linha in arquivo:
                id, produto_id, quantidade, preco_unitario, total, data, cliente_id = linha.strip().split(";")
                vendas.append({"id": id, "produto_id": produto_id, "quantidade": quantidade, "preco_unitario": preco_unitario, "total": total, "data": data, "cliente_id": cliente_id})
        return vendas
    
    def buscar_venda_id(self, id):
        vendas = self.listar_vendas()
        for venda in vendas:
            if venda["id"] == id:
                return venda
        return None
    
    def editar_venda(self, id, nova_quantidade, novo_preco_unitario, novo_total):
        vendas = self.listar_vendas()
        venda_encontrada = False
        for venda in vendas:
            if venda["id"] == id:
                venda["quantidade"] = nova_quantidade
                venda["preco_unitario"] = novo_preco_unitario
                venda["total"] = novo_total
                venda_encontrada = True
                break
        if venda_encontrada:
            with open("./data/vendas.txt", "w") as arquivo:
                for venda in vendas:
                    arquivo.write(f"{venda['id']};{venda['produto_id']};{venda['quantidade']};{venda['preco_unitario']};{venda['total']};{venda['data']};{venda['cliente_id']}\n")
        return venda_encontrada
    
    def remover_venda(self, id):
        vendas = self.listar_vendas()
        venda_encontrada = False
        for venda in vendas:
            if venda["id"] == id:
                vendas.remove(venda)
                venda_encontrada = True
                break
        if venda_encontrada:
            with open("./data/vendas.txt", "w") as arquivo:
                for venda in vendas:
                    arquivo.write(f"{venda['id']};{venda['produto_id']};{venda['quantidade']};{venda['preco_unitario']};{venda['total']};{venda['data']};{venda['cliente_id']}\n")
        return venda_encontrada