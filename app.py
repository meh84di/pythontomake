from flask import Flask, jsonify

app = Flask(__name__)

# Example function to return two numbers added
def calculate_sum(a, b):
    return a + b

@app.route('/run_script', methods=['GET'])
def run_script():
    sum_result = calculate_sum(5, 10)
    return jsonify({
        'sum_result': sum_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
