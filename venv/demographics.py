from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json

imgurl = input("Input image URL.\n")

app = ClarifaiApp(api_key='60a12430f9ca4d2c855ce51a475662ef')
model = app.models.get('demographics')

try:
    image = ClImage(url=imgurl)
    data = model.predict([image])
except:
    print("Invalid entry. Make sure the input is an image URL which contains only one face that is clearly visible.")

def getData(data):
    nData = data
    nData = nData['outputs']
    nData = nData[0]
    nData = nData['data']
    nData = nData['regions']
    nData = nData[0]
    nData = nData['data']
    nData = nData['concepts']
    age = nData[0]['name']
    gender = nData[20]['name']
    ethnicity = nData[22]['name']
    demographics = {'age': age, 'gender': gender, 'ethnicity' : ethnicity}
    return demographics

results = getData(data)
print(results)

with open('results.txt', 'w') as r:
    json.dump(results, r, sort_keys=True)

input()
