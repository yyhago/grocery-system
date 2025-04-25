import sys
import os

# Adiciona o diretório pai ao sys.path para importar os módulos corretamente, sem erros
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.categoria_controller import CategoriaController
from controller.produto_controller import ProdutoController
from controller.venda_controller import VendaController
from controller.cliente_controller import ClienteController
from controller.fornecedor_controller import FornecedorController
from controller.funcionario_controller import FuncionarioController

def mostrar_linha():
    print("=" * 50)

while True:
    mostrar_linha()
    print("MENU PRINCIPAL | SISTEMA DE MERCEARIA".center(50))
    mostrar_linha()
    
    print("\n1 - Sistema de Vendas")
    print("2 - Sistema de Produtos")
    print("3 - Sistema de Categorias")
    print("4 - Sistema de Fornecedores")
    print("5 - Sistema de Funcionários")
    print("6 - Sistema de Clientes")
    print("7 - Sair do sistema\n")
    
    opcao = input("Digite a opção desejada: ")
    mostrar_linha()

    # Sistema de Vendas
    if opcao == "1":
        while True:
            print("\nSISTEMA DE VENDAS")
            mostrar_linha()
            print("1 - Criar Venda")
            print("2 - Listar Vendas")
            print("3 - Buscar Venda por ID")
            print("4 - Atualizar Venda")
            print("5 - Deletar Venda")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVA VENDA:")
                    id = int(input("ID da Venda: "))
                    produto_id = int(input("ID do Produto: "))
                    quantidade = int(input("Quantidade: "))
                    preco_unitario = float(input("Preço Unitário: "))
                    total = float(input("Total: "))
                    data = input("Data (dd/mm/aaaa): ")
                    cliente_id = int(input("ID do Cliente: "))
                    
                    if VendaController.criar_venda(id, produto_id, quantidade, 
                                                 preco_unitario, total, data, cliente_id):
                        print("\nVenda registrada com sucesso!")
                    else:
                        print("\nErro ao registrar venda!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "2":
                vendas = VendaController.listar_vendas()
                print("\nLISTA DE VENDAS:")
                for venda in vendas:
                    print(f"ID: {venda['id']} | Data: {venda['data']} | Total: R${venda['total']}")

            elif sub_opcao == "3":
                try:
                    id = int(input("ID da Venda: "))
                    venda = VendaController.buscar_venda_id(id)
                    if venda:
                        print(f"\nVenda encontrada:\n{venda}")
                    else:
                        print("\nVenda não encontrada!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "4":
                try:
                    id = int(input("ID da Venda: "))
                    nova_quantidade = int(input("Nova Quantidade: "))
                    novo_preco = float(input("Novo Preço Unitário: "))
                    novo_total = float(input("Novo Total: "))
                    
                    if VendaController.atualizar_venda(id, nova_quantidade, 
                                                     novo_preco, novo_total):
                        print("\nVenda atualizada com sucesso!")
                    else:
                        print("\nErro ao atualizar venda!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "5":
                try:
                    id = int(input("ID da Venda: "))
                    if VendaController.deletar_venda(id):
                        print("\nVenda deletada com sucesso!")
                    else:
                        print("\nErro ao deletar venda!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    # Sistema de Produtos
    elif opcao == "2":
        while True:
            print("\nSISTEMA DE PRODUTOS")
            mostrar_linha()
            print("1 - Criar Produto")
            print("2 - Listar Produtos")
            print("3 - Buscar Produto por ID")
            print("4 - Atualizar Produto")
            print("5 - Deletar Produto")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVO PRODUTO:")
                    id = int(input("ID: "))
                    nome = input("Nome: ")
                    preco = float(input("Preço: "))
                    quantidade = int(input("Quantidade: "))
                    categoria_id = int(input("ID da Categoria: "))
                    
                    if ProdutoController.cadastrar_produto(nome, id, preco, 
                                                         quantidade, categoria_id):
                        print("\nProduto criado com sucesso!")
                    else:
                        print("\nErro ao criar produto!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "2":
                produtos = ProdutoController.listar_produtos()
                print("\nLISTA DE PRODUTOS:")
                for produto in produtos:
                    print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R${produto['preco']}")

            elif sub_opcao == "3":
                try:
                    id = int(input("ID do Produto: "))
                    produto = ProdutoController.buscar_produto_id(id)
                    if produto:
                        print(f"\nProduto encontrado:\n{produto}")
                    else:
                        print("\nProduto não encontrado!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "4":
                try:
                    id = int(input("ID do Produto: "))
                    novo_nome = input("Novo Nome: ")
                    novo_preco = float(input("Novo Preço: "))
                    nova_quantidade = int(input("Nova Quantidade: "))
                    
                    if ProdutoController.editar_produto(id, novo_nome, 
                                                      novo_preco, nova_quantidade):
                        print("\nProduto atualizado com sucesso!")
                    else:
                        print("\nErro ao atualizar produto!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "5":
                try:
                    id = int(input("ID do Produto: "))
                    if ProdutoController.remover_produto(id):
                        print("\nProduto deletado com sucesso!")
                    else:
                        print("\nErro ao deletar produto!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    # Sistema de Categorias
    elif opcao == "3":
        while True:
            print("\nSISTEMA DE CATEGORIAS")
            mostrar_linha()
            print("1 - Criar Categoria")
            print("2 - Listar Categorias")
            print("3 - Buscar Categoria por ID")
            print("4 - Atualizar Categoria")
            print("5 - Deletar Categoria")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVA CATEGORIA:")
                    id = int(input("ID: "))
                    nome = input("Nome: ")
                    
                    if CategoriaController.cadastrar_categoria(nome, id):
                        print("\nCategoria criada com sucesso!")
                    else:
                        print("\nErro ao criar categoria!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "2":
                categorias = CategoriaController.listar_categorias()
                print("\nLISTA DE CATEGORIAS:")
                for categoria in categorias:
                    print(f"ID: {categoria['id']} | Nome: {categoria['nome']}")

            elif sub_opcao == "3":
                try:
                    id = int(input("ID da Categoria: "))
                    categoria = CategoriaController.buscar_categoria_id(id)
                    if categoria:
                        print(f"\nCategoria encontrada:\n{categoria}")
                    else:
                        print("\nCategoria não encontrada!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "4":
                try:
                    id = int(input("ID da Categoria: "))
                    novo_nome = input("Novo Nome: ")
                    
                    if CategoriaController.editar_categoria(id, novo_nome):
                        print("\nCategoria atualizada com sucesso!")
                    else:
                        print("\nErro ao atualizar categoria!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "5":
                try:
                    id = int(input("ID da Categoria: "))
                    if CategoriaController.remover_categoria(id):
                        print("\nCategoria deletada com sucesso!")
                    else:
                        print("\nErro ao deletar categoria!")
                except ValueError:
                    print("\nID inválido!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    # Sistema de Fornecedores
    elif opcao == "4":
        while True:
            print("\nSISTEMA DE FORNECEDORES")
            mostrar_linha()
            print("1 - Criar Fornecedor")
            print("2 - Listar Fornecedores")
            print("3 - Buscar Fornecedor por CPF")
            print("4 - Atualizar Fornecedor")
            print("5 - Deletar Fornecedor")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVO FORNECEDOR:")
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    cpf = input("CPF (11 dígitos): ")
                    
                    if FornecedorController.cadastrar_fornecedor(nome, idade, cpf):
                        print("\nFornecedor criado com sucesso!")
                    else:
                        print("\nErro ao criar fornecedor!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "2":
                fornecedores = FornecedorController.listar_fornecedores()
                print("\nLISTA DE FORNECEDORES:")
                for fornecedor in fornecedores:
                    print(f"Nome: {fornecedor['nome']} | CPF: {fornecedor['cpf']}")

            elif sub_opcao == "3":
                cpf = input("CPF do Fornecedor: ")
                fornecedor = FornecedorController.buscar_fornecedor_cpf(cpf)
                if fornecedor:
                    print(f"\nFornecedor encontrado:\n{fornecedor}")
                else:
                    print("\nFornecedor não encontrado!")

            elif sub_opcao == "4":
                try:
                    cpf = input("CPF do Fornecedor: ")
                    novo_nome = input("Novo Nome: ")
                    nova_idade = int(input("Nova Idade: "))
                    novo_cpf = input("Novo CPF: ")
                    
                    if FornecedorController.editar_fornecedor(cpf, novo_nome, 
                                                            nova_idade, novo_cpf):
                        print("\nFornecedor atualizado com sucesso!")
                    else:
                        print("\nErro ao atualizar fornecedor!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "5":
                cpf = input("CPF do Fornecedor: ")
                if FornecedorController.remover_fornecedor(cpf):
                    print("\nFornecedor deletado com sucesso!")
                else:
                    print("\nErro ao deletar fornecedor!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    # Sistema de Funcionários
    elif opcao == "5":
        while True:
            print("\nSISTEMA DE FUNCIONÁRIOS")
            mostrar_linha()
            print("1 - Criar Funcionário")
            print("2 - Listar Funcionários")
            print("3 - Buscar Funcionário por CPF")
            print("4 - Atualizar Funcionário")
            print("5 - Deletar Funcionário")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVO FUNCIONÁRIO:")
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    cpf = input("CPF (11 dígitos): ")
                    total_vendas = float(input("Total de Vendas: "))
                    
                    if FuncionarioController.cadastrar_funcionario(nome, idade, 
                                                                  cpf, total_vendas):
                        print("\nFuncionário criado com sucesso!")
                    else:
                        print("\nErro ao criar funcionário!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "2":
                funcionarios = FuncionarioController.listar_funcionarios()
                print("\nLISTA DE FUNCIONÁRIOS:")
                for funcionario in funcionarios:
                    print(f"Nome: {funcionario['nome']} | Vendas: R${funcionario['total_vendas']}")

            elif sub_opcao == "3":
                cpf = input("CPF do Funcionário: ")
                funcionario = FuncionarioController.buscar_funcionario_cpf(cpf)
                if funcionario:
                    print(f"\nFuncionário encontrado:\n{funcionario}")
                else:
                    print("\nFuncionário não encontrado!")

            elif sub_opcao == "4":
                try:
                    cpf = input("CPF do Funcionário: ")
                    novo_nome = input("Novo Nome: ")
                    nova_idade = int(input("Nova Idade: "))
                    novo_total = float(input("Novo Total de Vendas: "))
                    
                    if FuncionarioController.editar_funcionario(cpf, novo_nome, 
                                                              nova_idade, novo_total):
                        print("\nFuncionário atualizado com sucesso!")
                    else:
                        print("\nErro ao atualizar funcionário!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "5":
                cpf = input("CPF do Funcionário: ")
                if FuncionarioController.remover_funcionario(cpf):
                    print("\nFuncionário deletado com sucesso!")
                else:
                    print("\nErro ao deletar funcionário!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    # Sistema de Clientes
    elif opcao == "6":
        while True:
            print("\nSISTEMA DE CLIENTES")
            mostrar_linha()
            print("1 - Criar Cliente")
            print("2 - Listar Clientes")
            print("3 - Buscar Cliente por CPF")
            print("4 - Atualizar Cliente")
            print("5 - Deletar Cliente")
            print("6 - Voltar\n")
            
            sub_opcao = input("Opção: ")
            mostrar_linha()

            if sub_opcao == "1":
                try:
                    print("NOVO CLIENTE:")
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    cpf = input("CPF (11 dígitos): ")
                    
                    if ClienteController.cadastrar_cliente(nome, idade, cpf):
                        print("\nCliente criado com sucesso!")
                    else:
                        print("\nErro ao criar cliente!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "2":
                clientes = ClienteController.listar_clientes()
                print("\nLISTA DE CLIENTES:")
                for cliente in clientes:
                    print(f"Nome: {cliente['nome']} | CPF: {cliente['cpf']}")

            elif sub_opcao == "3":
                cpf = input("CPF do Cliente: ")
                cliente = ClienteController.buscar_cliente_cpf(cpf)
                if cliente:
                    print(f"\nCliente encontrado:\n{cliente}")
                else:
                    print("\nCliente não encontrado!")

            elif sub_opcao == "4":
                try:
                    cpf = input("CPF do Cliente: ")
                    novo_nome = input("Novo Nome: ")
                    nova_idade = int(input("Nova Idade: "))
                    
                    if ClienteController.editar_cliente(cpf, novo_nome, nova_idade):
                        print("\nCliente atualizado com sucesso!")
                    else:
                        print("\nErro ao atualizar cliente!")
                except ValueError:
                    print("\nValores inválidos!")

            elif sub_opcao == "5":
                cpf = input("CPF do Cliente: ")
                if ClienteController.remover_cliente(cpf):
                    print("\nCliente deletado com sucesso!")
                else:
                    print("\nErro ao deletar cliente!")

            elif sub_opcao == "6":
                break

            else:
                print("Opção inválida!")
            mostrar_linha()

    elif opcao == "7":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")

    