# DoScriptð£

## åé¡æ
å®å¨ãªãµã¤ããä½ã£ãã®ã«ããã­ã³ã°ããã¦ãalertãåºãããã«ãªã£ã¦ãã¾ãã¾ãããå¹¸ããªãã¨ã«alertä»¥å¤ã®è¢«å®³ã¯ãªãããã§ããæ¹ç«ãã§ãã«ã¼ããã¾ããã¾ãããã­ï¼  
[http://118.27.104.46:31416/](http://118.27.104.46:31416/)  
[app.py](files/app.py)  

## é£æåº¦
**easy**  

## ä½åã«ããã£ã¦
ç´20,000ç¤¾ã§å©ç¨ããã¦ããããããµã¼ãã¹ã®ãå®éã®èå¼±æ§ã¨ãã¦å ±åãããã®ã§ãã  
è¬ã®ãµãã¿ã¤ãºã«ãã£ã¦XSSãçºç«ããªãããã«ãªã£ã¦ãã¾ããããèç©åã®DoSãè¡ãã¾ããã  
ãã®åé¡ã§ã¯æ±ã£ã¦ãã¾ãããããã£ãããµãã¿ã¤ãºããã¦ããªãå ´åã¯æ¹è¡ã³ã¼ããªã©ã«ãè¦æ³¨æã§ãã  

## è§£æ³
ãµã¤ãã«ã¢ã¯ã»ã¹ããã¨ãä½ããã¢ã©ã¼ããåºç¾ããã  
![alert.png](images/alert.png)  
ããã­ã³ã°ããã¦æ¹ç«ããã¦ãã¾ã£ãããã ã  
`/tamperchecker`ã§ã¯ãµã¤ãã®æ¹ç«ããã§ãã¯ã§ããããã ã  
åé¡æãããalertãåºãªãããã°ããããã ãããµã¤ãã½ã¼ã¹ãè¦ãã¨ä»¥ä¸ã®ããã«ãªã£ã¦ãã¦é£ããã  
```html
~~~
<ScRiPt>
//Hack! Hack! Hack!
alert("Hacked by Nagoya-Hacker!!");
alert("Is there any way to turn off the alerts?");
alert("Hehehehehe");
</ScRiPt>
~~~
```
éå¸ãããapp.pyãè¦ãã¨ä»¥ä¸ã®ããã§ã£ãã  
```python
~~~
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
~~~
```
`name`ã§ååãæå®ã§ãããã`\`ã`"`ã`'`ã`/`ããµãã¿ã¤ãºããã¦ããããã ã  
XSSããã®ã¯é£ãããDoSãèµ·ããã°ããã  
app.pyã§ã¯ä»¥ä¸ã®ããã«alertãçºçããªãå ´åãflagãæã«å¥ãã¨ããã¦ããã  
```python
~~~
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
            return 'This site has been hacked ð¾'#Alerts are detected.
        return f'This site has not been hacked ð»\nFlag:{os.getenv("FLAG")}'#No alerts are detected.
~~~
```
ãJSã§DoSããªã©èª¿ã¹ãã¨ã[JSã§DoSã/ Shibuya.XSS techtalk #11](https://speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-11)ãè¦ã¤ããããã  
ã©ãããæå­åãªãã©ã«ä¸­ã§`<!--<script>`ãå©ç¨ããã¨JSãå£ããä»æ§ãããããã ã  
JSãå£ããã¨alertã¯çºç«ããªãã  
`http://118.27.104.46:31416/?name=<!--<script>`ã`/tamperchecker`ã§éä¿¡ãã¦ããã°ããã  
![flag.png](images/flag.png)  
flagãå¾ãããã  

## imctf{d1d_y0u_f1nd_d05_by_570r3dx55?}
