import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_tracks = pd.read_csv('tracks.csv')
df_genre = pd.read_csv('SpotifyFeatures.csv')

# Set page title and layout
st.set_page_config(page_title='Spotify Dashboard', layout='wide')

# Title and introduction
st.title('Spotify Dashboard')
st.write("Explore and analyze Spotify dataset with interactive visualizations!")

# Cards showing top song, top genre, top artist
top_song = df_tracks[df_tracks['popularity'] == df_tracks['popularity'].max()]
top_genre = df_genre[df_genre['popularity'] == df_genre['popularity'].max()]
top_artist = df_tracks[df_tracks['popularity'] == df_tracks['popularity'].max()]

