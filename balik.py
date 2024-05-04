# Enter script code
from time import sleep
import os
# System Conf
SEND_MODE:int=1
SLEEP:float=0.2
RUN:bool=True

# Log Conf
DEFAULT_LOG_DIR:str="/home/faruk/Documents/GTA San Andreas User Files/SAMP/logs/"
LOG_NAME:str=""

# Yem Conf
NO_YEM_MSG:str=""

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
        with open(logfile,"r") as file:
            last_line=str(file.readlines()[-1]).encode(encoding="iso-8859-9")
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
    

def main(run:bool=RUN):
    LOG_NAME=get_last_modified_log_file()
    while run:
        send_text("/baliktut")
        sleep(29)
        if (NO_YEM_MSG==""):
            pass
        elif ((read_last_log_line()==str(NO_YEM_MSG))): # add global env var to disable/enable script
            RUN=False
    
    
main()
