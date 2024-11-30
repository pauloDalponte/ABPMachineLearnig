from flask import Flask, request, jsonify
from joblib import load  
from flask_cors import CORS 
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd



app = Flask(__name__)
CORS(app) 

modelo, ref_cols, target = load(r'C:\Users\DalpTecnologia\Documents\ABPMachineLearnig\models\model_nota_REDACAO.pkl')
print(f"Modelo: {modelo}")
print(f"Colunas de referência: {ref_cols}")
print(f"Coluna alvo: {target}")

ordinal = OrdinalEncoder()

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.json
    try:
        dados = request.json

        if not isinstance(dados, dict):
            return jsonify({'erro': 'Os dados enviados devem estar no formato JSON'}), 400

        entrada_df = pd.DataFrame([dados], columns=ref_cols)
        
        columns_to_convert = entrada_df.select_dtypes(include=['object', 'bool']).columns
        entrada_df[columns_to_convert] = ordinal.fit_transform(entrada_df[columns_to_convert])

        previsao = modelo.predict(entrada_df)

        return jsonify({'nota': previsao[0]})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)
