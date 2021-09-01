#Importing the requisite libraries
import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0) #Starting video capture
def nothing(x):
    pass
cv.namedWindow("trackbar") 
#Finding the lower and upper HSV values of object to be tracked
cv.createTrackbar("LH","trackbar",0,179,nothing)
cv.createTrackbar("LS","trackbar",0,255,nothing)
cv.createTrackbar("LV","trackbar",0,255,nothing)
cv.createTrackbar("UH","trackbar",179,179,nothing)
cv.createTrackbar("US","trackbar",255,255,nothing)
cv.createTrackbar("UV","trackbar",255,255,nothing)

while(True):
    ret,frame=cap.read() #Reading frames from camera
    frame=cv.flip(frame,1) #Flips the frame horizontally
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV) #Converting BGR to HSV
    
    #Assigning trackbar values
    lh=cv.getTrackbarPos("LH","trackbar")
    ls=cv.getTrackbarPos("LS","trackbar")
    lv=cv.getTrackbarPos("LV","trackbar")
    hh=cv.getTrackbarPos("UH","trackbar")
    hs=cv.getTrackbarPos("US","trackbar")
    hv=cv.getTrackbarPos("UV","trackbar")
    #Creating an array of the HSV values
    lower = np.array([lh,ls,lv])
    higher = np.array([hh,hs,hv])
   
   #Creating a mask 
    mask = cv.inRange(hsv,lower,higher) 
    output = cv.bitwise_and(frame,frame,mask=mask) #Combining the frames and the mask  
    cv.imshow("output",output) #Displaying the trackbar with mask aplied
    key = cv.waitKey(1) #Delay of 1 millisecond to wait for user input
    #if esc pressed exit
    if key == 27:
        break
#Releases the capture and breaks all the open windows
cap.release()
cv.destroyAllWindows()