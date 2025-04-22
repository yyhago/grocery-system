# Grocery Management System

A comprehensive Python-based grocery store management system designed for managing inventory, sales, employees, and generating reports.

## Overview

This project is a personal study application that aims to create a complete grocery store management solution. The system manages various aspects of a grocery business including product inventory, sales transactions, customer relationships, and employee management.

## Features

### Entity Management
- **Category Management**
  - Add/Edit/Delete product categories
  - Organize products by category

- **Product Management**
  - Add/Edit/Delete products
  - Assign products to categories
  - Track inventory levels

- **Supplier Management**
  - Add/Edit/Delete suppliers
  - Track supplier information and products

- **Customer Management**
  - Add/Edit/Delete customer records
  - Track customer purchase history

- **Employee Management**
  - Add/Edit/Delete employee information
  - Manage employee access and roles

### Point of Sale System
- Process customer transactions
- Calculate totals with taxes
- Apply discounts
- Handle product returns

### Reporting
- **General Sales Report**
  - Overview of all sales transactions
  - Total revenue metrics

- **Sales by Date Report**
  - Filter sales data by specific dates or date ranges
  - Daily/Weekly/Monthly sales performance

- **Best-Selling Products Report**
  - Products ranked by sales volume
  - Most profitable products

- **Top Customers Report**
  - Customers ranked by purchase volume
  - Customer purchase frequency analysis

## Technology Stack

- **Backend**: Python
- **Database**: .txt

## Installation

```bash
# Clone the repository
git clone https://github.com/yyhago/grocery-system.git

# Navigate to the project directory
cd grocery-system
```

## Project Structure

```
MercadoManager/
│
├── controller/
│   ├── categoria_controller.py
│   ├── produto_controller.py
│   ├── fornecedor_controller.py
│   ├── cliente_controller.py
│   ├── funcionario_controller.py
│   └── caixa_controller.py
│
├── model/
│   ├── categoria.py
│   ├── produto.py
│   ├── fornecedor.py
│   ├── cliente.py
│   ├── funcionario.py
│   └── venda.py
│
├── dal/
│   ├── categoria_dal.py
│   ├── produto_dal.py
│   ├── fornecedor_dal.py
│   ├── cliente_dal.py
│   ├── funcionario_dal.py
│   └── venda_dal.py
│
├── view/
│   └── menu_principal.py
│
├── data/
│   ├── categorias.txt
│   ├── produtos.txt
│   ├── fornecedores.txt
│   ├── clientes.txt
│   ├── funcionarios.txt
│   └── vendas.txt
│
├── reports/
│   ├── relatorio_vendas.py
│   ├── relatorio_produtos.py
│   └── relatorio_clientes.py
│
├── README.md
└── main.py
```

## Contributing

This is a personal study project. Feel free to fork and adapt for your own learning purposes.