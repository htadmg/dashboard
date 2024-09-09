from dash import Dash, html, dcc, Output, Input
from flask import Flask, render_template
from dashboards import produto_loja

server = Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/dash/')
produto_loja.init_dashboard(app)

@server.route('/')
def index():
    return render_template('produto_loja.html')

@server.route('/produto_loja')
def produto_loja_page():
    return render_template('produto_loja.html')

if __name__ == '__main__':
    server.run(debug=True)