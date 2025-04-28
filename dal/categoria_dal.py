import os
from model.categoria import Categoria


class CategoriaDal:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def add_categoria(self, categoria: Categoria):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        with open(os.path.join(self.DATA_DIR, "categorias.txt"), "a") as arquivo:
            arquivo.write(f"{categoria.nome};{categoria.id}\n")

    def listar_categorias(self):
        categorias = []
        try:
            with open(os.path.join(self.DATA_DIR, "categorias.txt"), "r") as arquivo:
                for linha in arquivo:
                    nome, id = linha.strip().split(";")
                    categorias.append({"nome": nome, "id": id})
        except FileNotFoundError:
            print("Arquivo categorias.txt não encontrado!")
        return categorias

    def buscar_categoria_id(self, id: int):
        categorias = self.listar_categorias()
        for categoria in categorias:
            if categoria["id"] == str(id):
                return categoria
        return None

    def editar_categoria(self, id: int, novo_nome: str):
        categorias = self.listar_categorias()
        categoria_encontrada = False
        for categoria in categorias:
            if categoria["id"] == str(id):
                categoria["nome"] = novo_nome
                categoria_encontrada = True
                break
        if categoria_encontrada:
            with open(os.path.join(self.DATA_DIR, "categorias.txt"), "w") as arquivo:
                for categoria in categorias:
                    arquivo.write(f"{categoria['nome']};{categoria['id']}\n")
        return categoria_encontrada

    def remover_categoria(self, id: int):
        categorias = self.listar_categorias()
        categoria_encontrada = False
        for categoria in categorias:
            if categoria["id"] == str(id):
                categorias.remove(categoria)
                categoria_encontrada = True
                break
        if categoria_encontrada:
            with open(os.path.join(self.DATA_DIR, "categorias.txt"), "w") as arquivo:
                for categoria in categorias:
                    arquivo.write(f"{categoria['nome']};{categoria['id']}\n")
        return categoria_encontrada