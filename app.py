from flask import Flask, render_template, request, jsonify
from viga_calculations import calcular_viga

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.json
    resultados = calcular_viga(datos)
    return jsonify(resultados)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()

