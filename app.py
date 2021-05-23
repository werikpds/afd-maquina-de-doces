from flask import Flask, jsonify, request
from afd import afd
from elevador import vai_para
from flask_cors import CORS
from analisador import analise

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Hello", 200

@app.route('/doce', methods=['POST'])
def doce():
    data = request.get_json()
    print(data["dinheiro"])
    return afd(data["dinheiro"]) , 200

@app.route('/elevador', methods=['POST'])
def elevador():
    data = request.get_json()
    print(data["andares"])
    return vai_para(data["andares"]) , 200

@app.route('/analisador', methods=['POST'])
def analisador():
    data = request.get_json()
    print(data["bloco"])
    return analise(data["bloco"]) , 200

if __name__ == '__main__':
    app.run(debug=True)
