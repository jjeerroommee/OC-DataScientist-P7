import joblib
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    print("hello")
    print(os.listdir())
    return render_template('index.html')



@app.route('/predict/')
def classif():
    print(os.path.join('models', 'lr-pipe_8feat.joblib'))
    # Loads a model previously saved 
    model = joblib.load(os.path.join('models', 'lr-pipe_8feat.joblib'))
        
    return jsonify({
      'classe': 'crédit accordé', 
      'probabilité de défaut de paiement': 0.2
    })


if __name__ == '__main__':
   app.run()














