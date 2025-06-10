# Import necessary libraries
import pandas as pd
import warnings
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

# Ignore warning messages
warnings.filterwarnings('ignore')

# ----------------------------
# Step 1: Load the datasets
# ----------------------------
movies = pd.read_csv(r"C:\Users\Rajesh\Desktop\movie_recommender\movies_recommendation_tmdb_5000_movies.csv")
credits = pd.read_csv(r"C:\Users\Rajesh\Desktop\movie_recommender\movies_recommedations_tmdb_5000_credits.csv")

# Merge movies and credits data on the 'title' column
movies = movies.merge(credits, on='title')

# Select only the necessary columns for the recommendation system
movies = movies[['genres', 'movie_id', 'keywords', 'title', 'overview', 'cast', 'crew']]

# Remove rows with missing values and duplicates
movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)

# ----------------------------
# Step 2: Preprocessing helpers
# ----------------------------

# Convert stringified JSON to list of 'name' values
def convert(obj):
    try:
        L = [i['name'] for i in ast.literal_eval(obj)]
    except:
        L = []
    return L

# Extract top 3 cast members
def convert3(obj):
    try:
        L = [i['name'] for i in ast.literal_eval(obj)[:3]]
    except:
        L = []
    return L

# Extract director name from crew list
def fetch_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return [i['name']]
    except:
        return []
    return []

# Apply transformations on respective columns
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)

# Split overview into list of words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces in multi-word names to ensure consistency
for feature in ['genres', 'keywords', 'cast', 'crew']:
    movies[feature] = movies[feature].apply(lambda x: [i.replace(" ", "") for i in x])

# ----------------------------
# Step 3: Creating tags
# ----------------------------

# Combine all text features into a single 'tags' column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Create a new DataFrame with essential columns
new_df = movies[['movie_id', 'title', 'tags']].copy()

# Join list into a string and convert to lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x).lower())

# Initialize Porter Stemmer
ps = PorterStemmer()

# Define stemming function
def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])

# Apply stemming to tags
new_df['tags'] = new_df['tags'].apply(stem)

# ----------------------------
# Step 4: Vectorization & Similarity
# ----------------------------

# Convert text data into numerical vectors using CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity between all movie vectors
similarity = cosine_similarity(vectors)

# ----------------------------
# Step 5: Save processed data
# ----------------------------

# Save the processed DataFrame and similarity matrix using pickle
pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Preprocessing and model training completed. Files saved: movies.pkl, similarity.pkl")
