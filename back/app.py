from flask import Flask, request, jsonify
from joblib import load  
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

modelo, ref_cols, target = load(r'C:\Users\DalpTecnologia\Documents\ABPMachineLearnig\models\model_nota_REDACAO.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.json
    try:
       
        dados = request.json

        if not isinstance(dados, dict):
            return jsonify({'erro': 'Os dados enviados devem estar no formato JSON'}), 400

        entrada = list(dados.values())

        X_new = entrada[ref_cols]
        y_new = entrada[target]
        

        previsao = modelo.predict([X_new])
     
        return jsonify({'nota': previsao[0]})
    except Exception as e:
      
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)
