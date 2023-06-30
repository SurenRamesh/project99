import time
import os
import shutil

firstpath = input("Enter the path: ")
time1 = int(input("Enter a time: "))

def Gateway():
    if os.path.exists(firstpath):
        seconds = time.time(time1)
        pathway = os.walk(firstpath)
        ctime = os.stat(pathway).st_ctime
        if ctime > seconds:
            if os.path.isfile(firstpath):
                os.remove(firstpath)
            else:
                shutil.rmtree(firstpath)

    else:
        print("Not found :D")
    


Gateway()
    
