from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'Service is up and running'
    })

@app.route('/', methods=['GET'])
def hello_world():
    """Root endpoint that returns a welcome message."""
    return jsonify({
        'message': 'Hello, World!',
        'service': 'DevOps Sample Service',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)