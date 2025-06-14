# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System** built using Python, Streamlit, and NLP techniques! This application suggests movies similar to the one you like, based on their content and metadata.

![Movie Recommender Demo](demo.gif.gif)

---

## 🚀 Features

- Recommend top 5 similar movies
- Uses **cosine similarity** over movie tags
- Poster, rating, and IMDb link using **OMDb API**
- **Clickable posters** open IMDb pages
- Built with **Streamlit** for interactive web UI

---

## 🧠 Tech Stack

- **Python**
- **Pandas & Scikit-learn** (NLP + Machine Learning)
- **Streamlit** (Web app)
- **OMDb API** (Poster & metadata)
- **Pickle** (Model persistence)

---

## 🛠️ How It Works

1. Preprocess TMDB movie and credits data.
2. Create a unified `tags` column combining genre, keywords, cast, director, and overview.
3. Apply stemming and vectorization using `CountVectorizer`.
4. Compute **cosine similarity** matrix.
5. Recommend top 5 most similar movies.

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/your-username/movie_recommender_system.git
cd movie_recommender_system
pip install -r requirements.txt
streamlit run app.py

