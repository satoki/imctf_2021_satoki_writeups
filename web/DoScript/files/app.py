import os
import subprocess
import urllib.parse
from flask import Flask, request

app = Flask(__name__)

def js_sanitize(text):
    #I've heard that this is enough to sanitize special characters in JavaScript.
    return "".join([c for c in text if ord(c) > 0x1f]).replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'").replace("/", "\\/")

@app.route("/")
def doscript():
    name = request.args.get("name")
    if not name:
        name = 'Nagoya-Hacker'
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<title>DoScript</title>
<ScRiPt>
//Hack! Hack! Hack!
alert("Hacked by {js_sanitize(name)}!!");
alert("Is there any way to turn off the alerts?");
alert("Hehehehehe");
</ScRiPt>
</head>
<body>
<h1>DoScript</h1>
This site is a perfectly safe site that will not be hacked.<br>
It cannot be tampered with by a hacker!!!<br>
👻<br>
<a href="/tamperchecker">Tamper Checker 🧐</a><br>
</body>
</html>
"""
    return html


@app.route("/tamperchecker", methods=["GET", "POST"])
def tamperchecker():
    mysite = "http://118.27.104.46:31416/"
    if request.method == "GET":
        return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<title>Tamper Checker 🧐</title>
</head>
<body>
<h1>Tamper Checker 🧐</h1>
<form action="/tamperchecker" method="post">
<label for="url">URL: </label>
<input type="text" style="width:350px;" id="url" name="url" placeholder="{mysite}?name=Nagoya-Hacker">
<button type="submit">Submit</button>
</form>
</body>
</html>
"""
    else:
        url = request.form["url"]
        if f"{mysite}?name=" != url[0:len(mysite + "?name=")]:
            return "Not my site!"
        if len(url) > 100:
            return "URL is too long!"
        url = f"{mysite}?name=" + urllib.parse.quote(url.replace(f"{mysite}?name=", ""))
        try:
            cmd = f'chromium-browser --no-sandbox --headless --disable-gpu "{url}"'
            subprocess.run(cmd, shell=True, timeout=3)
        except:
            return 'This site has been hacked 👾'#Alerts are detected.
        return f'This site has not been hacked 👻\nFlag:{os.getenv("FLAG")}'#No alerts are detected.

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=23142)