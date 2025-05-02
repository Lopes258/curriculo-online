import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os

# Configurações do Streamlit
st.set_page_config(page_title="Portfólio de Lucas Lopes", page_icon=":bar_chart:", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;  /* Cor de fundo escura */
        color: white;  /* Cor do texto branca */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Título do site
st.title("Lucas - Analista de Dados")

# Seção 1: Foto e informações básicas
st.header("Sobre mim")
#Criar colunas para deixar foto e resumo profissional lado a lado
col1, col2 = st.columns([1,3])
#Foto na coluna da esquerda
with col1:
    st.image(r"C:\Users\lopes\Portifolio\privados\profile.png", width=200)

#Resumo profissional a direita
with col2:
    st.subheader("Resumo da Carreira")
    st.write("""
            Sou Lucas Lopes, Analista de Dados com mais de 6 anos de experiência na transformação de dados em insights estratégicos. 
            Atualmente atuo na Cheil Brasil, liderando projetos de BI com foco em automação, visualização de dados e melhoria de performance. 
            Especialista em Power BI, Python e SQL, tenho histórico em reduzir custos, aumentar a eficiência e apoiar a tomada de decisão com inteligência analítica.
            Possuo fluência em português e inglês, além de vivência em ambientes multiculturais e domínio de metodologias ágeis.
""")
#Juntar as informações de contato e as rede sociais em duas colunas tambem
col3,col4 = st.columns([2,1])
# Informações de contato
with col3:
    st.subheader("Informações de Contato")
    st.markdown("""
                <div style="background-color: #2c2f3e; border-radius: 10px; padding:20px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <ul>
                        <li><strong>Cargo:</strong> Analista de Dados</li>
                        <li><strong>Empresa:</strong> SPOT</li>
                        <li><strong>Telefone:</strong> +55 (13) 98118-1893</li>
                        <li><strong>E-mail:</strong> lopes.lucas128@gmail.com</li>
                    <ul>
                </div>
    """, unsafe_allow_html=True)

# Links do LinkedIn e GitHub com ícones
with col4:
    st.subheader("Redes Sociais")
   
    st.markdown("""
        <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <ul>
                <li>
                    <a href="https://www.linkedin.com/in/seulinkedin" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo_2013.svg" width="20" height="20" style="vertical-align: middle;">
                        LinkedIn
                    </a>
                </li>
                <li>
                    <a href="https://github.com/seugithub" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="20" height="20" style="vertical-align: middle;">
                        GitHub
                    </a>
                <li>
                    <a href="C:/Users/lopes/Portifolio/privado/Profile.pdf" download style=text-decoration: none; color: white;">
                    📄 Baixar Currículo
                    </a>            
                </li>
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Seção 2: Gráficos de habilidades
st.header("Minhas Habilidades")

# Criar gráficos interativos (exemplo usando Plotly)
habilidades = {
    'Inglês': 8,
    'SQL': 9,
    'Python': 9,
    'Power BI': 7,
    'Looker': 6,
    'Excel': 8,
    'VBA': 5
}

# Estilo futurista com barras horizontais e gradiente de cores
fig = go.Figure()


fig.add_trace(go.Bar(
    y=list(habilidades.keys()),
    x=list(habilidades.values()),
    orientation='h',  # Barras horizontais
    marker=dict(
        color=list(habilidades.values()),
        colorscale='RdYlGn',  # Gradiente de vermelho (baixo) para verde (alto)
        cmin=0,  # Mínimo valor para a escala de cores
        cmax=10,  # Máximo valor para a escala de cores
        cornerradius=10,
        line=dict(color='black', width=0.5),  # Bordas das barras
    ),
    text=None,
    textposition=None,
    insidetextanchor='start',
    textfont=dict(color='white'),
    hoverinfo='skip'

))

# Ajustar visual
fig.update_layout(
    title="",
    xaxis=dict(
        title=None,
        showgrid=False,  # Remover a grade do gráfico
        zeroline=False,
        visible=False  # Remover a linha zero
    ),
    yaxis=dict(
        title='Habilidades',
        tickfont=dict(size=14, color='white'),  # Tamanho e cor da fonte dos ticks
    ),
    plot_bgcolor='#1e1e1e',  # Fundo escuro
    paper_bgcolor='#2c2f3e',  # Fundo do papel
    font=dict(color='white'),  # Cor da fonte geral
    height=400,
    showlegend=False,
    margin=dict(l=100, r=20, t=50, b=50),  # Ajustar margens
    
)

# Adicionar os números na parte externa da barra
for i, habilidade in enumerate(habilidades):
    valor = habilidades[habilidade]
    # Adicionando texto ao lado das barras
    fig.add_annotation(
        x=valor + 0.2,  # Ajuste para o texto ficar fora da barra
        y=i,
        text=str(valor),
        font=dict(size=14, color='white'),
        showarrow=False,
        align='left',
    )

st.plotly_chart(fig)

# Seção 3: Quadros de acesso - Hospedando diretamente no site

# Usando Expanders para criar seções que podem ser expandidas
st.header("Acesse meus Projetos")

# Dashboard
with st.expander("Dashboards", expanded=False):
    st.write("Aqui estão meus Dashboards interativos de Power BI.")
    # Exemplo de embutir Power BI via Iframe (ajustar o link do Power BI)
    st.markdown("""
        <iframe width="100%" height="400" src="https://app.powerbi.com/reportEmbed?reportId=SEU_REPORT_ID&autoAuth=true&ctid=SEU_CTI" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

# Data Science
with st.expander("Data Science", expanded=False):
    st.write("Aqui estão exemplos de projetos de Data Science.")
    st.markdown("[Ver Projetos de Data Science no GitHub](https://github.com/Lopes258/2--Projeto-Pratico---Dados)")

# Montagem de Banco e SQL
with st.expander("Montagem de Banco e Portfólio com SQL", expanded=False):
    st.write("Aqui estão meus exemplos de SQL.")
    st.markdown("""
        <pre>
        -- Exemplo de query SQL
        SELECT * FROM vendas WHERE data BETWEEN '2023-01-01' AND '2023-12-31';
        </pre>
    """, unsafe_allow_html=True)

# Automação em Python
with st.expander("Automação em Python", expanded=False):
    st.write("Aqui você pode ver minhas automações feitas com Python.")
    st.markdown("""
        <pre>
        # Exemplo de automação em Python
        import os
        os.system('python seu_script.py')
        </pre>
    """, unsafe_allow_html=True)
