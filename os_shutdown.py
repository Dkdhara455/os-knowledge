import os
shutdown=input("shutdown your pc ?yes or no")
if shutdown=="no":
    exit()
else:
    os.system("shutdown /s /t 5")
