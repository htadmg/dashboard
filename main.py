from dash import Dash, html, dcc, Output, Input
from flask import Flask, render_template
from dashboards import produto_loja, loja_faturamento, curva_abc

server = Flask(__name__)
app_produto = Dash(__name__, server=server, url_base_pathname='/dash/produto_loja/')
app_faturamento = Dash(__name__, server=server, url_base_pathname='/dash/loja_faturamento/')
app_curva = Dash(__name__, server=server, url_base_pathname='/dash/curva_abc/')
produto_loja.init_produto(app_produto)
loja_faturamento.init_faturamento(app_faturamento)
curva_abc.init_curva(app_curva)
@server.route('/')
def index():
    return render_template('produto_loja.html')

@server.route('/produto_loja')
def produto_loja_page():
    return render_template('produto_loja.html')

@server.route('/loja_faturamento')
def loja_faturamento_page():
    return render_template('loja_faturamento.html')

@server.route('/curva_abc')
def curva_abc_page():
    return render_template('curva_abc.html')

if __name__ == '__main__':
    server.run(debug=True)