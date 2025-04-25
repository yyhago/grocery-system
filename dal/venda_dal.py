from model.venda import Venda

class VendaDal:
    def add_venda(self, venda: Venda):
        with open("./data/vendas.txt", "a") as arquivo:
            arquivo.write(f"{venda.id};{venda.produto_id};{venda.quantidade};{venda.preco_unitario};{venda.total};{venda.data};{venda.cliente_id}\n")

    def listar_vendas(self):
        vendas = []        
        try:
            with open("./data/vendas.txt", "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) == 7:
                        vendas.append({
                            "id": dados[0],
                            "produto_id": dados[1],
                            "quantidade": dados[2],
                            "preco_unitario": dados[3],
                            "total": dados[4],
                            "data": dados[5],
                            "cliente_id": dados[6]
                        })
        except FileNotFoundError:
            pass
        return vendas
    
    def buscar_venda_id(self, id):
        vendas = self.listar_vendas()
        for venda in vendas:
            if venda["id"] == str(id):
                return venda
        return None
    
    def editar_venda(self, id, nova_quantidade, novo_preco_unitario, novo_total):
        vendas = self.listar_vendas()
        venda_encontrada = False
        for venda in vendas:
            if venda["id"] == str(id):
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
            if venda["id"] == str(id):
                vendas.remove(venda)
                venda_encontrada = True
                break
        if venda_encontrada:
            with open("./data/vendas.txt", "w") as arquivo:
                for venda in vendas:
                    arquivo.write(f"{venda['id']};{venda['produto_id']};{venda['quantidade']};{venda['preco_unitario']};{venda['total']};{venda['data']};{venda['cliente_id']}\n")
        return venda_encontrada