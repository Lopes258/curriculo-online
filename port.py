import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# Configurações do Streamlit
st.set_page_config(page_title="Portfólio de Lucas Lopes", page_icon=":bar_chart:", layout="wide")
st.markdown(
    """
    <style>
    /* Forçar tema escuro para todo o site */
    .stApp {
        background-color: #1e1e1e;
        color: white;
    }
    
    /* Estilizar elementos específicos do Streamlit */
    .stButton button {
        background-color: #2c2f3e;
        color: white;
        border: 1px solid #4a4a4a;
    }
    
    .stSelectbox {
        background-color: #2c2f3e;
        color: white;
    }
    
    /* Estilizar textos e cabeçalhos */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    p, div {
        color: white !important;
    }
    
    /* Estilizar expanders */
    .streamlit-expanderHeader {
        background-color: #2c2f3e !important;
        color: white !important;
    }
    
    /* Estilizar links */
    a {
        color: #4a9eff !important;
    }
    
    a:hover {
        color: #6fb1ff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Seleção de idiomas
language = st.selectbox("Selecione o idioma", ["Português", "English"])
language_code = 'pt'if language == "Português" else 'en'


#TEXTOS
texts = {
    'title': {
        'pt': "Lucas - Analista de Dados",
        'en': "Lucas - Data Analyst"
    },
    'about': {
        'pt': "Sobre mim",
        'en': "About me"
    },
    'summary': {
        'pt': "Resumo da Carreira",
        'en': "Career Summary"
    },
    'sumary_text': {
        'pt': """Sou Lucas Lopes, Analista de Dados com mais de 6 anos de experiência na transformação de dados em insights estratégicos. 
                Atualmente atuo na Cheil Brasil, liderando projetos de BI com foco em automação, visualização de dados e melhoria de performance. 
                Especialista em Power BI, Python e SQL, tenho histórico em reduzir custos, aumentar a eficiência e apoiar a tomada de decisão com inteligência analítica.
                Possuo fluência em português e inglês, além de vivência em ambientes multiculturais e domínio de metodologias ágeis.""",
        'en':"""I'm Lucas Lopes, a Data Analyst with over 6 years of experience transforming data into strategic insights. 
                Currently working at Cheil Brazil, I lead BI projects focused on automation, data visualization, and performance improvement. 
                I specialize in Power BI, Python, and SQL, with a track record of reducing costs, increasing efficiency, and supporting decision-making with analytical intelligence. 
                Fluent in both Portuguese and English, with multicultural experience and knowledge of agile methodologies."""      
                },
    'contact': {
        'pt': "Informações de Contato",
        'en': "Contact Information"
    },
    'social': {
        'pt': "Redes Sociais",
        'en': "Social Networks"
    },
    'skills': {
        'pt': "Minhas Habilidades",
        'en': "My Skills"
    },
    'projects': {
        'pt': "Acesse meus Projetos",
        'en': "Access my Projects"
    },
    'dashboard': {
        'pt': "Aqui um exemplo de Dashboards em Power BI.",
        'en': "Here there is a exemple of Dashboards in Power BI."
    },
    'data_science': {
        'pt': "Acesse o meu github para ver uma analise em Data Science usando Python.",
        'en': "Access my github to see a a analisys of Data Science using Python."
    },
    'sql': {
        'pt': "Montagem de Banco e SQL",
        'en': "Database Setup and SQL"
    },
    'automation': {
        'pt': "Automação em Python",
        'en': "Automation in Python"
    },
    'download_resume': {
        'pt': "📄 Baixar Currículo",
        'en': "📄 Download Resume"
    },
    'phone': {
        'pt': "Telefone",
        'en': "Phone"
    },
    'email': {
        'pt': "E-mail",
        'en': "E-mail"
    },
    'position': {
        'pt': "Cargo",
        'en': "Position"
    },
    'company': {
        'pt': "Empresa",
        'en': "Company"
    }
}



# Título do site
st.title(texts['title'][language_code])

# Seção 1: Foto e informações básicas
st.header(texts['about'][language_code])
#Criar colunas para deixar foto e resumo profissional lado a lado
col1, col2 = st.columns([1,3])
#Foto na coluna da esquerda
with col1:
    st.image("profile.png", width=200)

#Resumo profissional a direita
with col2:
    st.subheader(texts['summary'][language_code])
    st.write(texts['sumary_text'][language_code])
#Juntar as informações de contato e as rede sociais em duas colunas tambem
col3,col4 = st.columns([2,1])
# Informações de contato
with col3:
    st.subheader(texts['contact'][language_code])
    st.markdown(f"""
        <div style="background-color: #2c2f3e; border-radius: 10px; padding:20px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <ul>
                <li><strong>{texts['position'][language_code]}:</strong> Analista de Dados</li>
                <li><strong>{texts['company'][language_code]}:</strong> SPOT</li>
                <li><strong>{texts['phone'][language_code]}:</strong> +55 (13) 98118-1893</li>
                <li><strong>{texts['email'][language_code]}:</strong> lopes.lucas128@gmail.com</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Redes sociais
with col4:
    st.subheader(texts['social'][language_code])
    st.markdown(f"""
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
                </li>
                <li>
                    <a href="Profile.pdf" download style="text-decoration: none; color: white;">
                        {texts['download_resume'][language_code]}
                    </a>            
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
st.header(texts['projects'][language_code])

# Dashboard
with st.expander("Dashboards", expanded=False):
    st.write(texts['dashboard'][language_code])
    # Exemplo de embutir Power BI via Iframe (ajustar o link do Power BI)
    st.markdown("""
        <iframe width="100%" height="400" src="https://app.powerbi.com/reportEmbed?reportId=SEU_REPORT_ID&autoAuth=true&ctid=SEU_CTI" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

# Data Science
with st.expander("Data Science", expanded=False):
    st.write(texts['data_science'][language_code])
    
    # Adicionar título e descrição do projeto
    st.subheader("Análise de Dados de Alimentos")
    st.write("""
    Este projeto realiza uma análise detalhada de dados de alimentos, incluindo:
    - Tratamento de dados e preparação para análise
    - Análise exploratória de dados
    - Visualizações interativas
    - Insights sobre nutrição e categorias de alimentos
    """)
    
    # Adicionar link para o notebook
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>📊 Notebook de Análise</h4>
        <p>Para ver a análise completa, acesse o notebook no GitHub:</p>
        <a href="https://github.com/Lopes258/food_project/blob/main/src/analysis/food_analysis.ipynb" target="_blank" style="color: #4a9eff;">
            Ver Notebook Completo
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Adicionar seção de tecnologias utilizadas
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>🛠️ Tecnologias Utilizadas</h4>
        <ul>
            <li>Python</li>
            <li>Pandas</li>
            <li>Matplotlib</li>
            <li>Seaborn</li>
            <li>Jupyter Notebook</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Montagem de Banco e SQL
with st.expander("SQL", expanded=False):
    st.write(texts['sql'][language_code])
    
    # Adicionar informações sobre o projeto BigQuery
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>📊 Projeto Food Analysis - BigQuery</h4>
        <p>Projeto de análise de dados de alimentos utilizando Google BigQuery, incluindo:</p>
        <ul>
            <li>Integração com API de alimentos</li>
            <li>Automação de coleta de dados</li>
            <li>Análise nutricional</li>
            <li>Dashboard interativo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Exemplos de queries do projeto de alimentos
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>🔍 Exemplos de Queries do Projeto</h4>
        <pre style="background-color: #1e1e1e; padding: 15px; border-radius: 5px; overflow-x: auto;">
-- Análise de alimentos por categoria
SELECT 
    food_category,
    COUNT(*) as total_foods,
    AVG(calories) as avg_calories,
    AVG(protein) as avg_protein
FROM `food-project-459320.food_data.foods`
GROUP BY food_category
ORDER BY total_foods DESC;

-- Análise nutricional detalhada
SELECT 
    food_name,
    calories,
    protein,
    carbs,
    fat,
    ROUND((protein * 4 + carbs * 4 + fat * 9) / calories * 100, 2) as macro_balance
FROM `food-project-459320.food_data.foods`
WHERE calories > 0
ORDER BY macro_balance DESC
LIMIT 10;
        </pre>
    </div>
    """, unsafe_allow_html=True)

# Codigo desse projeto no Streamlit
with st.expander("Python", expanded=False):
    st.write(texts['automation'][language_code])
    
    # Mostrar o código de automação
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>🤖 Automação de Coleta de Dados</h4>
        <p>Código Python para coleta automática de dados de alimentos via API e carregamento no BigQuery:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Código de exemplo da automação
    st.code("""
import requests
import pandas as pd
from google.cloud import bigquery
from datetime import datetime

def fetch_food_data():
    # Configuração da API
    api_url = "https://api.example.com/foods"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }
    
    # Coleta de dados
    response = requests.get(api_url, headers=headers)
    data = response.json()
    
    # Transformação dos dados
    df = pd.DataFrame(data)
    df['load_date'] = datetime.now()
    
    # Carregamento no BigQuery
    client = bigquery.Client()
    table_id = "food-project-459320.food_data.foods"
    
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
    )
    
    job = client.load_table_from_dataframe(
        df, table_id, job_config=job_config
    )
    job.result()
    
    return f"Loaded {len(df)} rows into {table_id}"
    """, language="python")
    
    # Explicação do processo
    st.markdown("""
    <div style="background-color: #2c2f3e; border-radius: 10px; padding: 20px; margin: 10px 0;">
        <h4>🔄 Processo de Automação</h4>
        <ol>
            <li>Coleta de dados via API de alimentos</li>
            <li>Transformação e limpeza dos dados</li>
            <li>Carregamento automático no BigQuery</li>
            <li>Atualização diária dos dados</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
