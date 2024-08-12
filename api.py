from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Request: %s %s', request.method, request.url)

@app.after_request
def log_response_info(response):
    logging.info('Response: %s %s', response.status, response.response)
    return response

# Root endpoint
@app.route('/', methods=['GET'])
def root():
    return jsonify({"msg": "BC4M"})

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    # Simple health check
    return jsonify({"status": "healthy"})

# POST endpoint
@app.route('/', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400  
    return jsonify(data)

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_PORT', 5000)))
