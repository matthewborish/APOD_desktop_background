import os
from datetime import datetime
from datetime import timedelta
import urllib
import sys
from BeautifulSoup import *
import random

x = datetime.now()

myRI= random.randint(-1000,-1)

y = timedelta(weeks=0, days=myRI, hours=0, minutes=0, seconds=0)

print x

z = x + y

myDate = z.strftime('%y%m%d')

print myDate

url = "https://apod.nasa.gov/apod/ap"+ myDate + ".html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

hrefList = []
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
    hrefList.append(tag.get('href', None))

print "\n"
#print hrefList[1]

print "\n"
myImage = hrefList[1]
print myImage


urllib.urlretrieve("https://apod.nasa.gov/apod/" + myImage, "C:\\Wallpaper\\myApod.jpg")

import ctypes
import os
drive = "C:\\"
folder = "Wallpaper"
image = "myApod.jpg"
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)

sys.exit()



