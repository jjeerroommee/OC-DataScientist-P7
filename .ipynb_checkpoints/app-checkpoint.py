import joblib
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict/')
def classif():

    # Loads a model previously saved 
    path_to_model = "./models/"
    model_name = 'lr-pipe_8feat.joblib'
    model = joblib.load(path_to_model + model_name)
    
    return jsonify({
      'classe': 'crédit accordé', 
      'probabilité de défaut de paiement': 0.2
    })


if __name__ == '__main__':
   app.run()














