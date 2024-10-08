import requests
import base64
import constants

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Speechify API Key (if not in constants.py file)",
                    type=str, default=None)
args = parser.parse_args()

if(args.key == None):
    api_key = constants.API_KEY
else:
    api_key = args.key

text = "Hello World"

# to build the POST request, we use the API key in the header
#  and then can choose the data we want in the json data
#  of the request. Make sure to wrap text in the speak tags
url = "https://api.sws.speechify.com/v1/audio/speech"
headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "Authorization": api_key
}
data = {
    "input":f"<speak>{text}</speak>",
    "voice_id":"john",
    "audio_format":"mp3"
}

# Handle the actual request here, don't forget to convert the JSON
response = requests.post(url, headers=headers, json=data)
print(response)
responseJSON = response.json()

print(response)
print(responseJSON)

# The audio is a 64-bit encoded text string, we take that and convert
#  to bit string and save to file 
try:
   file_content=base64.b64decode(responseJSON['audio_data'])
   with open("Hello_world.mp3","wb") as f:
        f.write(file_content)
except Exception as e:
   print(str(e))
