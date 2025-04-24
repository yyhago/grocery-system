class CategoriaDal:

    def add_categoria(self, categoria):
        with open("./data/categorias.txt", "a") as arquivo:
            arquivo.write(f"{categoria.nome};{categoria.id}\n")

    def listar_categorias(self):
        categorias = []
        with open("./data/categorias.txt", "r") as arquivo:
            for linha in arquivo:
                nome, id = linha.strip().split(";")
                categorias.append({"nome": nome, "id": id})
        return categorias
    
    def buscar_categoria_id(self, id):
        categorias = self.listar_categorias()
        for categoria in categorias:
            if categoria["id"] == id:
                return categoria
        return None
    
    def editar_categoria(self, id, novo_nome):
        categorias = self.listar_categorias()
        categoria_encontrada = False
        for categoria in categorias:
            if categoria["id"] == id:
                categoria["nome"] = novo_nome
                categoria_encontrada = True
                break
        if categoria_encontrada:
            with open("./data/categorias.txt", "w") as arquivo:
                for categoria in categorias:
                    arquivo.write(f"{categoria['nome']};{categoria['id']}\n")
        return categoria_encontrada
    
    def remover_categoria(self, id):
        categorias = self.listar_categorias()
        categoria_encontrada = False
        for categoria in categorias:
            if categoria["id"] == id:
                categorias.remove(categoria)
                categoria_encontrada = True
                break
        if categoria_encontrada:
            with open("./data/categorias.txt", "w") as arquivo:
                for categoria in categorias:
                    arquivo.write(f"{categoria['nome']};{categoria['id']}\n")
        return categoria_encontrada