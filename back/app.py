from flask import Flask, request, jsonify
from joblib import load  

app = Flask(__name__)


modelo = load(r'C:\Users\paulocesar\Documents\Sistemas Bendo\ABPMachineLearnig\models\model_nota_REDACAO.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.json
    try:
       
        entrada = [
            dados['idade'],
            dados['salario'],
            dados['experiencia']
        ]
        
    
        previsao = modelo.predict([entrada])
        
     
        return jsonify({'nota': previsao[0]})
    except Exception as e:
      
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)
