import numpy as np
import cv2
import picamera
from num2words import num2words
from subprocess import call


camera = picamera.PiCamera()
rawCapture=PiRGBArray(camera)
time.sleep(0.5)
cv2.waitKey(0)

camera.start_preview()

camera.capture(‘snapshot.jpg’)

camera.stop_preview()

image_input = cv2.imread("snapshot.jpg")
image_height, image_width, image_depth = image_input.shape
content_total = image_height*image_width

print("TOTAL PIXELS:")
print (content_total)

cv2.imshow("Input Image", image_input)

print (" RGB PIXELS RESPECTIELY:")

#RED MASKING

mask_red = cv2.inRange(image_input, np.array([0,0,10]), np.array([80,80,255]))
content_red = cv2.countNonZero(mask_red)

print(content_red)

#cv2.imshow("red masked image", mask_red)
#cv2.waitKey(0)




#GREEN MASKING

mask_green = cv2.inRange(image_input, np.array([0,10,0]), np.array([80,255,80]))
content_green = cv2.countNonZero(mask_green)

print(content_green)

#cv2.imshow("green masked image", mask_green)
#cv2.waitKey(0)


#BLUE MASKING

mask_blue = cv2.inRange(image_input, np.array([10,0,0]), np.array([255,80,80]))
content_blue = cv2.countNonZero(mask_blue)

print(content_blue)

#cv2.imshow("Blue masked image", mask_blue)
#cv2.waitKey(0)


#CALCULATIONS
red_percent = (content_red * 100)/content_total

green_percent = (content_green * 100)/content_total

blue_percent = (content_blue * 100)/content_total


if red_percent > green_percent and red_percent > blue_percent:
    text="The object is red"
    print("The object is red")

if green_percent > red_percent and green_percent > blue_percent:
    text="The object is green"
    print("The object is green")

if blue_percent > green_percent and red_percent < blue_percent:
    text="The object is blue"
    print("The object is blue")



cmd_beg= 'espeak '
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file


#Replacing ' ' with '_' to identify words in the text entered
text = text.replace(' ', '_')

#Calls the Espeak TTS Engine to read aloud a Text
call([cmd_beg+cmd_out+text+cmd_end], shell=True)

    
