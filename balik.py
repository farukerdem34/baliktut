# Enter script code
from time import sleep
import os
# System Conf
SEND_MODE:int=1
SLEEP:float=0.2
RUN:bool=store.get_global_value('RUN')     


# Log Conf
DEFAULT_LOG_DIR:str="/home/faruk/Documents/GTA San Andreas User Files/SAMP/logs/"
HOME_DIR="/home/faruk/Documents/AutoKeyScripts/"
LOG_NAME:str=""
# /timestamp ile oynamıyorsanız False yapın
TIME_STAMP_ON=True

# Yem Conf
NO_YEM_MSG:str="Balık tutmadan önce balıkçı kulübesinden yem satın almalısınız."

# Limit Conf
LIMIT_STR:str="Yavaş salla oltayı, denizde balık bırakmadın! ((Limite ulaşıldı, biraz dinlen.))"

# KDE-Connect Conf
DEVICE_ID="2087ca79_a6d9_45cb_8136_6b2fa43eddb6"

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


def send_msg_to_android(msg:str):
    cmd=f"kdeconnect-cli --device={DEVICE_ID} --ping-msg='{msg}'"
    os.system(cmd)
    return cmd


def main(run:bool=RUN):
    if TIME_STAMP_ON:
        start_index=24
    else:
        start_index=13
    while run:
        run=store.get_global_value('RUN')
        if not run:
            quit('Çıkış yapıldı.')
        send_text("/baliktut")
        sleep(29)
        if (NO_YEM_MSG==""):
            pass
        elif ((read_last_log_line(log_name=get_last_modified_log_file())[start_index:-2]==str(NO_YEM_MSG))): # add global env var to disable/enable script
            run=False
            msg:str='Yem Bitti'
            cmd=f"kdeconnect-cli --device={DEVICE_ID} --ping-msg='{msg}'"
            send_msg_to_android(msg)
            quit(msg)
        if read_last_log_line(log_name=get_last_modified_log_file())[24:-2]==LIMIT_STR:
            run=False
            msg:str='Saatlik limit doldu'
            cmd = send_msg_to_android(msg)
            quit(msg)
        
    
main()
