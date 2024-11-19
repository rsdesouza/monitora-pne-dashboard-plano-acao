import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    st.title("Acompanhamento de Estratégias - Meta 15 do PNE")

    # Conectar ao Google Cloud Storage (GCS) e ler o arquivo CSV
    conn = st.connection('gcs', type=FilesConnection)

    # Especificar o caminho do arquivo no bucket do GCS
    df = conn.read("monitora_pne_15_streamlit/planoacao.csv", input_format="csv", ttl=600, sep=";", decimal=",")

    df.set_index('index', inplace=True)

    ###### Consulta plano de ação agrupado ######
    consulta_plano_acao_agrupado = df.groupby(['status', 'indicador']).size().reset_index(name='total_planos_de_acao')

    ###### Consulta Indicador 1 ######
    consultaIndicador1 = df[df['indicador'] == 'indicador1']
    agrupamento_status_indicador1 = consultaIndicador1.groupby('status').size().reset_index(name='total_planos_de_acao')

    ###### Consulta Indicador 2 ######
    consultaIndicador2 = df[df['indicador'] == 'indicador2']
    agrupamento_status_indicador2 = consultaIndicador2.groupby('status').size().reset_index(name='total_planos_de_acao')

    ###### Consulta Indicador 3 ######
    consultaIndicador3 = df[df['indicador'] == 'indicador3']
    agrupamento_status_indicador3 = consultaIndicador3.groupby('status').size().reset_index(name='total_planos_de_acao')

    ###### Consulta Indicador 4 ######
    consultaIndicador4 = df[df['indicador'] == 'indicador4']
    agrupamento_status_indicador4 = consultaIndicador4.groupby('status').size().reset_index(name='total_planos_de_acao')

    ##### Área de Gráficos #####

    #### Geral ####
    grafico_geral = px.bar(
        consulta_plano_acao_agrupado,
        x='status',
        y='total_planos_de_acao',
        color='indicador',
        title='Status Geral dos planos de ação por indicador'
    )
    st.plotly_chart(grafico_geral)

    multi = '''**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.
    #'''
    st.markdown(multi)

    grafico_indicador1 = px.bar(
        agrupamento_status_indicador1,
        x='status',
        y='total_planos_de_acao',
        color='status',
        title='Status por indicador'
    )
    grafico_pizza_indicador1 = px.pie(
        agrupamento_status_indicador1,
        values='total_planos_de_acao',
        names='status',
        color='status',
        title='Status por indicador'
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_indicador1)
    with col2:
        st.plotly_chart(grafico_pizza_indicador1)

    multi = '''**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação
    superior está adequada à área de conhecimento que lecionam.
    #'''
    st.markdown(multi)

    grafico_indicador2 = px.bar(
        agrupamento_status_indicador2,
        x='status',
        y='total_planos_de_acao',
        color='status',
        title='Status por indicador'
    )
    grafico_pizza_indicador2 = px.pie(
        agrupamento_status_indicador2,
        values='total_planos_de_acao',
        names='status',
        color='status',
        title='Status por indicador'
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_indicador2)
    with col2:
        st.plotly_chart(grafico_pizza_indicador2)

    multi = '''**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação
    superior está adequada à área de conhecimento que lecionam.
    #'''
    st.markdown(multi)

    grafico_indicador3 = px.bar(
        agrupamento_status_indicador3,
        x='status',
        y='total_planos_de_acao',
        color='status',
        title='Status por indicador'
    )
    grafico_pizza_indicador3 = px.pie(
        agrupamento_status_indicador3,
        values='total_planos_de_acao',
        names='status',
        color='status',
        title='Status por indicador'
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_indicador3)
    with col2:
        st.plotly_chart(grafico_pizza_indicador3)

    multi = '''**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada
    à área de conhecimento que lecionam.
    #'''
    st.markdown(multi)

    grafico_indicador4 = px.bar(
        agrupamento_status_indicador4,
        x='status',
        y='total_planos_de_acao',
        color='status',
        title='Status por indicador'
    )
    grafico_pizza_indicador4 = px.pie(
        agrupamento_status_indicador4,
        values='total_planos_de_acao',
        names='status',
        color='status',
        title='Status por indicador'
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_indicador4)
    with col2:
        st.plotly_chart(grafico_pizza_indicador4)

if __name__ == "__main__":
    main()
