import joblib
import os
import pandas as pd
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


@app.route('/')
def home():
    #print("hello home")
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def classif():
    # Loads a model previously saved 
    model = joblib.load(os.path.join('models', 'lr-pipe_8feat.joblib'))
        
    #getting an array of features from the post request's body
    data_json = request.get_json()
    data = pd.DataFrame(data_json['inputs'])

    
    #creating a response object
    proba_echec = model.predict_proba(data)[0][1]

    if proba_echec > 0.5 :
        classe = 'refusé'
    else :
        classe = 'accepté'
    
    #returning the response object as json
    return jsonify({
        'classe': classe, 
        'proba_echec': proba_echec
    })


if __name__ == '__main__':
   app.run()














