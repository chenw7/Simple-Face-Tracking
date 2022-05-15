#This program does not recognize but instead, tracks the face of any user that is present in the live webcam feed. 
#As long as the necessary libraries (numpy and opencv) are installed on your computer, this program will run successfully.
#Author @Wei-cen Chen
#Version February 15, 2022

#Importing the necessary libraries to run the program
import numpy as np
import cv2

#Extracting information from an external program to create face cascades for this program
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

#Enabling webcam to operate when program operates
cap = cv2.VideoCapture(0)

#This is the main() of the program.
while (True):
    
    #Capture frame by frame
    ret, frame = cap.read()
    
    #Converting information from webcam feed into a grey scale photo for it to be better processed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 5)
    
    #Prints the x-coordinate, y-coordinate, width, and height of the rectangle that is drawn around the detected face
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        #Creates an image of the latest detected face in the folder you store this program
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        
        #Setting the color, stroke, and dimensions of the rectangle that will be drawn around the detected face
        color = (255, 0, 0) #BGR values 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
        
    #Display resulting frame
    cv2.imshow('frame',frame)
    
    #Press q to stop execution of the program
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
