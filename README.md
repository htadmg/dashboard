# Dashboard de Vendas com Dash e Flask

Este projeto é um dashboard de vendas que utiliza a biblioteca Dash para visualizações de dados e Flask para o backend. Ele possui três seções principais: Produto X Loja, Loja X Faturamento e Curva ABC (Gráfico de Pareto), que exibem diferentes análises sobre os dados de vendas a partir de um arquivo Excel.

## Funcionalidades

- **Produto X Loja**: Exibe a quantidade de produtos vendidos por loja.
- **Loja X Faturamento**: Mostra o faturamento por produto e loja.
- **Curva ABC (Gráfico de Pareto)**: Apresenta a curva ABC de produtos, com base na quantidade vendida e o percentual cumulativo.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:
```
├── main.py                   # Arquivo principal contendo o servidor Flask
├── dashboards/
│   ├── produto_loja.py       # Módulo para o gráfico Produto X Loja
│   ├── loja_faturamento.py   # Módulo para o gráfico Loja X Faturamento
│   └── curva_abc.py          # Módulo para o gráfico Curva ABC (Pareto)
├── templates/
│   ├── base.html             # Template base HTML
│   ├── produto_loja.html     # Template da página Produto X Loja
│   ├── loja_faturamento.html # Template da página Loja X Faturamento
│   └── curva_abc.html        # Template da página Curva ABC
├── static/
│   ├── styles/
│   │   └── principal.css     # Estilos CSS
├── Vendas.xlsx               # Arquivo Excel com dados de vendas
└── requirements.txt          # Dependências do projeto
```

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias estão listadas no arquivo `requirements.txt`

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Como Executar

1. Coloque o arquivo Vendas.xlsx na raiz do projeto.
2. Execute o servidor Flask:

```bash
  python app.py
```
3. Acesse o dashboard no navegador:

```bash
 http://127.0.0.1:5000/
```
