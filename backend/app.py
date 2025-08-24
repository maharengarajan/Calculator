from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import Calculator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

calc = Calculator()

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    if not data or 'expression' not in data:
        return jsonify({'error': 'No expression provided'}), 400
    
    expression = data['expression']
    
    try:
        result = calc.evaluate(expression)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Calculation error: {str(e)}'}), 500

@app.route('/api/operations', methods=['GET'])
def get_operations():
    operations = [
        {'name': 'Addition', 'symbol': '+', 'example': '5 + 3'},
        {'name': 'Subtraction', 'symbol': '-', 'example': '5 - 3'},
        {'name': 'Multiplication', 'symbol': '*', 'example': '5 * 3'},
        {'name': 'Division', 'symbol': '/', 'example': '10 / 2'},
        {'name': 'Power', 'symbol': '**', 'example': '2 ** 3'},
        {'name': 'Square Root', 'symbol': 'sqrt', 'example': 'sqrt(9)'}
    ]
    return jsonify(operations)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)