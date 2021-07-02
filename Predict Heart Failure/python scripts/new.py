import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "iCtSN6ILgqr5TlSlYEhkzxSBRVM_PAwFbtjzCMmM4y22"
token_response = requests.post('https://iam.ng.bluemix.net/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data": [ {"field": [["G1","G2","G3","CreditScore","Gender","Age","Tenure",	"Balance",	"NumOfProducts",	"HasCrCard",	"IsActiveMember",	"EstimatedSalary"]],
                   "values": [[1, 0, 0, 62348600,
       1, 327890000, 60009900, 30,
       2000000, 100055000, 100880000, 1790932]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7753c081-b55b-4021-a33c-bf6165aed208/predictions?version=2020-12-26', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]

if(pred == 0):
    print("he will not get exited")
    
else:
    print("he gets exited")