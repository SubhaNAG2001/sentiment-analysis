from flask import Flask, request, jsonify, render_template
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords

# Initialize Flask app
app = Flask(__name__)

# Download NLTK resources
print("Downloading NLTK resources...")
nltk.download('stopwords')
nltk.download('punkt')

# Load the model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

stop_words = set(stopwords.words('english'))

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)         # Remove mentions
    text = re.sub(r'#', '', text)                      # Remove hashtags
    text = re.sub(r'RT[\s]+', '', text)                # Remove retweet
    text = re.sub(r'https?:\/\/\S+', '', text)         # Remove URLs
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # Remove punctuation
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)
    
    text = re.sub(r'\s+', ' ', text).strip()           # Normalize whitespace
    return text

# Prediction function
def predict_sentiment(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)
    
    # Get prediction probability
    proba = model.predict_proba(vec)[0]
    confidence = max(proba) * 100  # Convert to percentage
    
    return prediction[0], confidence

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get text from request
        data = request.get_json()
        text = data['text']
        
        # Make prediction
        sentiment, confidence = predict_sentiment(text)
        
        # Return result
        return jsonify({
            'text': text,
            'sentiment': sentiment,
            'confidence': f"{confidence:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/sentiment', methods=['POST'])
def api_sentiment():
    try:
        # Get text from request
        data = request.get_json()
        text = data['text']
        
        # Make prediction
        sentiment, confidence = predict_sentiment(text)
        
        # Return result
        return jsonify({
            'text': text,
            'sentiment': sentiment,
            'confidence': f"{confidence:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
