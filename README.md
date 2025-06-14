# 🎬 Movie Recommender System

![Demo](demo.gif)

An intelligent movie recommendation system built using **Machine Learning** and deployed with **Streamlit**.  
Given a movie title, it suggests 5 similar movies using content-based filtering.

---

## 🚀 Features

- 🔍 Content-based filtering using cosine similarity
- 🎯 Recommendations based on cast, genre, overview, and keywords
- 🖼️ Poster images and IMDb ratings from OMDb API
- 🎥 Clickable posters linking directly to IMDb
- 🧠 NLP preprocessing using stemming and vectorization
- ⚡ Clean, interactive UI with Streamlit

---

## 🛠️ Tech Stack

| Tool            | Purpose                             |
|-----------------|-------------------------------------|
| Python          | Core programming language           |
| Pandas          | Data handling & preprocessing       |
| Scikit-learn    | Cosine similarity & vectorization   |
| NLTK            | Text stemming for better matches    |
| Streamlit       | Web UI                              |
| OMDb API        | Movie metadata (poster, rating)     |
| Pickle          | Model/data serialization            |

---

## 🧠 How It Works

1. Preprocess the TMDB movie and credit datasets
2. Merge and clean relevant features like `cast`, `crew`, `genres`, `keywords`, and `overview`
3. Create a new column `tags` from those features
4. Apply stemming to normalize text
5. Use `CountVectorizer` to convert tags into vectors
6. Calculate cosine similarity between movies
7. On user input, find top 5 most similar movies
8. Fetch posters, ratings, and IMDb links using OMDb API
9. Display them with clickable poster layout in Streamlit

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/santaji-vhankade/movie_recommender_system.git
cd movie_recommender_system
