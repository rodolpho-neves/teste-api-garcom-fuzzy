# bibliotecas necessarias para a aplicacao
from flask import Flask, request, Response
#import os

# carregando o arquivo do modelo
from garcom.FuzzyModel import *

# declarando o modelo
model = FuzzyModelGorjeta()


app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def index():
#    #nota_json = request.get_json()
#    response = model.model_predict(8, 2)
#    return f"Teste das notas servico=8 e comida=2, gorjeta: {response}"

@app.route('/fuzzygorjeta/predict', methods=['POST'])
def predict():
    nota_json = request.get_json()

    if nota_json:
        response = model.model_predict(nota_json['servico'], nota_json['comida'])
        return response
    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=False)