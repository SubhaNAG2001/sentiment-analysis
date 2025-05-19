# Sentiment Analysis Web Application

A web application that analyzes the sentiment of text using machine learning. The application provides both a user-friendly web interface and an API for integration with other systems.

## Features

- Text sentiment analysis (Positive, Negative, Neutral)
- Confidence score for predictions
- History of recent analyses
- RESTful API for integration
- Responsive web interface

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Machine Learning**: scikit-learn, NLTK
- **Production Server**: Waitress

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Install required packages:
   ```
   pip install flask waitress nltk joblib scikit-learn
   ```

3. Download NLTK resources:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

## Usage

### Running the Application

#### Development Mode
```
python app.py
```

#### Production Mode
```
python run.py
```

The application will be available at `http://localhost:5000`.

### Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Enter text in the provided text area
3. Click "Analyze Sentiment"
4. View the sentiment result and confidence score
5. Recent analyses will be displayed in the history section

### API Usage

The application provides a RESTful API endpoint for sentiment analysis:

**Endpoint**: `/api/sentiment`
**Method**: POST
**Content-Type**: application/json

**Request Body**:
```json
{
  "text": "Your text to analyze"
}
```

**Response**:
```json
{
  "text": "Your text to analyze",
  "sentiment": "Positive",
  "confidence": "85.75%"
}
```

**Example using curl**:
```
curl -X POST http://localhost:5000/api/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text":"This is a great product, I love it!"}'
```

**Example using Python requests**:
```python
import requests
import json

url = "http://localhost:5000/api/sentiment"
data = {"text": "This is a great product, I love it!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)
result = response.json()
print(result)
```

## Configuration

You can modify the application settings in `config.py`:

- `DEBUG`: Set to `True` for development, `False` for production
- `HOST`: The host address to bind to
- `PORT`: The port to listen on
- `API_RATE_LIMIT`: Maximum number of API requests per minute

## Model Information

The sentiment analysis model is trained on a dataset of tweets. It uses:

- TF-IDF vectorization for feature extraction
- Logistic Regression for classification
- NLTK for text preprocessing

## Project Structure

```
sentiment-analysis/
├── app.py                 # Main Flask application
├── run.py                 # Production server script
├── config.py              # Configuration settings
├── sentiment_model.pkl    # Trained ML model
├── tfidf_vectorizer.pkl   # TF-IDF vectorizer
├── model.ipynb            # Jupyter notebook for model training
├── templates/
│   └── index.html         # Web interface template
└── README.md              # This file
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.