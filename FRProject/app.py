import numpy as np
import os
import operator
import numpy as np
import face_recognition
import base64
from base64 import decodestring
import random
from StringIO import StringIO
from flask import Flask, jsonify, request, redirect,render_template

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
	imgPath = request.form['t1']
        if 'file' not in request.files and imgPath=='':
            return redirect(request.url)
	filename=''
        if imgPath!='':
		(imgPath,filename)=imgPath.split('#')
	else:
            file = request.files['file']
	    imgPath = "data:imagejpg;base64," + base64.b64encode(file.read())
	    filename = file.filename
	    
	fh = StringIO()
	fh.write(str(imgPath.split(",")[1].decode('base64')))
        (res1,per1,hname1) =  detect_faces_in_image(fh)
        fh.close()
    	return render_template('onePage.html' , fname=filename.split('.')[0],res = res1 , imgpath = imgPath , per = per1 , hname = hname1) 
    else:
    	listDup = os.listdir('static/duplicates')
    	filename = listDup[random.randint(0,len(listDup)-1)]
    	imgPath = 'static/duplicates/'+filename
        (res1,per1,hname1) =  detect_faces_in_image(imgPath)
    	return render_template('onePage.html' , fname=filename.split('.')[0],res = res1 , imgpath = imgPath , per = per1 , hname = hname1) 

def detect_faces_in_image(file_stream):
        fp = open("img_path.txt")
        images =[i[:-1] for i in fp.readlines()]
        fp.close()

        fp = open("faces_encoding.txt")
        known_faces = [ np.array([np.float32(i) for i in enc[1:-2].split()]) for enc in fp.readlines()]
        fp.close()

        check_image = face_recognition.load_image_file(file_stream)
        unknown_face_encoding = face_recognition.face_encodings(check_image)
	
	if unknown_face_encoding == []:
		return ("static/backgorundImg/wrong.jpg",0,'Uploaded Image has No Face Detect Plese Select Single Face Image')
	elif len(unknown_face_encoding)>1:
		return ("static/backgorundImg/wrong.jpg",0,'Uploaded Image has Multiple Face Detect Plese Select Single Face Image')
		
        results =face_recognition.face_distance(known_faces, unknown_face_encoding[0])
        rs = results.argsort()
        return ('static/'+images[rs[0]],int(round((1-results[rs[0]])*100)),images[rs[0]].split('/')[1])

if __name__ == "__main__":
     app.run(port=5001,debug=True)
