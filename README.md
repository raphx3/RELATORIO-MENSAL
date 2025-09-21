Relatório de Monitoramento Ambiental Interativo
Este projeto é um painel de controle interativo (dashboard) construído com Streamlit para visualizar dados de monitoramento ambiental. O relatório simula a análise da qualidade da água e das correntes oceânicas em uma área costeira próxima a Vitória, Espírito Santo.

O objetivo deste projeto é demonstrar proficiência em:

Análise e Geração de Dados Fictícios: Criação de dados de série temporal, de contorno e geográficos que simulam um cenário realista.

Visualização de Dados: Uso de bibliotecas como Plotly e Folium para criar gráficos dinâmicos e mapas interativos.

Desenvolvimento de Aplicações Web: Criação de um painel de controle com Streamlit, permitindo a navegação por abas e a organização visual dos dados.

Geoprocessamento Básico: Representação e visualização de dados geográficos em um mapa interativo.

Funcionalidades do Dashboard
O painel apresenta quatro seções principais, acessíveis via abas:

Série Temporal: Gráfico interativo que mostra a evolução do Oxigênio Dissolvido e da Concentração de Clorofila ao longo do tempo.

Boxplot: Análise da distribuição estatística dos dados para identificar a variabilidade das variáveis.

Velocidade das Correntes: Gráfico de contorno que visualiza a velocidade das correntes marítimas em diferentes profundidades.

Mapa de Localização: Mapa interativo que mostra o ponto de monitoramento no mar, próximo à costa de Vitória.

Como Executar o Projeto
Para rodar o projeto localmente, siga os passos abaixo.

1. Pré-requisitos
Certifique-se de ter o Python instalado (versão 3.8+ recomendada).

2. Instalação das Dependências
Crie um ambiente virtual (prática recomendada) e instale todas as bibliotecas necessárias usando o arquivo requirements.txt.

Bash

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual (Windows)
.\.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
3. Execução do Aplicativo
Navegue até o diretório do projeto no seu terminal e execute o aplicativo com o comando do Streamlit:

Bash

streamlit run app.py
O aplicativo será aberto automaticamente no seu navegador padrão.

Tecnologias Utilizadas
Python

Streamlit (para a interface do dashboard)

Pandas (para manipulação e análise de dados)

NumPy (para geração de dados numéricos)

Plotly Express & Plotly Graph Objects (para visualizações gráficas)

Folium & Streamlit-Folium (para o mapa interativo)
