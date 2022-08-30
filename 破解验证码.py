#1. 图像识别
#2. 选择互联网上成熟的验证码破解工具

#超级鹰

from selenium.webdriver import Chrome
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")

#处理验证码

img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('13012979755', 'Wz20030908', '936703')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

#向页面填入用户名和验证码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("18614075987")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("6035945")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()