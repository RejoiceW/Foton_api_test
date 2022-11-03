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
    adverlist = requests.get(url + '/api/upms/v1/foton/adver/list?pageNum=1&pageSize=10', headers=header)
    return adverlist


# 获取知识库列表
def get_knowledgemange():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    knowledgemange = requests.get(url + '/api/upms/v1/foton/knowledgemange/list?'
                                        'kno=&kname=&state=-2&createBy=&startTime=&endTime=&operationPersonName=&pageNum=1&pageSize=10',
                                  headers=header)
    return knowledgemange


# 获取待办列表
def get_fotodo():
    token = read_yaml()
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    fotodo = requests.get(url + '/api/upms/v1/foton/fotodo/list?pageNum=1&pageSize=10&inputType=0', headers=header)
    return fotodo


# 获取任务列表
def get_tasklist():
    token = read_yaml()
    data = {'inTaskStatus': 0, 'pageNum': 1, 'pageSize': 10}
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    tasklist = requests.post(url + '/api/foton/v1/web/expert/task/list', data=json.dumps(data), headers=header)
    return tasklist


# 新建知识库
def create_knowledgemange():
    token = read_yaml()
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    data = {"ktid": 35, "kname": now, "ktype": "电路图", "brandId": "2b2a38b6-1076-11ec-9d3d-00163e20",
            "brandName": "全品牌", "brandCode": "111111",
            "brandRelObjectInputList": [], "carname": "发动机",
            "carid": 244, "desc": "", "detail": "", "ossList": [], "commitOrDraft": 1}
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + '/api/upms/v1/foton/knowledgemange/add', data=json.dumps(data), headers=header)
    return response


# 新建公告
def create_adver():
    token = read_yaml()
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    data = {"title": now, "adverType": 24, "adverBrandList": [{"brandId": "2b2a38b6-1076-11ec-9d3d-00163e20"}],
            "content": now, "adverRoleList": [{"roleId": "111111"}], "carModelList": [],
            "status": 3, "spId": "4A9AD2C56A5B424198EEBDC5056A65BD"}
    header = {'authorization': token, 'Content-Type': 'application/json', 'client-type': 'web'}
    response = requests.post(url + '/api/upms/v1/foton/adver/insert', data=json.dumps(data), headers=header)
    return response


# 获取意见反馈列表
# def get_feedback():

# if __name__ == '__main__':
