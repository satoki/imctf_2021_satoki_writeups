# mmm😰

## 問題文
先輩がmなんちゃら？を有効にしたようです。アドレスバーで検索をするなと言われましたが意味が分かりません。  
URL1: [http://118.27.114.90:31417](http://118.27.114.90:31417/)  
URL2: [http://118.27.104.46:31417](http://118.27.104.46:31417/)  
※この問題はリクエストを複数回施行することが許可されています。URL1、URL2のどちらを用いても構いません。重くないほうをご利用ください。  
[app.py](files/app.py)  

## 難易度
**medium**  

## 作問にあたって
ブラウザのアドレスバーから検索を行うとmDNSによって検索ワードがばれることから思いつきました。  
おそらくCTFで扱われたことがないですが、作問時間が少なすぎておかしい問題設定になっています。  
もっとうまくやりたかった...。  

## 解法
サイトには謎のメッセージが表示されるだけである。  
```bash
$ curl http://118.27.114.90:31417
Can you get the server's traffic data?<br>Some well-known port numbers may be blocked.
```
配布されたapp.pyを見ると以下のようであった。  
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
`/`では`google-chrome`で`http://乱数+flagの記号を置換したもの+dataクエリパラメータ`にアクセスしているだけである。  
`/<int:port>`ではtcpdumpで好きなポートをキャプチャでき、その結果を返してくれる。  
ただし、`22`、`53`、`80`、`443`は禁止されている。  
問題文にmなんちゃらとあり、「ブラウザ　アドレスバー　検索」Google検索すると、[ツイート](https://twitter.com/akira_you/status/1419228947766644736)がヒットする。  
ブラウザのアドレスバーで検索すると、mDNSで検索文字列が流出するようだ。  
mDNSポートを調べると5353であることがわかるのでここをキャプチャすればよい。  
ここで注意だが、Linux環境では.localでない場合、mDNSが発されないことがあるので`data=local`で対応すればよい。  
`http://118.27.114.90:31417?data=local`にアクセスしつつ、`http://118.27.114.90:31417/5353`を取得する。  
一連のリクエストを、solver.shをいくつか起動することで行う。  
```bash
$ ./solver.sh;./solver.sh
~~~
Saving to: ‘5353’

5353                          100%[=================================================>]     473  --.-KB/s    in 0s

2021-12-18 20:09:13 (6.31 MB/s) - ‘5353’ saved [473/473]
~~~
Saving to: ‘5353.1’

5353.1                        100%[=================================================>]      25  --.-KB/s    in 0s

2021-12-18 20:09:17 (1.25 MB/s) - ‘5353.1’ saved [25/25]
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
データが取得できたので、余分な文字列を取り、置換されている部分を戻してやるとflagとなる。  

## imctf{534rch_73rm5_h4v3_b33n_l34k3d_0m6}
