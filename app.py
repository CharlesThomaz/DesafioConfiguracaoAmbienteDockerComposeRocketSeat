from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Endpoint /hello funcionando!"})

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "status": "success",
        "message": "Endpoint /info funcionando!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)