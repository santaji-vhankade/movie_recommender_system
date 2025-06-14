# 🎬 Movie Recommender System

![Demo](demo.gif)

An intelligent movie recommendation system built using **Machine Learning** and deployed with **Streamlit**. This project suggests similar movies based on a selected title using a content-based filtering approach.

---

## 🚀 Features

- 🔍 Movie similarity search
- 🧠 Machine learning model for content-based recommendations
- 🎥 Movie poster and metadata fetched using OMDb API
- 💡 User-friendly web interface with Streamlit
- 🖱️ Clickable posters redirecting to IMDb

---

## 📂 Project Structure

```plaintext
movie_recommender_system/
│
├── app.py                  # Streamlit app
├── model_trainer.py        # Script to preprocess data and train similarity model
├── movies.pkl              # Pickle file containing movie data
├── similarity.pkl          # Pickle file containing similarity matrix
├── similarity.pkl.gz       # Compressed version of similarity matrix
├── requirements.txt        # Project dependencies
└── demo.gif                # App demo (optional, remove if corrupted)
