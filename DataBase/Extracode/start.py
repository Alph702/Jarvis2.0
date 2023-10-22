import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    oo = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Data.txt",'rt')
    query = str(oo.read())
    oo.close
    pppp = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Data.txt",'r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\webdriver\\chromedriver.exe"
    photos = "F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\GooglePhotos\\"

    search_keys = [f'{query}']
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)

    for search_keys in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)
        os.startfile(photos)

GoogleImage()


