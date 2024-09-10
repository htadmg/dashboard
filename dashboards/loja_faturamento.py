from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px
from flask import Flask

df = pd.read_excel("Vendas.xlsx")

# Agrupar os dados por Produto e somar os valores de "Valor Final"
df_agrupado = df.groupby(['Produto', 'ID Loja'], as_index=False)['Valor Final'].sum()


def init_faturamento(app):
    fig = px.bar(df_agrupado, x="Produto", y="Valor Final", color="ID Loja", barmode="group", text_auto=True)

    # Configurar a exibição do texto no gráfico
    fig.update_traces(textposition='outside')

    opcoes = list(df['ID Loja'].unique())
    opcoes.append("Todas as Lojas")

    app.layout = html.Div(children=[
        html.H6('Faturamento X Loja'),
        dcc.Dropdown(opcoes, value="Todas as Lojas", id='lista_lojas_faturamento', clearable=True),
        dcc.Graph(
            id='grafico_faturamento_vendas',
            figure=fig
        )
    ])

    @app.callback(
        Output('lista_lojas_faturamento', 'value'),
        Input('lista_lojas_faturamento', 'value')
    )
    def update_dropdown(value):
        if value is None:
            return "Todas as Lojas"
        return value

    @app.callback(
        Output('grafico_faturamento_vendas', 'figure'),
        Input('lista_lojas_faturamento', 'value')
    )
    def update_output(value):
        if value == "Todas as Lojas":
            fig = px.bar(df_agrupado, x="Produto", y="Valor Final", color="ID Loja", barmode="group", text_auto=True)
        else:
            tabela_filtrada = df_agrupado.loc[df_agrupado['ID Loja'] == value]
            fig = px.bar(tabela_filtrada, x="Produto", y="Valor Final", color="ID Loja", barmode="group",
                         text_auto=True)

        # Atualizar o gráfico para exibir o texto com o valor total
        fig.update_traces(textposition='outside')
        return fig
