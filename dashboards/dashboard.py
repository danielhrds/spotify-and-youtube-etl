import streamlit as st
from pymongo import MongoClient
import pandas as pd

import matplotlib.pyplot as plt

import os
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(layout="wide")

client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DB')]

st.title("Análise de Tendências: Spotify e YouTube")
fonte = st.sidebar.radio("Selecione a Fonte", ['Spotify', 'YouTube'])

if fonte == 'Spotify':
    df = pd.DataFrame(list(db.spotify_tracks.find()))

    # array = [
    #     "Faixas Populares", "Artistas em Destaque",
    #     "Distribuição de Duração", "Linha do Tempo de Lançamentos"
    # ]
    array = [
        "Faixas Populares", "Artistas em Destaque",
        "Distribuição de Duração"
    ]

    aba = st.sidebar.selectbox("Tópico", array)

    if aba == "Faixas Populares":
        st.subheader("Faixas Mais Populares")
        st.dataframe(df[['name', 'artist', 'popularity', 'duration_min']])
        st.bar_chart(df.set_index('name')['popularity'])

    elif aba == "Artistas em Destaque":
        st.subheader("Artistas Mais Frequentes")
        top_artistas = df['artist'].value_counts().head(10)
        st.bar_chart(top_artistas)

    elif aba == "Distribuição de Duração":
        st.subheader("Distribuição da Duração das Músicas (min)")
        fig, ax = plt.subplots()
        df['duration_min'].hist(bins=20, ax=ax)
        st.pyplot(fig)

    # elif aba == "Linha do Tempo de Lançamentos":
    #     st.subheader("Lançamentos por Ano")
    #     if 'release_date' in df.columns:
    #         df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    #         timeline = df['release_year'].value_counts().sort_index()
    #         st.line_chart(timeline)
    #     else:
    #       st.info("Sem dados válidos disponíveis.")

elif fonte == 'YouTube':
    df = pd.DataFrame(list(db.youtube_videos.find()))

    # array = [
    #     "Vídeos Populares", "Canais em Destaque",
    #     "Distribuição de Duração", "Linha do Tempo de Publicações"
    # ]
    array = [
        "Vídeos Populares", "Canais em Destaque",
    ]
    aba = st.sidebar.selectbox("Tópico", array)

    if aba == "Vídeos Populares":
        st.subheader("Vídeos Mais Populares")
        st.dataframe(df[['title', 'channel', 'views', 'likes', 'comments']])
        st.line_chart(df[['views', 'likes', 'comments']])

    elif aba == "Canais em Destaque":
        st.subheader("Canais com Mais Vídeos")
        top_canais = df['channel'].value_counts().head(10)
        st.bar_chart(top_canais)

    # elif aba == "Distribuição de Duração":
    #     st.subheader("Distribuição da Duração dos Vídeos (min)")
    #     if 'duration_min' in df.columns:
    #         fig, ax = plt.subplots()
    #         df['duration_min'].hist(bins=20, ax=ax)
    #         st.pyplot(fig)
    #     else:
    #       st.info("Sem dados válidos disponíveis.")

    # elif aba == "Linha do Tempo de Publicações":
    #     st.subheader("Publicações por Ano")
    #     if 'publish_time' in df.columns:
    #         df['publish_year'] = pd.to_datetime(df['publish_time'], errors='coerce').dt.year
    #         timeline = df['publish_year'].value_counts().sort_index()
    #         st.line_chart(timeline)
    #     else:
    #       st.info("Sem dados válidos disponíveis.")