import os
def shutdown():
    print("Shutting down the computer...")
    os.system("shutdown /s /t 0")
shutdown()