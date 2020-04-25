import sys
import os
from datetime import datetime

def log_error(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    now_time = datetime.now()
    return f"""------- [{now_time}]:
File: {__file__}
[Error: {exc_type.__name__}]: {e} 
Line: {exc_tb.tb_lineno}

"""

def save_error(error_string):
    with open("Error.txt", "a") as fil:
        fil.write(error_string)
    
    print(error_string)

def errors():
    try:
        print("Paso 1")
        a, b, c = d
        # raise Exception("pepa Pig es mala")
    except Exception as e:
        save_error(log_error(e))


if __name__ == "__main__":
    errors()
