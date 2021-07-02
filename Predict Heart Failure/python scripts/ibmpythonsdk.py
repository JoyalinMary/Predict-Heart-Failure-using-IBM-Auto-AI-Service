import requests
import numpy as np

from PIL import Image


img = Image.open(r"E:\Training\Stanley\bear.jpg")
#img = image.load_img(,target_size = (64,64))
sm_img        = img.resize( ( 64, 64 ), Image.LANCZOS )

alpha_arr       = np.array( sm_img.split()[-1] )
norm_alpha_arr  = alpha_arr / 255
norm_alpha_list = norm_alpha_arr.reshape( 64,64 ).tolist()



# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "iCtSN6ILgqr5TlSlYEhkzxSBRVM_PAwFbtjzCMmM4y22"
token_response = requests.post('https://iam.ng.bluemix.net/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)



header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring =  { "values" : norm_alpha_list }
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/609f46a5-66f2-437e-b2c2-ad62b49dd861/predictions?version=2020-12-26', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")

print(response_scoring )


