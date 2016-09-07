#!/usr/bin/python

import requests
import json
import os
import time
import glob

oldwall = glob.glob('current*')[0]
os.rename("./" + oldwall, "./pastwalls/" + time.strftime("%H:%M:%S"))

res = requests.get("https://www.reddit.com/r/wallpapers/.json", headers = {'User-agent': 'example.programV1.0.1'})
jsonres = json.loads(res.text)

picurl = jsonres["data"]["children"][0]["data"]["url"]

filetype = picurl.split('.').pop()
path = "./"
filepath = path + "current." + filetype

f = open(filepath,'wb')
f.write(requests.get(picurl).content)
f.close()

setup = "file://" + filepath
os.system("gsettings set org.gnome.desktop.background picture-uri '%s'" % (setup))

print ("done")
