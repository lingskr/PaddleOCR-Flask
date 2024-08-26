# import requests
# import json
# # url = 'http://127.0.0.1:8090'
#
# url = 'http://127.0.0.1:8090/ocr'
# files = {'file': open('./demo.jpg', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)
import requests
import json

url = 'http://127.0.0.1:8090/ocr'
files = {'file': open('./5407_corrected.jpg', 'rb')}
r = requests.post(url, files=files)
#print(r.text)
print(r.text.encode('utf-8').decode('unicode-escape'))