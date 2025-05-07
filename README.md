# 🛒 Sistema de Gestão de Mercearia

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

Um sistema completo de gestão de mercearia desenvolvido em **Python puro**, implementando o padrão de arquitetura MVC (Model-View-Controller) e utilizando arquivos `.txt` como base de dados para fins de estudo e aprendizado.

## 📋 Visão Geral

Este projeto é um estudo pessoal focado na implementação de um sistema de gestão de mercearia com arquitetura limpa e bem estruturada. O objetivo principal foi aplicar conceitos de programação orientada a objetos, padrões de projeto, organização de código, e treinar a lógica, sem depender de frameworks ou bancos de dados complexos.

### 🎯 Objetivos de Aprendizado
- Implementar uma arquitetura MVC completa em Python
- Desenvolver um CRUD funcional utilizando arquivos `.txt` como persistência de dados
- Praticar separação de responsabilidades entre camadas do sistema
- Aplicar boas práticas de desenvolvimento de software

## ⚙️ Características Principais

### 📦 Gerenciamento de Entidades

#### Categorias
- Criar, visualizar, atualizar e excluir categorias
- Organização de produtos por categorias específicas

#### Produtos
- Gerenciamento completo do catálogo de produtos
- Controle de estoque com alertas de níveis baixos
- Associação com categorias e fornecedores

#### Fornecedores
- Cadastro e manutenção de fornecedores
- Associação de produtos com seus respectivos fornecedores
- Histórico de entregas e informações de contato

#### Clientes
- Gestão de cadastro de clientes
- Histórico de compras por cliente
- Sistema de fidelidade (pontuação)

#### Funcionários
- Controle de acesso ao sistema
- Níveis de permissão por função
- Registro de operações realizadas

### 💵 Sistema de Ponto de Venda (PDV)
- Interface intuitiva para processar vendas
- Cálculo automático de preços, impostos e descontos
- Gestão de devoluções e trocas

### 📊 Relatórios Gerenciais
- Vendas por período (diário/semanal/mensal)
- Produtos mais vendidos e mais rentáveis
- Desempenho de vendas por categoria
- Análise de clientes e comportamento de compra

## 🏗️ Arquitetura MVC

O sistema segue rigorosamente o padrão arquitetural MVC, com adição de uma camada DAL (Data Access Layer):

- **Model**: Definição das entidades de negócio e suas regras
- **View**: Interface com o usuário via terminal
- **Controller**: Coordenação entre Model e View, processamento de lógica de negócio
- **DAL**: Camada de acesso aos dados armazenados nos arquivos `.txt`

## 📁 Estrutura do Projeto

```
grocery-system/
│
├── controller/              # Controladores para lógica de negócio
│   ├── categoria_controller.py
│   ├── produto_controller.py
│   ├── fornecedor_controller.py
│   ├── cliente_controller.py
│   ├── funcionario_controller.py
│   └── caixa_controller.py
│
├── model/                   # Definição das entidades e regras
│   ├── categoria.py
│   ├── produto.py
│   ├── fornecedor.py
│   ├── cliente.py
│   ├── funcionario.py
│   └── venda.py
│
├── dal/                     # Camada de acesso a dados
│   ├── categoria_dal.py
│   ├── produto_dal.py
│   ├── fornecedor_dal.py
│   ├── cliente_dal.py
│   ├── funcionario_dal.py
│   └── venda_dal.py
│
├── view/                    # Interface com usuário
│   └── menu_principal.py    # Ponto de entrada da aplicação
│
├── data/                    # Armazenamento em arquivos .txt
│   ├── categorias.txt
│   ├── produtos.txt
│   ├── fornecedores.txt
│   ├── clientes.txt
│   ├── funcionarios.txt
│   └── vendas.txt
│
├── reports/                 # Geração de relatórios
│   ├── relatorio_vendas.py
│   ├── relatorio_produtos.py
│   └── relatorio_clientes.py
│
├── README.md
```

## 💾 Armazenamento de Dados

Em vez de utilizar um SGBD tradicional, este projeto emprega **arquivos `.txt`** como mecanismo de persistência para fins de estudo:

- Cada entidade possui seu próprio arquivo de armazenamento
- Implementação de operações CRUD diretamente nos arquivos
- Operações atômicas para garantir integridade dos dados
- Serialização e deserialização de objetos para texto

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/yyhago/grocery-system.git

# Navegue até o diretório do projeto
cd grocery-system

# Execute o sistema
python main.py
```

## 📝 Aprendizados e Considerações

Este projeto foi desenvolvido com propósito educacional e demonstra:

- **Aplicação prática de padrões de design**: MVC implementado em Python puro
- **Persistência sem frameworks**: Manipulação direta de arquivos como alternativa a ORMs
- **Separação de responsabilidades**: Código organizado em camadas distintas
- **Programação orientada a objetos**: Uso de classes, herança e encapsulamento

Para um ambiente de produção real, seria recomendável utilizar um banco de dados relacional ou NoSQL para maior escalabilidade, segurança e performance.

## 📜 Licença

Este projeto é um estudo pessoal e está disponível para qualquer pessoa que deseje aprender sobre desenvolvimento de sistemas em Python e padrões de arquitetura de software.
