# Enter script code
from pytesseract import pytesseract
from PIL import ImageGrab
import string
import re
from time import sleep

ss_region = (1130, 490, 1183, 530)
ss_img = ImageGrab.grab(ss_region)
ss_img.show()