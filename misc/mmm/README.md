# mmm๐ฐ

## ๅ้กๆ
ๅ่ผฉใmใชใใกใใ๏ผใๆๅนใซใใใใใงใใใขใใฌในใใผใงๆค็ดขใใใใชใจ่จใใใพใใใๆๅณใๅใใใพใใใ  
URL1: [http://118.27.114.90:31417](http://118.27.114.90:31417/)  
URL2: [http://118.27.104.46:31417](http://118.27.104.46:31417/)  
โปใใฎๅ้กใฏใชใฏใจในใใ่คๆฐๅๆฝ่กใใใใจใ่จฑๅฏใใใฆใใพใใURL1ใURL2ใฎใฉใกใใ็จใใฆใๆงใใพใใใ้ใใชใใปใใใๅฉ็จใใ ใใใ  
[app.py](files/app.py)  

## ้ฃๆๅบฆ
**medium**  

## ไฝๅใซใใใฃใฆ
ใใฉใฆใถใฎใขใใฌในใใผใใๆค็ดขใ่กใใจmDNSใซใใฃใฆๆค็ดขใฏใผใใใฐใใใใจใใๆใใคใใพใใใ  
ใใใใCTFใงๆฑใใใใใจใใชใใงใใใไฝๅๆ้ใๅฐใชใใใฆใใใใๅ้ก่จญๅฎใซใชใฃใฆใใพใใ  
ใใฃใจใใพใใใใใใฃใ...ใ  

## ่งฃๆณ
ใตใคใใซใฏ่ฌใฎใกใใปใผใธใ่กจ็คบใใใใ ใใงใใใ  
```bash
$ curl http://118.27.114.90:31417
Can you get the server's traffic data?<br>Some well-known port numbers may be blocked.
```
้ๅธใใใapp.pyใ่ฆใใจไปฅไธใฎใใใงใใฃใใ  
```python
~~~
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
~~~
```
`/`ใงใฏ`google-chrome`ใง`http://ไนฑๆฐ+flagใฎ่จๅทใ็ฝฎๆใใใใฎ+dataใฏใจใชใใฉใกใผใฟ`ใซใขใฏใปในใใฆใใใ ใใงใใใ  
`/<int:port>`ใงใฏtcpdumpใงๅฅฝใใชใใผใใใญใฃใใใฃใงใใใใฎ็ตๆใ่ฟใใฆใใใใ  
ใใ ใใ`22`ใ`53`ใ`80`ใ`443`ใฏ็ฆๆญขใใใฆใใใ  
ๅ้กๆใซmใชใใกใใใจใใใใใใฉใฆใถใใขใใฌในใใผใๆค็ดขใGoogleๆค็ดขใใใจใ[ใใคใผใ](https://twitter.com/akira_you/status/1419228947766644736)ใใใใใใใ  
ใใฉใฆใถใฎใขใใฌในใใผใงๆค็ดขใใใจใmDNSใงๆค็ดขๆๅญๅใๆตๅบใใใใใ ใ  
mDNSใใผใใ่ชฟในใใจ5353ใงใใใใจใใใใใฎใงใใใใญใฃใใใฃใใใฐใใใ  
ใใใงๆณจๆใ ใใLinux็ฐๅขใงใฏ.localใงใชใๅ ดๅใmDNSใ็บใใใชใใใจใใใใฎใง`data=local`ใงๅฏพๅฟใใใฐใใใ  
`http://118.27.114.90:31417?data=local`ใซใขใฏใปในใใคใคใ`http://118.27.114.90:31417/5353`ใๅๅพใใใ  
ไธ้ฃใฎใชใฏใจในใใใsolver.shใใใใคใ่ตทๅใใใใจใง่กใใ  
```bash
$ ./solver.sh;./solver.sh
~~~
Saving to: โ5353โ

5353                          100%[=================================================>]     473  --.-KB/s    in 0s

2021-12-18 20:09:13 (6.31 MB/s) - โ5353โ saved [473/473]
~~~
Saving to: โ5353.1โ

5353.1                        100%[=================================================>]      25  --.-KB/s    in 0s

2021-12-18 20:09:17 (1.25 MB/s) - โ5353.1โ saved [25/25]
~~~
$ ls
5353  5353.1  solver.sh
$ strings 5353 | grep imctf
114470498imctfmmm534rch_73rm5_h4v3_b33n_l34k3d_0m6
114470498imctfmmm534rch_73rm5_h4v3_b33n_l34k3d_0m6
114470498imctfmmm534rch_73rm5_h4v3_b33n_l34k3d_0m6
176214533imctfmmm534rch_73rm5_h4v3_b33n_l34k3d_0m6
$ strings 5353.1 | grep imctf
$ cat 5353.1
There is no capture data.
```
ใใผใฟใๅๅพใงใใใฎใงใไฝๅใชๆๅญๅใๅใใ็ฝฎๆใใใฆใใ้จๅใๆปใใฆใใใจflagใจใชใใ  

## imctf{534rch_73rm5_h4v3_b33n_l34k3d_0m6}
