# Configuration settings for the Flask app

# Flask settings
DEBUG = True  # Set to False in production
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5000

# Model settings
MODEL_PATH = 'sentiment_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

# API settings
API_RATE_LIMIT = 100  # requests per minute