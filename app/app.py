from flask import Flask, jsonify, request
from bad_practices import PoorlyDesignedClass, broad_exception_handling, parse_json_risky

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

@app.route('/bad-practices', methods=['POST'])
def use_bad_practices():
    """
    This endpoint intentionally uses bad coding practices
    to test code analysis pipelines
    """
    # Using the poorly designed class
    poor_class = PoorlyDesignedClass()
    
    # Getting data from request without validation
    data = request.json if request.json else {}
    
    # Unnecessary variables
    temp_val = data.get('value', 10)
    
    # Using function with broad exception handling
    broad_exception_handling()
    
    # Using function with risky type handling
    try:
        json_result = parse_json_risky('''{"name": "Test", "age": 30, "score": 100}''')
    except KeyError:
        json_result = "Error parsing JSON"
    
    # Using complex nested function from the class
    complex_result = poor_class.complex_function(1, 2, 3, 4, 5, 6)
    
    # Duplicated methods
    items = [5, 10, 15, 20]
    result1 = poor_class.duplicate_code_1(items)
    result2 = poor_class.duplicate_code_2(items)
    
    # Inconsistent variable naming
    userName = "TestUser"  # camelCase - inconsistent with Python conventions
    user_id = 12345  # snake_case
    
    # Magic numbers
    if temp_val > 42:  # Magic number
        status = "above threshold"
    else:
        status = "below threshold"
    
    return jsonify({
        'status': status,
        'complex_result': complex_result,
        'results': result1 + result2,
        'user': userName,
        'id': user_id,
        'json_data': json_result,
        'message': 'Bad practices endpoint called'
    })

if __name__ == '__main__':
    # Running with debug mode on - bad practice for production
    app.run(host='0.0.0.0', port=5000, debug=True)
