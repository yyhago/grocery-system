from dal.categoria_dal import CategoriaDal
from model.categoria import Categoria

class CategoriaController:
    @classmethod
    def cadastrar_categoria(cls, nome: str, id: int):
        if len(nome) > 2:
            try:
                categoria = Categoria(nome, id)
                categoria_dal = CategoriaDal()
                categoria_dal.add_categoria(categoria)
                return True
            except Exception as e:
                print(f"Erro ao cadastrar categoria: {e}")
                return False
        else:
            print("Nome da categoria deve ter mais de 2 caracteres")
            return False
        
    @classmethod
    def listar_categorias(cls):
        categoria_dal = CategoriaDal()
        return categoria_dal.listar_categorias()
    
    @classmethod
    def buscar_categoria_id(cls, id: int):
        categoria_dal = CategoriaDal()
        return categoria_dal.buscar_categoria_id(id)
    
    @classmethod
    def editar_categoria(cls, id: int, novo_nome: str):
        categoria_dal = CategoriaDal()
        return categoria_dal.editar_categoria(id, novo_nome)
    
    @classmethod
    def remover_categoria(cls, id: int):
        categoria_dal = CategoriaDal()
        return categoria_dal.remover_categoria(id)