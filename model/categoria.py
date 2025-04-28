class Categoria:
    def __init__(self, nome: str, id: int):
        self.nome = nome
        self.id = id

    def __str__(self):
        return f"Categoria -> ID: {self.id} | Nome: {self.nome}"