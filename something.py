import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from webscrape import findWord
import pydirectinput
import time

#get string from picture
def OCR(yest):
    custom_config = r'-l eng --oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(yest, config=custom_config)
    return text

#types a word from string?
def typeword(word):
    print(word)
    try:
        for letter in word:
            pydirectinput.write(letter)
    except TypeError:
        return("rbeoiwbghbewioh")
    pydirectinput.press('enter')
'''sing happy birthday to someone'''

#just loops. Too lazy to use while loop
for i in range(0,1000000):
    #parameters for color mask for text
    lower = np.array([10, 10, 30])
    upper = np.array([25, 25, 45])
    
    #grabs image where the roblox prompt is
    img1 = ImageGrab.grab(bbox=(200, 660, 480, 720))
    img2 = ImageGrab.grab(bbox=(200, 390, 480, 450))
    
    #img into numpy array
    img_np1 = np.array(img1)
    img_np2 = np.array(img2)
    
    #convers numpy image to grayscale
    frame1 = cv2.cvtColor(img_np1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(img_np2, cv2.COLOR_BGR2GRAY)
    
    #creates mask
    mask1 = cv2.inRange(img_np1, lower, upper)
    mask2 = cv2.inRange(img_np2, lower, upper)

    #inverts color
    mask1 = cv2.bitwise_not(mask1)
    mask2 = cv2.bitwise_not(mask2)
    
    #i copy and pasted this from somewhere on the internet
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break
    
    #grabs text from mask
    text1 = OCR(mask1)
    text2 = OCR(mask2)
    
    #formats text
    fragment1 = text1.strip().lower()
    fragment2 = text2.strip().lower()
    
    #finds word in Webscrape.py
    if len(fragment1) != 0:
        final1 = findWord(fragment1)
    if len(fragment2) != 0:
        final2 = findWord(fragment2)

    #types words
    try:
        print(fragment1)
        print(fragment2)
        typeword(final1)
        typeword(final2)
    except NameError:
        continue


cv2.destroyAllWindows()

