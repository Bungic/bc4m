from flask import Flask, request, jsonify
import logging
import os

api = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@api.before_request
def log_request_info():
    logging.info('Request: %s %s', request.method, request.url)

@api.after_request
def log_response_info(response):
    logging.info('Response: %s %s', response.status, response.response)
    return response

# Root endpoint
@api.route('/', methods=['GET'])
def root():
    return jsonify({"msg": "BC4M"})

# Health check endpoint
@api.route('/health', methods=['GET'])
def health():
    # Simple health check
    return jsonify({"status": "healthy"})

# POST endpoint
@api.route('/', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    return jsonify(data)

if __name__ == '__main__':
    api.run(host=os.getenv('FLASK_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_PORT', 5000)))
