import requests
import json

url = 'https://srstest.foton.com.cn/'


# 打开登陆页
def openUrl():
    response = requests.get(url + 'login')
    return response


# 登录
def login(username):
    data = {
        "grantType": "companyAdmin",
        "username": username,
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + 'api/auth/oauth/token', data=json.dumps(data), headers=header)
    # print(response.json())
    return response
