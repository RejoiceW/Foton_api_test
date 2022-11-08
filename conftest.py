# 前置条件处理

import json
import os
import pytest
import requests
import yaml


# # 读取yaml环境文件
# def read_yaml_env():
#     # 工程目录拼接文件路径
#     yaml_path = os.path.dirname(__file__) + '\\data\\env.yaml'
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         result = yaml.load(f.read(), Loader=yaml.FullLoader)
#     url = result["url"]
#     # username = result["username"]
#     # password = result["password"]
#     # print(url, username, password)
#     return url


# url, username, password = read_yaml_env()
# url = read_yaml_env()


@pytest.fixture(scope="session")
def get_token():
    """获取登陆数据"""
    data = {
        "grantType": "companyAdmin",
        "username": "13183886106",
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    login_data = requests.post('https://srstest.foton.com.cn/api/auth/oauth/token', data=json.dumps(data),
                               headers=header)
    token = 'Bearer ' + login_data.json()['data']['accessToken']
    return token
    # data = {
    #     "token": token
    # }
    # yaml_path = os.path.dirname(__file__) + './data/token.yaml'
    # with open(yaml_path, "w", encoding="utf-8") as f:
    #     yaml.dump(data=data, stream=f, allow_unicode=True)
