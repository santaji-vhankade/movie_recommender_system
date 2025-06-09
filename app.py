# app.py

import streamlit as st
import pickle
import requests
import urllib.parse

# Load the preprocessed movie data and similarity matrix from pickle files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values
)

def fetch_poster(movie_title):
    api_key = OMDB_API_KEY
    movie_title_encoded = urllib.parse.quote(movie_title)
    url = f"http://www.omdbapi.com/?t={movie_title_encoded}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    poster_url = data.get('Poster')
    if poster_url and poster_url != 'N/A':
        return poster_url
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
