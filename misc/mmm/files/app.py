import io
import os
import random
import subprocess
from flask_limiter import Limiter
from flask import Flask, request, send_file
from flask_limiter.util import get_remote_address

#<This is not a hint.>
#This challenge is unstable and may require multiple attempts.
#Sorry, once you've theorized about the flag acquisition, give it a few tries!

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["7 per minute"])#Tekito :) <- This is not a hint.

@app.route("/")
def mmm():
    flag = os.getenv("FLAG")
    data = request.args.get("data")
    if not data:
        data = "example.com"
    hehehe = random.randint(1, 100000000)
    data = "".join([c for c in data if c in "qwertyuiop@asdfghjklzxcvbnm"])
    cmd = f"google-chrome --no-sandbox --headless --disable-gpu \"http://{hehehe}{flag.replace('{', 'mmm').replace('}', '.')}{data}\""
    try:
        subprocess.run(cmd, shell=True, timeout=3)
    except:
        pass
    return "Can you get the server's traffic data?<br>Some well-known port numbers may be blocked."

@app.route("/<int:port>")
def get_the_port(port):
    if (port <= 65535) and (port >= 0) and (port != 22) and (port != 53) and (port != 80) and (port != 443):#No 22, 53, 80, 443 :)
        filename = random.randint(1, 100000000)
        os.makedirs("data", exist_ok=True)
        tcpdump = f"tcpdump -w data/{filename}.mmm port {port} -W1 -G5"#I've blocked the port numbers where you can get request data.
        try:
            subprocess.run(tcpdump, shell=True, timeout=6)
        except:
            try:
                os.remove(f"data/{filename}.mmm")
            except:
                pass
            return "There is no capture data."
        mmm = open(f"data/{filename}.mmm", "rb")
        data = io.BytesIO(mmm.read())
        mmm.close()
        os.remove(f"data/{filename}.mmm")
        return send_file(data, mimetype="application/octet-stream")
    else:
        return "0 <= port <= 65535 AND 22, 53, 80, 443 != port"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=23141)
