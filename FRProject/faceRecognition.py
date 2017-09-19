import numpy as np
import os
import operator
import numpy as np
import face_recognition
import base64
from flask import Flask, jsonify, request, redirect,render_template

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    res1 = 'dataImg/Shahrukh Khan/7.jpeg'
    info1 = 'Some Information'
    imgPath = 'static/demoImg/defaultImg.jpg'
    per1 = 57 
    filename = "shahrukhanDuplicate.jpg"
    pageName = 'firstPage.html' 
    if request.method == 'POST':
	info1 = ''
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
	    imgPath = "data:imagejpg;base64," + base64.b64encode(file.read())
	    filename = file.filename
            (res1,per1) =  detect_faces_in_image(file)
	    pageName = 'secondPage.html'
    hname1 = res1.split('/')[2]	   
    return render_template(pageName , fname=filename.split('.')[0],res = res1 , info = info1, imgpath = imgPath , per = per1 , hname = hname1) 

def detect_faces_in_image(file_stream):
        fp = open("img_path.txt")
        images =[i[:-1] for i in fp.readlines()]
        fp.close()

        fp = open("faces_encoding.txt")
        known_faces = [ np.array([np.float32(i) for i in enc[1:-2].split()]) for enc in fp.readlines()]
        fp.close()

        check_image = face_recognition.load_image_file(file_stream)
        unknown_face_encoding = face_recognition.face_encodings(check_image)[0]

        results =face_recognition.face_distance(known_faces, unknown_face_encoding)
        rs = results.argsort()
        return ('static/'+images[rs[0]],int(round((1-results[rs[0]])*100)))

if __name__ == "__main__":
     app.run(debug=True)
