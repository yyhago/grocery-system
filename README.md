# Sistema de Gestão de Mercearia

Um sistema abrangente de gestão construido em Python, projetado para gerenciar estoque, vendas, funcionários e gerar relatórios.

## Visão Geral

Este projeto é uma aplicação de estudo pessoal que visa criar uma solução completa de gestão de supermercados. O sistema gerencia vários aspectos de um negócio de supermercados, incluindo estoque de produtos, transações de vendas, relacionamento com clientes e gestão de funcionários.

## Recursos

### Gerenciamento de Entidades
- **Gerenciamento de Categorias**
- Adicionar/Editar/Excluir categorias de produtos
- Organizar produtos por categoria

- **Gerenciamento de Produtos**
- Adicionar/Editar/Excluir produtos
- Atribuir produtos a categorias
- Acompanhar os níveis de estoque

- **Gerenciamento de Fornecedores**
- Adicionar/Editar/Excluir fornecedores
- Acompanhar informações e produtos de fornecedores

- **Gerenciamento de Clientes**
- Adicionar/Editar/Excluir registros de clientes
- Acompanhar o histórico de compras dos clientes

- **Gerenciamento de Funcionários**
- Adicionar/Editar/Excluir informações de funcionários
- Gerenciar acessos e funções de funcionários

### Sistema de Ponto de Venda
- Processar transações de clientes
- Calcular totais com impostos
- Aplicar descontos
- Gerenciar devoluções de produtos

### Relatórios
- **Relatório Geral de Vendas**
- Visão geral de todas as transações de vendas
- Métricas de receita total

- **Relatório de Vendas por Data**
- Filtrar dados de vendas por datas ou intervalos de datas específicos
- Desempenho de vendas diário/semanal/mensal

- **Produtos Mais Vendidos Relatório**
- Produtos classificados por volume de vendas
- Produtos mais rentáveis

- **Relatório de Principais Clientes**
- Clientes classificados por volume de compras
- Análise da frequência de compra dos clientes

## Pilha de Tecnologia

- **Backend**: Python
- **Banco de Dados**: .txt

## Instalação

```bash
# Clonar o repositório
git clone https://github.com/yyhago/grocery-system.git

# Navegar até o diretório do projeto
cd grocery-system
```

## Estrutura do Projeto

```
MercadoManager/
│
├── controller/
│ ├── categoria_controller.py
│ ├── produto_controller.py
│ ├── fornecedor_controller.py
│ ├── cliente_controller.py
│ ├── funcionario_controller.py
│ └── caixa_controller.py
│
├── modelo/
│ ├── categoria.py
│ ├── produto.py
│ ├── fornecedor.py
│ ├── cliente.py
│ ├── funcionario.py
│ └── venda.py
│
├── dal/
│ ├── categoria_dal.py
│ ├── produto_dal.py
│ ├── fornecedor_dal.py
│ ├── cliente_dal.py
│ ├── funcionario_dal.py
│ └── venda_dal.py
│
├── visualizar/
│ └── menu_principal.py
│
├── dados/
│ ├── categorias.txt
│ ├── produtos.txt
│ ├── fornecedores.txt
│ ├── clientes.txt
│ ├── funcionarios.txt
│ └── vendas.txt
│
├── relatórios/
│ ├── relatorio_vendas.py
│ ├── relatorio_produtos.py
│ └── relatorio_clientes.py
│
├── README.md
└── main.py
```

## Contribuindo

Este é um projeto de estudo pessoal. Sinta-se à vontade para criar um fork e adaptá-lo para seus próprios propósitos de aprendizado.
