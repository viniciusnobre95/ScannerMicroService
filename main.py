import base64
import io
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from scripts.birdViewTransform import transform

app = Flask(__name__)

@app.route('/')
def home():
    return '''Server Works!<hr>
<form action="/birdView/" method="POST" enctype="multipart/form-data">
<input type="file" name="foto">
<button>OK</button>
</form>'''

@app.route('/birdView/', methods=['POST', 'GET'])
def birdView():
    # Pegando arquivo da requisição post
    file = request.files['foto']
    print(file)
    # Abrindo imagem através do pillow
    image_pillow = Image.open(file)
    print(image_pillow)
    # Colocando em um formato que possa ser utilizado pelo opencv
    image_opencv_format = np.array(image_pillow)
    
    image_warped = transform(image_opencv_format)

    image_final = Image.fromarray(image_warped)
    
    buffer = io.BytesIO()
    image_final.save(buffer, 'png')
    buffer.seek(0)
    
    data = buffer.read()
    data = base64.b64encode(data).decode() # Codificando imagem para ser retornada
    
    return jsonify({
                'msg': 'success', 
                'size': [image_final.width, image_final.height], 
                'format': image_final.format,
                'img': data
           })


app.run(debug=True) 
