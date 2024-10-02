import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    st.title("Acompanhamento dos planos de ação")

    ###### Total de Planos de ação por indicador ######
    dfIndicadorGeral = pd.read_csv("indicador_qt_plano_acao.csv", sep=";", decimal=",")
    dfIndicadorGeral.set_index('index', inplace=True)

    ###### Total status por indicador ######
    dfStatus = pd.read_csv("indicador_status_plano_acao.csv", sep=";", decimal=",")
    dfStatus.set_index('index', inplace=True)

    ##### Área de Gráficos #####
    st.markdown("Abaixo os gráficos de acompanhamento dos planos de ação aplicadas às estratégias dos indicadores da meta 15 do PNE.")

    # Gráfico 1: Total de Planos de Ação
    multi = '''**Planos de Ação** - Total de planos de ação associados aos indicadores da meta 15 do PNE.'''
    st.markdown(multi)

    grafico_geral = px.bar(dfIndicadorGeral, x='indicador', y='quantidade', color='indicador',
                           title='Indicador Geral - Total de planos de ação ativos vinculados aos indicadores.')
    st.plotly_chart(grafico_geral)

    # Gráfico 2: Status dos Planos de Ação para o Indicador 1
    multi = '''**Status dos Planos de Ação para o Indicador 1.**'''
    st.markdown(multi)

    indicador1 = px.bar(dfStatus, x='status', y='quantidade', color='status', title='Status por Indicador')
    indicador1Pizza = px.pie(dfStatus, values='quantidade', names='status', color='status', title='Status por Indicador')

    # Exibir os gráficos lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(indicador1)
    with col2:
        st.plotly_chart(indicador1Pizza)

if __name__ == "__main__":
    main()
