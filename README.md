# Dashboard de Vendas com Dash e Flask

Este projeto é um dashboard de vendas que utiliza a biblioteca Dash para visualizações de dados e Flask para o backend. Ele possui três seções principais: Produto X Loja, Loja X Faturamento e Curva ABC (Gráfico de Pareto), que exibem diferentes análises sobre os dados de vendas a partir de um arquivo Excel.

## Funcionalidades

- **Produto X Loja**: Exibe a quantidade de produtos vendidos por loja.
- **Loja X Faturamento**: Mostra o faturamento por produto e loja.
- **Curva ABC (Gráfico de Pareto)**: Apresenta a curva ABC de produtos, com base na quantidade vendida e o percentual cumulativo.

## Tecnologias Usadas

- **Python**: Linguagem de programação usada para construir o backend.
- **Flask**: Framework para desenvolvimento de aplicações web em Python.
- **Dash**: Framework para criar aplicações web interativas com gráficos.
- **Plotly**: Biblioteca para criação de gráficos interativos.
- **HTML/CSS**: Linguagens de marcação e estilo usadas para construir e estilizar a interface do usuário.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- 
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
## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

### Pré-requisitos

- **Python 3.x** instalado no seu sistema.
- **Virtualenv** (opcional, mas recomendado) para criar um ambiente virtual.
- **Git** (opcional) para clonar o repositório.

### Passos de Instalação

1. **Clone o Repositório**

    - Usando HTTPS:
     ```bash
     git clone https://github.com/htadmg/dashboard_com_dash.git
     ```
   - Usando SSH:
     ```bash
     git clone git@github.com:htadmg/dashboard_com_dash.git
     ```
   - Navegue até o diretório do projeto:
     ```bash
        cd .\dashboard_com_dash
     ```
   
3. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
    - **Para Linux/MacOS:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - **Para Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```   
3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt

