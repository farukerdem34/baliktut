# Enter script code
from time import sleep
# System Conf
SEND_MODE:int=1
SLEEP:int=3
RUN:bool=True

# Log Conf
DEFAULT_LOG_DIR:str="/home/faruk/Documents/GTA San Andreas User Files/SAMP/logs/"
LOG_NAME:str=""

# Yem Conf
NO_YEM_MSG:str=""

def send_text(text:str):
    keyboard.send_key("t")
    keyboard.send_keys(text,send_mode=SEND_MODE)
    sleep(SLEEP)

def read_last_log_line(log_name:str=LOG_NAME,log_dir:str=DEFAULT_LOG_DIR):
    logfile:str=log_dir+log_name
    with open(logfile,"r") as file:
        last_line=str(file.readlines()[-1]).encode(encoding="iso-8859-9")
    return last_line


def main():
    while RUN:
        send_text("/baliktut")
        if ((read_last_log_line()==str(NO_YEM_MSG)) or (NO_YEM_MSG=="")): # add global env var to disable/enable script
            RUN=False
    