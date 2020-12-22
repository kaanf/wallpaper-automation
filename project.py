# Get the wallpaper from the internet
# Save it to a temp directory
# Set the wallpaper
# Automate the calls to this script

import requests
import wget
import subprocess
import time
import os

class colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    EndC = '\033[0m'

def get_wallpapers():
    access_key = 's6ztZTe_ZlfIZAIcvLB6np_ZU1_v9x8h-Djjw_28h2A'
    url = 'https://api.unsplash.com/photos/random/?client_id=' + access_key
    params = {
            'query': 'HD Wallpapers',
            'orientation': 'landscape'
            }
    response = requests.get(url, params=params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, '/tmp/wall.jpg') 
    return wallpaper

def set_wallpapers():
    wallpaper = get_wallpapers()
    o=subprocess.run('/usr/lib/x86_64-linux-gnu/io.elementary.contract.set-wallpaper /tmp/wall.jpg', shell=True)
    os.remove('/tmp/wall.jpg')

def choice_fun():
    choice = input(colors.BLUE  + "\nDo you like it " + "(" + 
            colors.GREEN + "Y" + "/" + colors.FAIL + "N" + colors.BLUE  +  "): " + colors.EndC)
    if(choice == 'Y' or choice == 'y'):
        print(colors.CYAN + "Bye!" + colors.EndC)
    elif(choice == 'N' or choice == 'n'):
        main()
    else:
        print(colors.WARNING + "Wrong input." + colors.EndC )
        choice_fun()

def main():
    try:
            set_wallpapers()
            choice_fun()

    except Exception:
        pass

if __name__ == '__main__':
    main()
