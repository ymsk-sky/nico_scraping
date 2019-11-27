# -*- coding: utf-8 -*-

import cv2

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

def main():
    url = get_source_url(id='sm31508454')
    play_movie(url)


def play_movie(url):
    video = cv2.VideoCapture(url)

    while(1):
        ret, frame = video.read()
        if(not ret):
            break
        cv2.imshow('frame', frame)

        if(cv2.waitKey(30) & 0xFF == ord('q')):
            break

    video.release()
    cv2.destroyAllWindows()


def get_source_url(id='sm31508454'):
    url = 'https://www.nicovideo.jp/watch/{}'.format(id)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    right_click = driver.find_element_by_class_name('PlayerContainer')
    actions = ActionChains(driver)
    actions.context_click(right_click)
    actions.perform()

    opened_menu = driver.find_elements_by_class_name('VideoContextMenuContainer-item')
    for system in opened_menu:
        if(system.text == 'システムメッセージを開く'):
            break

    actions.click(system)
    actions.perform()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    driver.close()
    driver.quit()

    # with open('page.html', 'w') as fw:
    #     fw.write(soup.prettify())
    # fw.close()

    line = soup.find_all('span', class_='SystemMessageContainer-info')
    text = '動画の読み込みを開始しました。'
    for l in line:
        if(text in l.text):
            break
    source_url = l.text.replace(text, '')[1:-1]

    return source_url

if __name__ == '__main__':
    main()
