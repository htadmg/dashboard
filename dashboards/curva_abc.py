

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, Output, Input

# Função para construir o DataFrame


def build_dataframe(name_dataframe, col):
    dataframe = pd.read_excel(name_dataframe)
    grp = dataframe.groupby([col])[col].count()
    df = pd.DataFrame(grp)
    df.index.name = ''
    df = df.sort_values(by=[col], ascending=False)
    count = dataframe[col].value_counts().rename(f'{col}_count')
    percentage = dataframe[col].value_counts(normalize=True).rename(f'{col}_percentage')
    df = pd.concat([count, percentage], axis=1)
    return df


# Função para calcular a porcentagem cumulativa
def cumulative(dataframe, col):
    df = dataframe.copy()
    names_group = list(df.index)
    df['cumulative'] = 0
    iter_n = 0
    for n, name in enumerate(names_group):
        if n == 0:
            df.loc[name, ['cumulative']] = df.loc[names_group[n], [f'{col}_percentage']][0]
        else:
            df.loc[name, ['cumulative']] = df.loc[names_group[iter_n], ['cumulative']][0] + df.loc[names_group[n], [f'{col}_percentage']][0]
            iter_n += 1
    df['cumulative'] = df['cumulative'] * 100
    return df


df_agrupado = build_dataframe('Vendas.xlsx', 'Produto')
df_agrupado = cumulative(df_agrupado, 'Produto')


# Inicializar o Dash app
app = Dash(__name__)


# Função para criar o layout do gráfico de Pareto
def init_curva(app):
    fig = go.Figure()

    # Adicionar as barras de quantidade
    fig.add_trace(go.Bar(
        x=df_agrupado.index,
        y=df_agrupado['Produto_count'],
        name='Quantidade',
        marker_color='blue',
        text=df_agrupado['Produto_count'],
        textposition='auto'
    ))

    # Adicionar a linha de percentual cumulativo
    fig.add_trace(go.Scatter(
        x=df_agrupado.index,
        y=df_agrupado['cumulative'],
        name='Percentual Cumulativo',
        yaxis='y2',
        mode='lines+markers',
        marker=dict(color='red'),
        line=dict(shape='linear')
    ))

    # Atualizar o layout para incluir um segundo eixo Y para o percentual
    fig.update_layout(
        title='Curva ABC - Gráfico de Pareto',
        xaxis_title='Produto',
        yaxis_title='Quantidade',
        yaxis2=dict(
            title='Percentual Cumulativo',
            overlaying='y',
            side='right',
            range=[0, 100],
            showgrid=False
        ),
        barmode='group'
    )

    opcoes = list(df_agrupado.index.unique())
    opcoes.append("Todos os Produtos")

    app.layout = html.Div(children=[
        html.H6('Curva ABC - Produto X Loja (Pareto)'),
        dcc.Dropdown(opcoes,
                     value="Todos os Produtos",
                     id='lista_lojas',
                     clearable=True),
        dcc.Graph(
            id='grafico_curva_abc',
            figure=fig
        )
    ])

    @app.callback(
        Output('grafico_curva_abc', 'figure'),
        Input('lista_lojas', 'value')
    )
    def update_output(value):
        if value == "Todos os Produtos":
            fig = go.Figure()

            # Adicionar as barras de quantidade
            fig.add_trace(go.Bar(
                x=df_agrupado.index,
                y=df_agrupado['Produto_count'],
                name='Quantidade',
                marker_color='blue',
                text=df_agrupado['Produto_count'],
                textposition='auto'
            ))

            # Adicionar a linha de percentual cumulativo
            fig.add_trace(go.Scatter(
                x=df_agrupado.index,
                y=df_agrupado['cumulative'],
                name='Percentual Cumulativo',
                yaxis='y2',
                mode='lines+markers',
                marker=dict(color='red'),
                line=dict(shape='linear')
            ))

            fig.update_layout(
                xaxis_title='Produto',
                yaxis_title='Quantidade',
                yaxis2=dict(
                    title='Percentual Cumulativo',
                    overlaying='y',
                    side='right',
                    range=[0, 100],
                    showgrid=False
                ),
                barmode='group'
            )
        else:
            tabela_filtrada = df_agrupado[df_agrupado.index == value]
            fig = go.Figure()

            # Adicionar as barras de quantidade
            fig.add_trace(go.Bar(
                x=tabela_filtrada.index,
                y=tabela_filtrada['Produto_count'],
                name='Quantidade',
                marker_color='blue',
                text=tabela_filtrada['Produto_count'],
                textposition='auto'
            ))

            # Adicionar a linha de percentual cumulativo
            fig.add_trace(go.Scatter(
                x=tabela_filtrada.index,
                y=tabela_filtrada['cumulative'],
                name='Percentual Cumulativo',
                yaxis='y2',
                mode='lines+markers',
                marker=dict(color='red'),
                line=dict(shape='linear')
            ))

            fig.update_layout(
                xaxis_title='Produto',
                yaxis_title='Quantidade',
                yaxis2=dict(
                    title='Percentual Cumulativo',
                    overlaying='y',
                    side='right',
                    range=[0, 100],
                    showgrid=False
                ),
                barmode='group'
            )
        return fig
