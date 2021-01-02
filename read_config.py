import configparser

#path of config file
CONFIG_FILE_PATH = 'config.ini'

def read_config():
    try:
        CONFIG_PATH = CONFIG_FILE_PATH
    except Exception:
        raise ValueError

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    BLACK = config["DATABASE"]["BLACK"]
    WHITE = config["DATABASE"]["WHITE"]
    GRAY = config["DATABASE"]["GRAY"]

    BLACK=convert_str_to_tuple(BLACK)
    WHITE = convert_str_to_tuple(WHITE)
    GRAY = convert_str_to_tuple(GRAY)

    return BLACK,WHITE,GRAY

def convert_str_to_tuple(str):
    temp=str.split(",")
    new_list=[]
    for i in range(len(temp)):
        new_list.append(int(temp[i]))
    return tuple(new_list)

BLACK,WHITE,GRAY=read_config()
print(type(WHITE))