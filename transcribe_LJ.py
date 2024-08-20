#!/usr/bin/python3

import requests
import json
import os

url='http://localhost:9000/asr?output=json'

f_list=(os.listdir("wavs/"))

count = 0

for i in (f_list):
    f_list[count] = i[:-4]
    count = count + 1

f_list.sort()
print (f_list)

for i in f_list:
	b = i
	i = "wavs/"+i+'.wav'
	files = {'audio_file': (i, open(i, 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
	response=requests.post(url, files=files)
	print(response)
	text=response.json()
	text_res=json.loads(response.text)
	print(text_res["text"])
	f_result = text_res["text"]
	f = open("transcribed.csv", "a")
	print(b)
	f.write('\n'+b+'|'+f_result.lstrip()+'|'+f_result.lstrip())
	f.close()


