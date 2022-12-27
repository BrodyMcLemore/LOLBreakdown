import os

if not os.path.exists(os.getcwd()+"/Output"):
    os.mkdir(str(os.getcwd()+"/Output"))
else:
    print("/Output exists")
