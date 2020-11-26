# //*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[4]/div
# //*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/span/div
import tinder
import cssutils
from bs4 import BeautifulSoup
import urllib.request
import os
from time import sleep


def get_pic(bot):
    html = (bot.driver.page_source)
    soup = BeautifulSoup(html)
    urls = []
    div_styles = soup.find_all('div', {"class": "Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox"})

    for div_style in div_styles:
        style = div_style['style']
        style = cssutils.parseStyle(style)
        url = style['background-image']
        url = url.replace('url(', '').replace(')', '')
        urls.append(url)

    name = soup.find('span', {"Fz($xl) Fw($bold)"})
    print(name.contents[0])
    new_dir_path = 'pic/{}'.format(name.contents[0])
    os.makedirs(new_dir_path)
    for i in range(len(urls)):
        save_name = new_dir_path + '/pic_{}.jpg'.format(i+1)
        tgt = urllib.request.urlopen(urls[i]).read()
        with open(save_name, mode='wb') as f:
            f.write(tgt)


bot = tinder.TinderBot()


bot.login()

bot.driver.get('https://tinder.com/app/recs')
sleep(3)
bot.close_popup_liked()

get_pic(bot)



sleep(10)