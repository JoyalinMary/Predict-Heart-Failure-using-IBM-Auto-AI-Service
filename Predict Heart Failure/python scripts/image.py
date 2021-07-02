import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "iCtSN6ILgqr5TlSlYEhkzxSBRVM_PAwFbtjzCMmM4y22"
token_response = requests.post('https://iam.ng.bluemix.net/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
from keras.models  import load_model 
from keras.preprocessing import image
from numpy import asarray
import numpy as np
# load the image
img = image.load_img("cat.jpg",target_size = (64,64))
# convert image to numpy array
data = asarray(img)
x = np.expand_dims(data,axis = 0)
print(x.shape)

print(x)

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
"""payload_scoring = {"input_data": [ {"field": [["G1","G2","G3","CreditScore","Gender","Age","Tenure",	"Balance",	"NumOfProducts",	"HasCrCard",	"IsActiveMember",	"EstimatedSalary"]],
                   "values": [[1, 0, 0, 62348600,
       1, 327890000, 60009900, 30,
       2000000, 100055000, 100880000, 1790932]]}]}"""

#payload_scoring = {"input_data": [{"fields":['prediction', 'prediction_classes', 'probability'],"values": x.tolist()}]}
payload_scoring = {"values" : [[x.tolist() ]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/609f46a5-66f2-437e-b2c2-ad62b49dd861/predictions?version=2020-12-26', payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response",response_scoring)

#predictions = response_scoring.json()
#pred = predictions
#print(predictions)