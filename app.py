from joblib import load
from flask import render_template, jsonify

app = Flask(__name__)

# Loads a model previously saved 
path_to_model = "Models/"
model_name = 'lr-pipe_8feat.joblib'
model = joblib.load(path_to_model + model_name)

@app.route('/')
def home():
   print('donner une consigne ici')
   return render_template('index.html')



@app.route('/predict/')
def classif():
    return jsonify({
      'classe': 'crédit accordé', 
      'probabilité de défaut de paiement': 0.2
    })


if __name__ == '__main__':
   app.run()














