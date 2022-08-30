from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
web = Chrome(options=opt)
#添加参数，让程序在后台运行

web.get("https://ys.endata.cn/BoxOffice/Ranking")


#定位到下拉列表

sel_el = web.find_element(By.XPATH,"a")
#对元素包装成下拉列表
sel = Select(sel_el)
#i就是每个下拉框索引的位置
for i in range(len(sel.options)):
    sel.select_by_index(i)#按照索引切换
    time.sleep(2)
    table = web.find_element(By.XPATH,'a')
    print(table.text)
    print("###############################")

web.close()