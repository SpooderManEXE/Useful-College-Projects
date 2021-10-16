import cv2
import numpy as np
import face_recognition

img = face_recognition.load_image_file('basic images/Ambadi.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('basic images/Ambadi.2.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(img)[0] #prints 4 values
encodeface = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0] #prints 4 values
encodetest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0],faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeface],encodetest)
dis = face_recognition.face_distance([encodeface],encodetest)
print(results,dis)

#cv2.imshow("ambadi", img)
#cv2.imshow("test", imgTest)
cv2.waitKey(0)
