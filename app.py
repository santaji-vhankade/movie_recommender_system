# -------------------------------
# Movie Recommender System (Professional Deployment-Ready)
# Built with Streamlit, OMDb API, and Content-Based Filtering
# -------------------------------

import streamlit as st  # Streamlit is used to create the web interface quickly and interactively
import pickle  # Used to load pre-computed data like movie list and similarity matrix efficiently
import requests  # For making HTTP requests to the OMDb API to get movie details
import urllib.parse  # To safely encode movie titles in URLs
from PIL import Image  # For image processing tasks like resizing posters
from io import BytesIO  # To handle image bytes from API responses
import base64  # For converting images to base64 for inline display in HTML

# -------------------------------
# Page Configuration
# -------------------------------
# Setting the title, layout, and favicon for the Streamlit app page to make it professional-looking
st.set_page_config(page_title="Movie Recommender", layout="wide", page_icon="🎬")

# -------------------------------
# Custom CSS Styling (Professional Dark Theme)
# -------------------------------
# This markdown block injects custom CSS to give the app a dark theme and consistent design language
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #0a0f2c, #1c1e2f);  /* Dark-themed background for better visual appeal */
            color: white;  /* Light text for contrast */
        }

        h1, h2, h3, .stSelectbox label {
            color: #FFD700;  /* Gold-colored headings for aesthetic contrast and readability */
        }

        .stButton>button {
            background-color: #FF6347;  /* Tomato color for CTA buttons to draw user attention */
            color: white;
            border-radius: 8px;  /* Rounded corners for modern UI look */
            padding: 0.6em 1.2em;
            font-weight: bold;
            font-size: 16px;
            width: 100%;
            max-width: 400px;
            display: block;
            margin: 0 auto;  /* Center-align button */
        }

        .stButton>button:hover {
            background-color: #e03e3e;  /* Slightly darker on hover for feedback */
        }

        .stSelectbox input, .stSelectbox div[data-baseweb="select"] {
            color: white !important;
            background-color: #1c2c40 !important;  /* Matches dark theme for input fields */
        }

        .stSelectbox [role="listbox"] {
            background-color: #1c2c40 !important;  /* Dropdown background to match theme */
        }

        .stSelectbox [role="option"]:hover {
            background-color: #FF6347 !important;
            color: white !important;  /* Highlights options on hover for interactivity */
        }

        div[data-baseweb="select"] {
            max-width: 400px !important;
            margin: 0 auto !important;  /* Align dropdown centrally */
        }

        img {
            box-shadow: 0 0 8px rgba(255,255,255,0.15);  /* Subtle shadow around posters for depth */
            border-radius: 10px;  /* Smooth poster corners */
        }

        .footer {
            text-align: center;
            color: #CCCCCC;
            font-size: 0.9rem;
            margin-top: 2em;  /* Footer separated from content */
        }

        .footer a {
            color: #AAAAFF;
            text-decoration: none;  /* Custom styling for footer links */
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Movie Data & Similarity Matrix
# -------------------------------
# Loading movie metadata and precomputed similarity scores to avoid recalculating each time
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# -------------------------------
# Title and Intro
# -------------------------------
# Main title and introduction to guide the user on how to use the app
st.title("🎬 Movie Recommender System")
st.markdown("""
Welcome to the **Movie Recommender System**! 
Select a movie you like and discover 5 similar ones. Posters are clickable to view IMDb pages.
""")

# -------------------------------
# Convert PIL image to base64 (for embedding)
# -------------------------------
def image_to_base64(img):
    buffered = BytesIO()  # Creating a memory buffer to temporarily store the image
    img.save(buffered, format="PNG")  # Save the image to buffer in PNG format
    return base64.b64encode(buffered.getvalue()).decode()  # Encode as base64 for inline HTML rendering

# -------------------------------
# Fetch Poster, IMDb Rating, IMDb URL
# -------------------------------
def fetch_movie_data(title, size=(200, 300)):
    api_key = 'a04287cf'  # OMDb API key to fetch movie details
    encoded_title = urllib.parse.quote(title)  # Encoding the movie title to be URL-safe
    url = f"http://www.omdbapi.com/?t={encoded_title}&apikey={api_key}"  # Constructing API URL

    try:
        r = requests.get(url)  # Sending API request
        data = r.json()  # Parsing JSON response

        # If valid poster exists, load it and resize; else create a placeholder image
        poster_url = data.get('Poster')
        if poster_url and poster_url != 'N/A':
            img = Image.open(BytesIO(requests.get(poster_url).content)).resize(size)
        else:
            img = Image.new("RGB", size, color=(40, 40, 40))  # Grey placeholder for missing posters

        rating = data.get('imdbRating', 'N/A')  # Extract IMDb rating

        imdb_id = data.get('imdbID')  # Construct IMDb URL
        imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

        return img, rating, imdb_url  # Return all fetched data
    except:
        fallback = Image.new("RGB", size, color=(70, 70, 70))  # Handle any failure with darker placeholder
        return fallback, 'N/A', None

# -------------------------------
# Recommend Function using Cosine Similarity
# -------------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]  # Get index of selected movie from the DataFrame
    distances = similarity[index]  # Get similarity scores for that movie
    recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Top 5 similar movies

    results = []
    for i in recommended:
        title = movies.iloc[i[0]].title  # Get recommended movie title
        poster, rating, url = fetch_movie_data(title)  # Fetch its data
        results.append((title, poster, rating, url))  # Store in results list
    return results

# -------------------------------
# UI - Movie Selection
# -------------------------------
# Movie selection dropdown lets user choose a reference movie for recommendations
selected_movie = st.selectbox("🎞️ Choose a movie you like:", movies['title'].values)

# -------------------------------
# Show Recommendations
# -------------------------------
if st.button("🔍 Recommend"):  # When user clicks recommend button
    with st.spinner("Fetching recommendations..."):  # Show spinner for user feedback
        recommendations = recommend(selected_movie)  # Get recommendations

    st.subheader("🎥 Top 5 Recommendations:")  # Section header for results
    cols = st.columns(5)  # Divide layout into 5 columns for poster display

    for i, (title, poster, rating, url) in enumerate(recommendations):  # Iterate over each recommended movie
        with cols[i]:
            img_base64 = image_to_base64(poster)  # Convert image to base64 for HTML rendering
            if url:  # If IMDb URL available, wrap poster in a clickable link
                st.markdown(f'''
                    <a href="{url}" target="_blank">
                        <img src="data:image/png;base64,{img_base64}" width="200" />
                    </a>
                    <br><b>{title}</b><br>⭐ IMDb: {rating}
                ''', unsafe_allow_html=True)
            else:  # Else show plain image and text
                st.image(poster, width=200)
                st.markdown(f"**{title}**<br>⭐ IMDb: {rating}", unsafe_allow_html=True)

# -------------------------------
# Footer
# -------------------------------
# Footer adds professional credit and link to GitHub repo for transparency and access
st.markdown("""
<hr>
<div class="footer">
    © 2025 Santaji Vhankade | Built with Streamlit & OMDb API<br>
    <a href="https://github.com/santaji-vhankade/movie_recommender_system" target="_blank">🔗 GitHub Repository</a>
</div>
""", unsafe_allow_html=True)
