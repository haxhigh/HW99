import os
from datetime import datetime

dt1 = datetime.now()
dt = datetime.timestamp(dt1)

cwd = os.getcwd()

the_dir = "C:/Users/iliea/OneDrive/Pictures/Screenshots"
change_dir = os.chdir(the_dir)

cwd = os.getcwd()

list_dir = os.listdir(cwd)

count = 0
for files in list_dir:
    last_modi =os.path.getctime(files)
    dt_obj = datetime.fromtimestamp(last_modi)
    print(last_modi)

    if (dt-last_modi) >= 2592000:
        print(files)
        print("This file has not been modified for 30 days.")
        os.unlink(files)
        print(f"{files} removed.") 