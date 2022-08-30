from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

web = Chrome(executable_path="chromedriver")

web.get("http://www.baidu.com")
print(web.title)

web = Chrome()

web.get("http://lagou.com")

web.find_element_by_xpath('//*[@id="cboxClose"]').click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(1)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()

# 如何进入到进窗口中进行提取
# 注意, 在selenium的眼中. 新窗口默认是不切换过来的.
web.switch_to.window(web.window_handles[-1])

# 在新窗口中提取内容
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# 关掉子窗口
web.close()
# 变更selenium的窗口视角. 回到原来的窗口中
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)


