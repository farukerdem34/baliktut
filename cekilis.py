# Enter script code
# Enter script code
import re
from time import sleep
import os
# System Conf
SEND_MODE:int=1
SLEEP:float=0.2
RUN:bool=store.get_global_value('RUN')     
# Log Conf
DEFAULT_LOG_DIR:str=os.getenv("DEFAULT_LOG_DIR")

HOME_DIR=os.getenv("HOME_DIR")

# Optional
LOG_NAME:str=""

# /timestamp ile oynamıyorsanız False yapın
TIME_STAMP_ON=bool(int(os.getenv("TIME_STAMP_ON")))


# KDE-Connect Conf
DEVICE_ID=os.getenv("DEVICE_ID")


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


file:str = DEFAULT_LOG_DIR+get_last_modified_log_file(log_dir=DEFAULT_LOG_DIR)
while store.get_global_value('RUN'):
    content=read_last_log_line(log_name=get_last_modified_log_file())
    regex=re.compile(r"\d\d\d\d\d\d\d\d\d\d")
    r=regex.search(content)
    if r is not None:
        kod=r.group()
        sleep(1.5)
        send_text("/vice "+str(kod))