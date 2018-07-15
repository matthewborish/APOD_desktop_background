import os
from datetime import datetime
from datetime import timedelta
import urllib3
import sys
from bs4 import BeautifulSoup as bs
import random
import shutil
import ctypes


x = datetime.now()

myRI= random.randint(-1000,-1)

y = timedelta(weeks=0, days=myRI, hours=0, minutes=0, seconds=0)

print (x)

z = x + y

myDate = z.strftime('%y%m%d')

print (myDate)
http = urllib3.PoolManager()
url = "https://apod.nasa.gov/apod/ap"+ myDate + ".html"

response = http.request('GET', url)
soup = bs(response.data)

hrefList = []
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print (tag.get('href', None))
    hrefList.append(tag.get('href', None))

print ("\n")
#print hrefList[1]

print ("\n")
myImage = hrefList[1]
print (myImage)


#urllib3.urlretrieve("https://apod.nasa.gov/apod/" + myImage, "C:\\Wallpaper\\myApod.jpg")

http.request('GET', "https://apod.nasa.gov/apod/" + myImage, preload_content=False)

url = "https://apod.nasa.gov/apod/" + myImage
c = urllib3.PoolManager()
filename = "C:\\Wallpaper\\myApod.jpg"

with c.request('GET', url, preload_content=False) as resp, open(filename, 'wb') as out_file:
    shutil.copyfileobj(resp, out_file)

resp.release_conn()     # not 100% sure this is required though



drive = "C:\\"
folder = "Wallpaper"
image = "myApod.jpg"
image_path = os.path.join(drive, folder, image)


SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002

user32 = ctypes.WinDLL('user32')
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint
#SystemParametersInfo.restype = wintypes.BOOL
print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))

sys.exit()



