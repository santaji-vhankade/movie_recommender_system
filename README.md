# 🎬 Movie Recommender System

![Demo](demo.gif)

An intelligent movie recommendation engine built using **machine learning** and deployed with **Streamlit** on **Render**. It suggests similar movies based on a selected title using a **content-based filtering** approach.

---

## 🚀 Features

- 🔎 **Search for similar movies** by title  
- 🧠 **Content-based filtering** using NLP and cosine similarity  
- 🎥 **Movie posters & metadata** fetched live via OMDb API  
- 💻 **Interactive web UI** built with Streamlit  
- ☁️ **Deployed on Render** with a public link  
- 🔗 Poster images link to IMDb  


---

## 📂 Project Structure

```plaintext
movie_recommender_system/
│
├── app.py                  # Streamlit frontend
├── model_trainer.py        # Data preprocessing & similarity model builder
├── movies.pkl              # Pickled movie metadata
├── similarity.pkl.gz       # Compressed similarity matrix
├── requirements.txt        # Required Python packages
├── demo.gif                # Demo preview
└── README.md
