from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fatorial/<int:number>', methods=['GET'])
def calcular_fatorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return jsonify({'fatorial': result})

if __name__ == '__main__':
    app.run()
