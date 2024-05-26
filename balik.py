# Enter script code
from time import sleep
import os
from pytesseract import pytesseract
from PIL import ImageGrab
import string
import re
# System Conf
SEND_MODE:int=1
SLEEP:float=0.2
RUN:bool=store.get_global_value('RUN') 
TEKNE:bool=True    


# Log Conf
DEFAULT_LOG_DIR:str=os.getenv("DEFAULT_LOG_DIR")

HOME_DIR:str=os.getenv("/home/faruk/Documents/AutoKeyScripts/")

# Optional
LOG_NAME:str=""

# /timestamp ile oynamıyorsanız False yapın
TIME_STAMP_ON:bool=bool(int(os.getenv("TIMESTAMP")))

# Yem Conf
NO_YEM_MSG:str="Balık tutmadan önce balıkçı kulübesinden yem satın almalısınız."

# Limit Conf
LIMIT_STR:str="Yavaş salla oltayı, denizde balık bırakmadın! ((Limite ulaşıldı, biraz dinlen.))"

# Kod Conf
KOD_STR:str="Lütfen dialog ekranına belirtilen kodu giriniz."
# KDE-Connect Conf
DEVICE_ID=os.getenv("DEVICE_ID")

def send_msg_to_android(msg:str,isKDECONNECT:bool=(DEVICE_ID!="")):
    cmd=f"kdeconnect-cli --device={DEVICE_ID} --ping-msg='{msg}'"
    os.system(cmd)
    return cmd

def send_text(text:str,send_mode:int=SEND_MODE,sleep_value:int=SLEEP):
    keyboard.send_key("t")
    keyboard.send_keys(text,send_mode=send_mode)
    sleep(sleep_value)
    keyboard.send_key(Key.ENTER)

def read_last_log_line(log_name:str=LOG_NAME,log_dir:str=DEFAULT_LOG_DIR):
    if log_name=="":
        return None
    elif log_name!=None:
        logfile:str=log_dir+log_name
        with open(logfile,"rb") as file:
            lines=file.readlines()
            last_line=lines[-1].decode('iso-8859-9')
        return last_line

def get_last_modified_log_file(log_dir:str=DEFAULT_LOG_DIR):
    lmlf:str=""
    lmlt=0
    for file_name in os.listdir(log_dir):
        file_path:str=os.path.join(log_dir,file_name)
        if os.path.isfile(file_path):
            modify_time=os.path.getmtime(file_path)
            if modify_time>lmlt:
                lmlt=modify_time
                lmlf=file_name
    return lmlf
    
def kod_gir(n:int=0):
    n=10
    while n>0:
        n-=1
        keyboard.send_key(Key.BACKSPACE)
        sleep(0.2)

    # x1,y1,x2,y2
    ss_region = (1130, 490, 1183, 530)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save("/tmp/test.jpg")

    control=True
    text = str(pytesseract.image_to_string(ss_img))
    for i in text:
        if i not in string.digits:
            text=text.replace(i,"")
    
    #regex=re.compile(r"\d\d\d\d\d\d")
    #while control:
    #    text = pytesseract.image_to_string(ss_img)
    #    dialog.info_dialog(text)
    #    r=regex.search(text)
    #    if r is not None:
    #        control=False
    
    keyboard.send_keys(text,send_mode=1)
    sleep(0.2)
    keyboard.send_keys(Key.ENTER)
    sleep(0.2)
    
        




def main(run:bool=RUN,tekne:bool=TEKNE):
    if TIME_STAMP_ON:
        start_index=24
    else:
        start_index=13
    while run:
        run=store.get_global_value('RUN')
        if not run:
            quit('Çıkış yapıldı.')
        if tekne:
            send_text("/teknebaliktut")
            sleep(11.5)
        else:
            send_text("/baliktut")
            sleep(29)
        
        if (NO_YEM_MSG==""):
            pass
        last_line=read_last_log_line(log_name=get_last_modified_log_file())
        if NO_YEM_MSG in last_line: # add global env var to disable/enable script
            run=False
            msg:str='Yem Bitti'
            send_msg_to_android(msg)
            quit(msg)
        # Timestamp açmak zorundalar
        elif LIMIT_STR in last_line:
            run=False
            msg:str='Saatlik limit doldu'
            send_msg_to_android(msg)
            quit(msg)
        elif KOD_STR in last_line:
            kod_gir()
            last_line=read_last_log_line(log_name=get_last_modified_log_file())
            if "Kodu hatalı girdiniz, lütfen doğru bir şekilde tekrar girin." in last_line:
                #if n>=5:
                run=False
                msg='Kod Girilmedi'
                send_msg_to_android(msg)
                quit(msg)
            sleep(11.5)
        
    
main()
