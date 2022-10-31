# 公共方法
import pytest
import requests
import json

url = 'https://srstest.foton.com.cn'
username = "13183880002"


# 打开登陆页
def openUrl():
    response = requests.get(url + '/login')
    return response


# 登录
def login(_username):
    data = {
        "grantType": "companyAdmin",
        "username": _username,
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    login_data = requests.post(url + '/api/auth/oauth/token', data=json.dumps(data), headers=header)
    # print(response.json())
    return login_data


# 登陆获取token
@pytest.fixture(scope="session")
def get_token_fixture():
    data = {
        "grantType": "companyAdmin",
        "username": "13183880002",
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    login_data = requests.post(url + '/api/auth/oauth/token', data=json.dumps(data), headers=header)
    token = 'Bearer ' + login_data.json()['data']['accessToken']
    return token


# 获取公告列表
def get_adverlist(get_token_fixture):
    # token = get_token(username)
    # print(token)
    header = {'authorization': get_token_fixture, 'Content-Type': 'application/json', 'client-type': 'web'}
    adverlist = requests.get(url + '/api/upms/v1/foton/adver/list?pageNum=1&pageSize=10', headers=header)
    return adverlist


# 获取知识库列表
def get_knowledgemange(get_token_fixture):
    # token = get_token(username)
    header = {'authorization': get_token_fixture, 'Content-Type': 'application/json', 'client-type': 'web'}
    knowledgemange = requests.get(url + '/api/upms/v1/foton/knowledgemange/list?'
                                        'kno=&kname=&state=-2&createBy=&startTime=&endTime=&operationPersonName=&pageNum=1&pageSize=10',
                                  headers=header)
    return knowledgemange


# 获取待办列表
def get_fotodo(get_token_fixture):
    # token = get_token(username)
    header = {'authorization': get_token_fixture, 'Content-Type': 'application/json', 'client-type': 'web'}
    fotodo = requests.get(url + '/api/upms/v1/foton/fotodo/list?pageNum=1&pageSize=10&inputType=0', headers=header)
    return fotodo


# 获取任务列表
def get_tasklist(get_token_fixture):
    # token = get_token(username)
    data = {'inTaskStatus': 0, 'pageNum': 1, 'pageSize': 10}
    header = {'authorization': get_token_fixture, 'Content-Type': 'application/json', 'client-type': 'web'}
    tasklist = requests.post(url + '/api/foton/v1/web/expert/task/list', data=json.dumps(data), headers=header)
    return tasklist
