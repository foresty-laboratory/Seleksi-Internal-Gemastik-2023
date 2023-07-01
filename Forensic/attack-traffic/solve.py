#!/usr/bin/python3

from urllib.parse import unquote
import json, re

data = json.loads(open('exported-http.json').read())
flag = [''] * 100
for i in range(len(data)):
    response_time = float(data[i]["_source"]["layers"]["frame"]["frame.time_delta_displayed"])
    if response_time >= 2:
        url = unquote(data[i]["_source"]["layers"]["http"]["http.response_for.uri"])
        idx, char = re.findall(r"ord\(substr\(password,(.*),1\)\)=(.*) and sleep\(2\)", url)[0]
        flag[int(idx)] = chr(int(char))
        
print(''.join(flag))
