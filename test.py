# Enter script code
from pytesseract import pytesseract
from PIL import ImageGrab
import string
import re
from time import sleep
def kod_gir()
    n=10
    while n>0:
        n-=1
        keyboard.send_key(Key.BACKSPACE)
        sleep(0.2)


    regex=re.compile(r"\d\d\d\d\d\d")
    # x1,y1,x2,y2
    ss_region = (1130, 490, 1183, 530)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save("/tmp/test.jpg")

    control=True
    text = str(pytesseract.image_to_string(ss_img))
    for i in text:
        if i not in string.digits:
            text=text.replace(i,"")
    #dialog.info_dialog(text)


    #while control:
    #    text = pytesseract.image_to_string(ss_img)
    #    dialog.info_dialog(text)
    #    r=regex.search(text)
    #    if r is not None:
    #        control=False
    #keyboard.send_key(Key.BACKSPACE)
    #keyboard.send_key(Key.BACKSPACE)
    #keyboard.send_key(Key.BACKSPACE)
    #keyboard.send_key(Key.BACKSPACE)
    #keyboard.send_key(Key.BACKSPACE)
    #keyboard.send_key(Key.BACKSPACE)
    keyboard.send_keys(text,send_mode=1)