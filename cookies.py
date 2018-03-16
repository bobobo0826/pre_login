#在webdriver中塞入cookie值
import requests
import time
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.set_window_size(1050, 840)
    # driver = webdriver.Chrome()
    # driver.maximize_window()

    url = 'https://www.qichacha.com/firm_3dd3f527dd7c3a81d73291eeb847aad1.html'
    cookie = 'UM_distinctid=160fd15721a9c9-071aff60ca647f-7b113d-1fa400-160fd15721bc1c; _uab_collina=151609163784756238080354; acw_tc=AQAAANwIZhO0pAMA01TheaMKJ/4EztGO; hasShow=1; zg_did=%7B%22did%22%3A%20%22160fd15722d136-0d486f5fca1888-7b113d-1fa400-160fd15722ea15%22%7D; CNZZDATA1254842228=918165069-1516073157-null%7C1516240667; _umdata=55F3A8BFC9C50DDA6D5B01D1A2C4BD594729A3C2F0A1F368B20B7C98FE1BB44573933CC5503128B8CD43AD3E795C914CDB578452826F1A2810689DF00059E9A6; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201516244097614%2C%22updated%22%3A%201516245509558%2C%22info%22%3A%201516074529331%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22076ec19e42d4f48979bef4ad1a1450a5%22%7D; PHPSESSID=9s800680tofhjn2fdtfbjvr552'
    cookie = dict(elem.strip().split('=') for elem in cookie.split(';'))#key不能带空格
    browser.get(url=url)
    time.sleep(3)
    browser.delete_all_cookies()
    for key, value in cookie.items():
        c1 = {
            # 'domain': 'qichacha.com',
            'name': key,
            'value': value,
            'path': '/',
            'secure': True,
        }
        browser.add_cookie(c1)
        # c1.clear()
    browser.get(url=url)
    res = browser.page_source
    print(res)

        # c1 = {
    #             # 'domain': 'qichacha.com',
    #             'name': "UM_distinctid",
    #             'value': "160fd15721a9c9-071aff60ca647f-7b113d-1fa400-160fd15721bc1c",
    #             'path': '/',
    #             'secure': True,
    # }
    # c2 = {
    #             # 'domain': 'qichacha.com',
    #             'name': "_uab_collina",
    #             'value': "151609163784756238080354",
    #             'path': '/',
    #             'secure': True,
    # }
    # c3 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "acw_tc",
    #     'value': "AQAAANwIZhO0pAMA01TheaMKJ/4EztGO",
    #     'path': '/',
    #     'secure': True,
    # }
    # c4 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "hasShow",
    #     'value': "1",
    #     'path': '/',
    #     'secure': True,
    # }
    # c5 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "zg_did",
    #     'value': "%7B%22did%22%3A%20%22160fd15722d136-0d486f5fca1888-7b113d-1fa400-160fd15722ea15%22%7D",
    #     'path': '/',
    #     'secure': True,
    # }
    # c6 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "CNZZDATA1254842228",
    #     'value': "918165069-1516073157-null%7C1516240667",
    #     'path': '/',
    #     'secure': True,
    # }
    # c7 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "_umdata",
    #     'value': "55F3A8BFC9C50DDA6D5B01D1A2C4BD594729A3C2F0A1F368B20B7C98FE1BB44573933CC5503128B8CD43AD3E795C914CDB578452826F1A2810689DF00059E9A6",
    #     'path': '/',
    #     'secure': True,
    # }
    # c8 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f",
    #     'value': "%7B%22sid%22%3A%201516244097614%2C%22updated%22%3A%201516245509558%2C%22info%22%3A%201516074529331%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22076ec19e42d4f48979bef4ad1a1450a5%22%7D",
    #     'path': '/',
    #     'secure': True,
    # }
    # c9 = {
    #     # 'domain': 'qichacha.com',
    #     'name': "PHPSESSID",
    #     'value': "9s800680tofhjn2fdtfbjvr552",
    #     'path': '/',
    #     'secure': True,
    # }
    # browser.add_cookie(c1)
    # browser.add_cookie(c2)
    # browser.add_cookie(c3)
    # browser.add_cookie(c4)
    # browser.add_cookie(c5)
    # browser.add_cookie(c6)
    # browser.add_cookie(c7)
    # browser.add_cookie(c8)
    # browser.add_cookie(c9)
    #
    # browser.get(url=url)
    # res = browser.page_source
    # print(res)






















    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    #     "Cookie": cookie,
    #     # "Host": "www.qichacha.com",
    #     # "Referer": "http://www.qichacha.com/",
    #     # "Connection": "keep-alive",
    #     # "DNT": "1",
    #     # "Upgrade-Insecure-Requests": "1"
    # }
    # res = requests.get(url=url,headers=headers)
    # print(res.content.decode("utf-8"))




