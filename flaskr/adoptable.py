import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db
from bs4 import BeautifulSoup
import requests
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.common import WebDriverWait as wait





bp = Blueprint('adoptable', __name__, url_prefix='/adoptable')

@bp.route('/all')
def all():
    URL = 'https://apps.mcdot.maricopa.gov/AdoptablePets/'

    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')
    pups = soup.find_all("div", class_="RoundTheCorners5")

    # driver = webdriver.Chrome("chromdriver.exe")
    # driver.get(URL)
    # driver.find_element_by_name('lstPhotos$DataPager1$ctl01$ctl00').click()
    # pups = driver.find_elements_by_class_name('RoundTheCorners5')
    # print(pups)
    # text = wait(driver, 10).until(lambda driver: not text_field.text == 'Gerando...' and text_field.text)
    # return text
    
    info = []
    info_list = {}

    count = 0
    for pup in pups:
        image = pup.find('input', class_='RoundTheCorners2')
        count = count + 1
        for child in pup.find_all('span'):
            info.append(child.text)
        # print(info)
        
        info_list[info[0]] = {
            "ID": info[0],
            "Name ": info[1],
            "Bio ": info[2],
            "Age ": info[3],
            "Location ": info[4] 
        }

    # print(info_list)


    # for k, v in info_list.items():
    #     print(k, v)

    # print('\n'*2)

    with open("animals.txt", "w") as file:
        # file.write(str(soup))
        info = []
        for pup in pups:
            image = pup.find('input', class_='RoundTheCorners2')
            info.append(image)
            for child in pup.find_all('span'):
                info.append(child.text)
            file.write("<div>" + str(info) + "</div>")
        
        # print(info)

    # animal_id = info_list['ID']

    return render_template('animals/all.html', **locals())