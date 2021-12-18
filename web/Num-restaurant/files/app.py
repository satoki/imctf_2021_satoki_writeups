import os
import random
import subprocess
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__)

def sanitize_price(price):
    if not price.isnumeric():
        return "10000000"
    return price

def sanitize_meal(meal):
    if not meal.isascii():
        return "Kasumi"
    #Is it possible to block XSS?
    return "".join([c for c in meal if ord(c) > 0x1f]).replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("http", "num")

@app.route("/")
def num_restaurant():
    niku = random.randint(1, 1000000)
    sushi = random.randint(1, 1000000)
    yasai = random.randint(1, 1000000)
    price = request.args.get("price")
    meal = request.args.get("meal")
    if (not price) or (not meal):
        script = ''
    else:
        script = f'''<script>
var text = "￥{sanitize_price(price)}{sanitize_meal(meal)}😋Yummy!!";
alert(text);
</script>
'''
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<title>Num-restaurant</title>
{script}
</head>
<body>
<h1>Welcome to Num-restaurant 🔥</h1>
<a href="?price={niku}&meal=Niku"><p style="font-size:200%;">￥{niku} / Niku🍖</p></a>
<a href="?price={sushi}&meal=Sushi"><p style="font-size:200%;">￥{sushi} / Sushi🍣</p></a>
<a href="?price={yasai}&meal=Yasai"><p style="font-size:200%;">￥{yasai} / Yasai🥗</p></a>
</body>
</html>
"""
    if request.args.get("encoding") == "shift_jis":
        return Response(html, content_type='text/html; charset=shift_jis')
        #No one uses it anymore, but I implemented it because I was born in 1997 and missed it.
    else:
        return Response(html, content_type='text/html; charset=utf-8')


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return """
<!DOCTYPE html>
<html lang="ja">
<head>
<title>Give the food to Admin !!</title>
</head>
<body>
<h1>Give the food to Admin !!</h1>
<form action="/admin" method="post">
Query: 
<input type="text" style="width:100px;" id="price" name="price" placeholder="10000">
<input type="text" style="width:100px;" id="meal" name="meal" placeholder="Niku">
<input type="hidden" id="encoding" name="encoding" value="utf-8">
<button type="submit">Submit</button>
</form>
</body>
</html>
"""
    else:
        url = f'http://160.251.83.96:31415?price={urllib.parse.quote(request.form["price"])}\
&meal={urllib.parse.quote(request.form["meal"])}\
&encoding={urllib.parse.quote(request.form["encoding"])}'
        try:
            flag = os.getenv("FLAG")
            cmd = f'chromium-browser --no-sandbox --headless --disable-gpu "{url}&flag={flag}"'
            subprocess.run(cmd, shell=True, timeout=3)
        except:
            return "Admin🥰Yummy!!"
        return "Admin🤤Yucky!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=23141)