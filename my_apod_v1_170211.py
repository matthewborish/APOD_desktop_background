
import os
from datetime import datetime
from datetime import timedelta
import urllib3
import sys
from bs4 import BeautifulSoup as bs
import random
import shutil
import ctypes


def get_random_date():
    now = datetime.now()
    random_int = random.randint(-1000, -1)
    td = timedelta(weeks=0, days=random_int, hours=0, minutes=0, seconds=0)
    random_date = (now + td).strftime('%y%m%d')
    return random_date


def scrape_apod(date):
    http = urllib3.PoolManager()
    url = "https://apod.nasa.gov/apod/ap" + date + ".html"

    response = http.request('GET', url)
    soup = bs(response.data)

    href_list = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print (tag.get('href', None))
        href_list.append(tag.get('href', None))

    my_image = href_list[1]

    http.request('GET', "https://apod.nasa.gov/apod/" + my_image, preload_content=False)

    url = "https://apod.nasa.gov/apod/" + my_image
    c = urllib3.PoolManager()
    filename = os.path.join("C:\\", "Wallpaper", "myApod.jpg")

    with c.request('GET', url, preload_content=False) as resp, open(filename, 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)

    resp.release_conn()

    if not os.path.exists(os.path.join("C:\\", "Wallpaper")):
        os.makedir(os.path.join("C:\\", "Wallpaper"))

    drive = "C:\\"
    folder = "Wallpaper"
    image = "myApod.jpg"
    image_path = os.path.join(drive, folder, image)
    return image_path


def update_wallpaper(image_path):
    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint
    print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))


x = get_random_date()
update_wallpaper(scrape_apod(date=x))

sys.exit()

