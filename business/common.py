# 封装公共方法

import os
import requests
import json
from conftest import get_token


url = "https://srstest.foton.com.cn"


# 读取yaml文件token
# def read_yaml_token():
#     yaml_path = os.path.dirname(__file__) + './data/token.yaml'
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         result = yaml.load(f.read(), Loader=yaml.FullLoader)
#     token = result["token"]
#     return token


# 定义请求头
header = {'authorization': get_token(), 'Content-Type': 'application/json', 'client-type': 'web'}


# 获取公告列表
def get_adverlist(_data):
    response = requests.get(url + '/api/upms/v1/foton/adver/list', params=_data, headers=header)
    return response


# 获取知识库列表
def get_knowledgemange(_data):
    response = requests.get(url + '/api/upms/v1/foton/knowledgemange/list', params=_data, headers=header)
    return response


# 获取待办列表
def get_fotodo(_data):
    response = requests.get(url + '/api/upms/v1/foton/fotodo/list', params=_data, headers=header)
    return response


# 获取任务列表
def get_tasklist(_data):
    response = requests.post(url + '/api/foton/v1/web/expert/task/list', data=json.dumps(_data), headers=header)
    return response


# 获取评价记录
def get_comment(_data):
    response = requests.post(url + '/api/foton/v1/admin/comment/list', data=json.dumps(_data), headers=header)
    return response


# 新建知识库
def create_knowledgemange(_data):
    response = requests.post(url + '/api/upms/v1/foton/knowledgemange/add', data=json.dumps(_data), headers=header)
    return response


# 新建公告
def create_adver(_data):
    response = requests.post(url + '/api/upms/v1/foton/adver/insert', data=json.dumps(_data), headers=header)
    return response


# 获取web端意见反馈列表
def get_web_feedback(_data):
    response = requests.get(url + "/api/upms/v1/foton/feedback/list", params=_data, headers=header)
    return response


# 获取移动端意见反馈列表
def get_mobie_feedback(_data):
    response = requests.get(url + "/api/upms/v1/open/feedback/list", headers=header)
    return response


# 获取流程管理列表
def get_processlist(_data):
    response = requests.post(url + "/api/foton/v1/process/list", data=json.dumps(_data), headers=header)
    return response


# 获取人员列表
def get_userlist(_data):
    response = requests.post(url + "/api/upms/v1/foton/system/deviceuser/list", data=json.dumps(_data), headers=header)
    return response


# 新建流程
def create_process(_data):
    response = requests.post(url + "/api/foton/v1/process/save", data=json.dumps(_data), headers=header)
    return response


# 获取故障模式报表
def get_fault(_data):
    response = requests.get(url + "/api/foton/v1/process/save", headers=header)
    return response


# 获取任务满意度报表
def get_satisfaction(_data):
    response = requests.get(url + "/api/foton/v1/taskcount/satisfaction", params=_data, headers=header)
    return response


# 获取故障模式报表
def get_fault(_data):
    response = requests.get(url + "/api/foton/v1/servicer/report/fault", params=_data, headers=header)
    return response
