import os
from math import sin, cos
from glob import glob
import os
import json
from PIL import Image, ImageOps
import math 
import os.path
import numpy as np
import sys
import cv2


#CHARACTER is a string with ASCII characters ordered with their brightness, Ñ is the lightest when using terminal/console 
# Different character sets that can be experemented with.
#CHARACTERS = " .',:;Il!i><~+_-?][1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#CHARACTERS = "                   @@@@@@@@@@@@%%%%%%%%#########********+++++++++====" 
#CHARACTERS= "             ====+++++++++********#########%%%%%%%%@@@@@@@@@@@@" #workes best for my background
CHARACTERS = "      _.,-=+:;cba!?0123456789$W#@Ñ" #more spaces will mean more black pixels, good for shodows?
#CHARACTERS = " Ñ" #black and white
#CHARACTERS= " 012345689"
#CHARACTERS= "                    _.,-=+:;cba!?0123456789$W#@Ñ"

#different sets depends on bg, best to not run in an editor

LENGTH = len(CHARACTERS)
cap = cv2.VideoCapture(0)

height = 120
width = 160
cap.set(3,120) #height
cap.set(4,160) # width

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gets each frame image as greyscale
    line = ""
    #renders each "frame"
    for i in range (0 , height,2): #this needs jump twice as often because the characters are alomst twice taller than they are wide
        # you can increase the jumps when iterating to lower resolution of the render (maintain the 2 to 1 ratio between height and width jumps)
        for j in range(width-1, 0,-1): #iterating backwards to flip image horizontally
            value = gray[i][j]
            asciichar = CHARACTERS[math.floor(((value/255)*LENGTH))-1]  # this finds how far along the grey
            line += asciichar
        line += "\n" #for each new line
    print(line, end= "\r") #prints frame to console,
     
    #os.system("cls") # old method, too slow 
    #cv2.imshow('webcam', frame) # shows live feed

    if (cv2.waitKey(30) == 27): # to close program if showing live feed
       break
cap.release()
cv2.destroyAllWindows()