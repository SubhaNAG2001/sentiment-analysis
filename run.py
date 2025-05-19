from waitress import serve
from app import app
import config

if __name__ == '__main__':
    print(f"Starting sentiment analysis service on {config.HOST}:{config.PORT}")
    print("Press Ctrl+C to quit")
    
    if config.DEBUG:
        # Use Flask's development server in debug mode
        app.run(host=config.HOST, port=config.PORT, debug=True)
    else:
        # Use Waitress in production
        serve(app, host=config.HOST, port=config.PORT, threads=4)