import face_recognition
import sys
import os
import operator

def trainImgData(dirPath):
	fp  = open("../img_path.txt","w")
	fp1 = open("../faces_encoding.txt","w")
	imgs = [ [imgD+"/"+img for img in os.walk(imgD).next()[2]] for imgD in [dirPath + '/' + imgDir for imgDir in os.walk(dirPath).next()[1]]]
	images = reduce(operator.concat,imgs)
	known_faces = []
	for img in images:
	     print img
	     known_faces.append(face_recognition.face_encodings(face_recognition.load_image_file(img))[0])
	[fp.write(imgPath+"\n") for imgPath in images]

	[fp1.write(str(enc).replace('\n','')+"\n") for enc in known_faces]
	fp.close()
	fp1.close()

trainImgData(sys.argv[1])
