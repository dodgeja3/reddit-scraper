#!/usr/bin/env python

import requests
import json
import os
import time
import glob
import string



# Move current wallpaper into pastwalls directory
try:
	oldwall = glob.glob('*jpg')[0]
	os.rename("./" + oldwall, "./pastwalls/" + oldwall)
except IndexError:
	print ("No current wallpaper found. Getting a new one")

# Get json from reddit/r/wallpapers
res = requests.get("https://www.reddit.com/r/wallpapers/.json", headers = {'User-agent': 'example.programV1.0.1'})
jsonres = json.loads(res.text)


os.system("touch FUUUCK1")

# Make sure url is jpg and get the title of post
found = False
count = 0
while (found == False):
	picurl = jsonres["data"]["children"][count]["data"]["url"]
	filetype = picurl.split('.').pop()
	if (filetype == "jpg"):
		filename = jsonres["data"]["children"][count]["data"]["title"]
		filename = filename.replace("/","")
		found = True
	else:
		count = count + 1
	
# Save the picture in current directory
path = os.getcwd()
filepath = (path + "/" + filename + "." + filetype).encode('utf-8')

f = open(filepath,'wb')
f.write(requests.get(picurl).content)
f.close()

# Set the picture as background
setup = "file://" + filepath

#os.system("xdg-open \"%s\"" % (setup))
#
#print("Would you like to set this wallpaper? (Y/N)")
#
#set_paper = input("Would you like to set this wallpaper? (Y/N)")


os.system("touch FUUUCK2")

#if (set_paper.lower() == "y"):
#print(setup)
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri \"%s\" " % (setup))
print ("Wallpaper set to: " + filename)
os.system("touch FUUUCK3")
