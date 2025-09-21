#%% Modulos
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
from streamlit_folium import st_folium
import folium

#%% CSS personalizado
css_file_path = os.path.join(os.path.dirname(__file__), "style.css")

if os.path.exists(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"Erro: O arquivo CSS não foi encontrado em {css_file_path}")

#%% Dados

# Geração de dados de série temporal para 2025 - Qualidade da Água
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
data = {
    "Data": dates,
    "Oxigênio Dissolvido (mg/L)": np.random.normal(7, 1.5, len(dates)),  # Valores mais realistas
    "Concentração de Clorofila (ug/L)": np.random.normal(5, 2, len(dates)) # Valores para eutrofização
}
df = pd.DataFrame(data)
df = df.set_index('Data')
df = df.rolling(window='7D').mean()
df = df.reset_index()

# Dados e plot do novo gráfico de contorno (Velocidade) - Correntes Oceânicas ---
tempo = pd.date_range(start='2025-01-01', end='2025-12-31', freq='D')
# Profundidades em metros

profundidades = [1, 5, 10, 20, 50] 
# Geração de dados simulando correntes mais fortes na superfície e mais fracas em profundidade
vel_prof_1 = np.random.normal(2.5, 0.5, len(tempo))
vel_prof_2 = np.random.normal(1.8, 0.4, len(tempo))
vel_prof_3 = np.random.normal(1.2, 0.3, len(tempo))
vel_prof_4 = np.random.normal(0.8, 0.2, len(tempo))
vel_prof_5 = np.random.normal(0.3, 0.1, len(tempo))

df_velocidade = pd.DataFrame({
    'tempo': tempo, 
    f'{profundidades[0]}m': vel_prof_1,
    f'{profundidades[1]}m': vel_prof_2,
    f'{profundidades[2]}m': vel_prof_3,
    f'{profundidades[3]}m': vel_prof_4,
    f'{profundidades[4]}m': vel_prof_5,
}).set_index('tempo').round(2)

#%% Plots
fig_velocidade = go.Figure(go.Contour(
    z=df_velocidade.transpose().values,
    x=df_velocidade.index,
    y=df_velocidade.columns,
    colorscale='Jet',
    colorbar=dict(title="Velocidade (m/s)"),
    contours=dict(showlines=False)
))

fig_velocidade.update_layout(
    title='Velocidade das Correntes em Diferentes Profundidades',
    xaxis_title='Tempo (dias)',
    yaxis_title='Profundidade (m)',
    yaxis=dict(autorange='reversed'), # Reverte o eixo Y para profundidade
    width=1000,
    height=450,
    template='ggplot2'
)

# Mapa
vitoria_coords = [-20.315, -40.262]
m = folium.Map(location=vitoria_coords, zoom_start=12)
folium.Marker(
    location=vitoria_coords,
    popup="Vitória, ES",
    tooltip="Ponto amostral",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)

#%% Front end
#st.title("Relatório de Monitoramento Ambiental")

with st.container(key="main_wrapper_card"):
    col_full1 = st.columns(1)[0]
    col_full2 = st.columns(1)[0]
    col_half1, col_half2 = st.columns(2)
    col_full3 = st.columns(1)[0]

    with col_full1:
        with st.container(border=True):
            st.subheader("Contexto do Projeto")
            st.write(
                "Este relatório mensal apresenta dados de monitoramento ambiental de uma área costeira próxima a Vitória, Espírito Santo. O projeto visa avaliar a qualidade da água e os padrões de correntes oceânicas para um ecossistema marinho sustentável."
            )

    with col_full2:
        with st.container(border=True):
            st.subheader("Análise de Dados")
            st.write(
                "A análise se concentra na evolução diária de variáveis críticas para a saúde do ecossistema: o nível de **Oxigênio Dissolvido** e a **Concentração de Clorofila**, que é um indicador de produtividade biológica. Além disso, o relatório explora os padrões de velocidade das correntes marítimas em diferentes profundidades."
            )
            
            tab1, tab2, tab3, tab4 = st.tabs(["Série Temporal", "Boxplot", "Velocidade das Correntes", "Mapa de Localização"])

            with tab1:
                fig = px.line(
                    df,
                    x="Data",
                    y=["Oxigênio Dissolvido (mg/L)", "Concentração de Clorofila (ug/L)"],
                    template="simple_white",
                    height=450,
                    width=1000,
                    title="Série Temporal de Indicadores de Qualidade da Água"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with tab2:
                df_melted = df.melt(id_vars='Data', value_vars=["Oxigênio Dissolvido (mg/L)", "Concentração de Clorofila (ug/L)"], var_name='Variável', value_name='Valores')
                fig = px.box(
                    df_melted,
                    x="Variável",
                    y="Valores",
                    template="simple_white",
                    height=450,
                    width=1000,
                    title="Distribuição das Variáveis de Qualidade da Água"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with tab3:
                st.plotly_chart(fig_velocidade, use_container_width=True)

            with tab4:
                st_folium(m, width=700, height=400)

    with col_full3:
        with st.container(border=True):
            st.subheader("Conclusão e Recomendações")
            st.write(
                "Os dados mostram que os níveis de **Oxigênio Dissolvido** se mantiveram dentro da faixa esperada, indicando boa saúde geral do ecossistema. A **Concentração de Clorofila**, no entanto, apresentou picos pontuais que merecem atenção, pois podem indicar eventos de eutrofização. As correntes superficiais são significativamente mais rápidas que as de profundidade, um padrão comum que impacta a dispersão de nutrientes e poluentes. **Recomendamos** um monitoramento mais frequente durante os meses de maior temperatura para identificar a causa dos picos de clorofila."
            )
            st.button("Gerar Relatório Completo", key="card5_button")