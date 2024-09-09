from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px
from flask import Flask

df = pd.read_excel("Vendas.xlsx")
def init_dashboard(app):

    fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

    opcoes = list(df['ID Loja'].unique())
    opcoes.append("Todas as Lojas")

    app.layout = html.Div(children=[
        html.H6('Produto X Loja'),
        dcc.Dropdown(opcoes, value="Todas as Lojas", id='lista_lojas'),

        dcc.Graph(
            id='grafico_quantidade_vendas',
            figure=fig
        )
    ])

    @app.callback(
        Output('grafico_quantidade_vendas', 'figure'),
        Input('lista_lojas', 'value')
    )
    def update_output(value):
        if value == "Todas as Lojas":
            fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        else:
            tabela_filtrada = df.loc[df['ID Loja'] == value]
            fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        return fig
