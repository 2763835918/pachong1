import requests
import json
def get_data(start,end):
    params = {
        "airport" : "PEK" ,
        "route_type" : "all" ,
        "start_time" : start ,
        "end_time" : end
        #"2022 - 08 - 16"
    }
    headers = {
        "Authorization": '''bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZGF0YS1hcGkuMTMzLmNuXC9hcGlcL3YxXC9hdXRoXC9sb2dpbiIsImlhdCI6MTY2MDcyOTEyNSwiZXhwIjoxNjYwODE1NTI1LCJuYmYiOjE2NjA3MjkxMjUsImp0aSI6Ik5JZXVUSlRxM1l2cGx6b1kiLCJzdWIiOjIyMzksInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.te7ZTT7TH44fXAWp4aj90a-vl-MZyYwTFn3UAH1wzZU''',
         "client-id": "Mydv7cuN0j0BKrPZ",
        "Referer": "https://dast.133.cn/",
        "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"''',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform ": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://dast.133.cn"

    }
    url = "https://data-api.133.cn/api/v1/airport/statistics"
    resp = requests.get(url=url,params=params,headers= headers)
    print(resp.text)

get_data("2022 - 08 - 9","2022 - 08 - 9")


# sessin = requests.session()
#
# url = "https://data-api.133.cn/api/v1/auth/login"
# data = {
#     "mobile": "13038596685",
#     "password": "Wz20030908",
#     "captcha": ""
# }
# resp = sessin.post(url = url,data=data)
# # print(resp.cookies)
#
# headers = {
#         "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZGF0YS1hcGkuMTMzLmNuXC9hcGlcL3YxXC9hdXRoXC9sb2dpbiIsImlhdCI6MTY2MDcyOTY4MywiZXhwIjoxNjYwODE2MDgzLCJuYmYiOjE2NjA3Mjk2ODMsImp0aSI6ImJ4THNwS0dDZzRSUWk3ZDAiLCJzdWIiOjIyMzksInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.um7oPNIMe4c-bvQHOZPZFV-_j8UFEBHsD1kXKHeAPf4"
#         , "client-id": "Mydv7cuN0j0BKrPZ",
#         "Referer": "https://dast.133.cn/",
#         "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "Windows",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-site",
#         "Connection": "keep-alive",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Origin": "https://dast.133.cn"
#
#     }
# resp = sessin.get("https://data-api.133.cn/api/v1/airport/statistics?airport=PEK&route_type=all&start_time=2022-08-16&end_time=2022-08-16",headers=headers)
# print(resp.text)