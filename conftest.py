# 前置条件处理
import json
import os
import pytest
import requests
import yaml

url = 'https://srstest.foton.com.cn'
username = "13183886106"


@pytest.fixture(scope="session")
def get_token():
    data = {
        "grantType": "companyAdmin",
        "username": username,
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    login_data = requests.post(url + '/api/auth/oauth/token', data=json.dumps(data), headers=header)
    token = 'Bearer ' + login_data.json()['data']['accessToken']
    # return token
    data = {
        "token": token
    }
    # 写入yaml文件
    yamlfile = os.path.dirname(__file__) + '.\\business\\token.yaml'
    with open(yamlfile, "w", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)
