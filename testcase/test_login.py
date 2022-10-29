# 测试登录

import requests
import json

url = 'https://srstest.foton.com.cn/'


def test_login():
    r1 = requests.get(url + 'login')
    assert r1.status_code == 200

    data = {
        "grantType": "companyAdmin",
        "username": "13183880002",
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    r2 = requests.post(url + 'api/auth/oauth/token', data=json.dumps(data), headers=header)
    print(r2.json())
    assert r2.status_code == 200
    assert r2.json()['msg'] == '成功'


test_login()
