# 公共方法
import os.path
import requests
import json
import yaml
import time
from business.login import url


# 读取yaml文件的token
def read_yaml():
    yamlfile = os.path.dirname(__file__) + '.\\token.yaml'
    with open(yamlfile, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    token = result["token"]
    return token


# 获取公告列表
def get_adverlist():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.get(url + '/api/upms/v1/foton/adver/list?pageNum=1&pageSize=10', headers=header)
    return response


# 获取知识库列表
def get_knowledgemange():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.get(url + '/api/upms/v1/foton/knowledgemange/list?'
                                  'kno=&kname=&state=-2&createBy=&startTime=&endTime=&operationPersonName=&pageNum=1&pageSize=10',
                            headers=header)
    return response


# 获取待办列表
def get_fotodo():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.get(url + '/api/upms/v1/foton/fotodo/list?pageNum=1&pageSize=10&inputType=0', headers=header)
    return response


# 获取任务列表
def get_tasklist():
    token = read_yaml()
    data = {'inTaskStatus': 0, 'pageNum': 1, 'pageSize': 10}
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + '/api/foton/v1/web/expert/task/list', data=json.dumps(data), headers=header)
    return response


# 新建知识库
def create_knowledgemange(_data):
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + '/api/upms/v1/foton/knowledgemange/add', data=json.dumps(_data), headers=header)
    return response


# 新建公告
def create_adver(_data):
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + '/api/upms/v1/foton/adver/insert', data=json.dumps(_data), headers=header)
    return response


# 获取web端意见反馈列表
def get_web_feedback():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.get(url + "/api/upms/v1/foton/feedback/list?pageNum=1&pageSize=10", headers=header)
    return response


# 获取移动端意见反馈列表
def get_mobie_feedback():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'android'}
    response = requests.get(url + "/api/upms/v1/open/feedback/list?pageNum=1&pageSize=10&fdType=1", headers=header)
    return response


# 获取流程管理列表
def get_processlist(_data):
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + "/api/foton/v1/process/list", data=json.dumps(_data), headers=header)
    return response


# 获取人员列表
def get_userlist(_data):
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + "/api/upms/v1/foton/system/deviceuser/list", data=json.dumps(_data), headers=header)
    return response

# if __name__ == '__main__':
