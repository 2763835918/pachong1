from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import re
# opt = Options()
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")
web = Chrome()
# web = Chrome(options=opt)
jx = []
star = []
en = []
mud = []
qis = []
hangban= []
date = []
for j in range(1,2):
    web.get(f"https://flights.ctrip.com/schedule/tao.bjs.html?pageno=2")

    tr_list = web.find_elements(By.XPATH,'//*[@id="flt1"]/tr')
    for tr in tr_list:
        jixing = tr.find_element(By.XPATH, 'td[1]/span/span').text
        jx.append(jixing)
        start = tr.find_element(By.XPATH, 'td[2]/strong').text
        star.append(start)
        end = tr.find_element(By.XPATH, 'td[4]/strong').text
        en.append(end)
        mudi = tr.find_element(By.XPATH, 'td[4]/div').text
        mud.append(mudi)
        qishi = tr.find_element(By.XPATH, 'td[2]/div').text
        qis.append(qishi)
        hangbanhao = tr.find_element(By.XPATH, 'td[1]/a/strong').text
        hangban.append(hangbanhao)
    resp = web.page_source

    obj = re.compile(r'.*?autocomplete="off" class="input_date submit_date" value="(?P<date>.*?)"></div></td><td><a data-testid.*?',re.S)
    result = obj.finditer(resp)
    for i in result:
        date.append(i.group("date"))
    list = [jx,star,en,mud,qis,hangban,date]
    x = pd.DataFrame(data=list)
    x.to_csv("shujv12.csv",encoding="ANSI")
    print("over")
    time.sleep(1)
    web.close()





























# print(jixing,start,end,mudi,qishi,hangbanhao,a)
# opt = Options()
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")
# web = Chrome(options=opt)
#
# web.get("https://flights.ctrip.com/online/list/oneway-sha-bjs?depdate=2022-08-19&cabin=y_s_c_f&adult=1&child=0&infant=0")
# tr_list = web.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[2]/span/div')
# # //*[@id="comfort-MU5099_1660863600000-0"]/div/span[1]/span
# for tr in tr_list:
#
#     jixing = tr.find_element(By.ID, 'departureFlightTrainMU5099_1660863600000-0"').text
#     # start = tr.find_element(By.XPATH, 'td[2]/strong').text
#     # end = tr.find_element(By.XPATH, 'td[4]/strong').text
#     # mudi = tr.find_element(By.XPATH, 'td[4]/div').text
#     # qishi = tr.find_element(By.XPATH, 'td[2]/div').text
#     # hangbanhao = tr.find_element(By.XPATH, 'td[1]/a/strong').text
#     # a = tr.find_element(By.XPATH, 'td[8]/div')
#     print(jixing)
#
#     # print(jixing,start,end,mudi,qishi,hangbanhao,a)
