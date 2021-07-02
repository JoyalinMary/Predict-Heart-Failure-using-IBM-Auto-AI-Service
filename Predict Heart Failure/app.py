import numpy as np
from flask import Flask, request, jsonify, render_template
import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "RyRxnYkTnQcStWr68PJjuDfpl0vp2u8f5VQaBqZc5ifA"
token_response = requests.post('https://iam.eu-gb.bluemix.net/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    AVGHEARTBEATSPERMIN = request.form["AVGHEARTBEATSPERMIN"]
    PALPITATIONSPERDAY = request.form["PALPITATIONSPERDAY"]
    CHOLESTEROL = request.form["CHOLESTEROL"]
    BMI = request.form["BMI"]
    SEX = request.form["SEX"]
   
    FAMILYHISTORY = request.form["FAMILYHISTORY"]
    SMOKERLAST5YRS = request.form["SMOKERLAST5YRS"]
    Age = request.form["Age"]
    EXERCISEMINPERWEEK = request.form["EXERCISEMINPERWEEK"]


    t = [[int(AVGHEARTBEATSPERMIN),int(PALPITATIONSPERDAY),int(CHOLESTEROL),int(BMI),str(SEX),str(FAMILYHISTORY),str(SMOKERLAST5YRS),int(Age),int(EXERCISEMINPERWEEK)]]
    print(t)
    payload_scoring = {"input_data": [ {"field": [["AVGHEARTBEATSPERMIN","PALPITATIONSPERDAY","CHOLESTEROL","BMI","SEX","FAMILYHISTORY","SMOKERLAST5YRS","Age","EXERCISEMINPERWEEK"]],
                   "values": t}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/e5e8ad95-8348-441a-8acd-374bb5a33c78/predictions?version=2021-06-27', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    print(predictions)
    pred = predictions['predictions'][0]['values'][0][0]
    
    return render_template('index.html', prediction_text= pred)


if __name__ == "__main__":
    app.run(debug=False)
