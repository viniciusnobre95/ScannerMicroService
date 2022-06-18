import base64
from io import BytesIO
import requests
import json
from PIL import Image

url = "http://127.0.0.1:5000/birdView/"

payload={}
files=[
  ('foto',('CPF.jpg',open('arquivosTeste/CPF.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
image_coded = json.loads(response.text)['img']

file = BytesIO(base64.b64decode(image_coded))

image = Image.open(file)
image.show()

