# 测试流程管理

import time
import allure
from business.common import get_processlist, create_process

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


@allure.title('测试获取流程管理列表')
def test_get_processlist(get_token):
    data = {"processId": "", "processName": "", "createStartTime": "", "createEndTime": "", "reviewStartTime": "",
            "reviewEndTime": "", "pageNum": 1, "pageSize": 10}
    response = get_processlist(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'


@allure.title('测试新建流程')
def test_create_process(get_token):
    data_get = {"processId": "", "processName": "", "createStartTime": "", "createEndTime": "", "reviewStartTime": "",
                "reviewEndTime": "", "pageNum": 1, "pageSize": 10}
    data_create = {"processId": "", "processName": now, "remark": "", "processType": 1,
                   "brandList": [{"brandCode": "104113", "carBrand": "递哥"}],
                   "postList": [{"id": 83, "remark": "", "createdBy": "system",
                                 "gmtCreated": 1599384173000, "params": {},
                                 "postId": "A563913EF2874788A2C5DC91F7FC0F8E",
                                 "companyId": "FCA54A71DF7D419794DCF5F7809317B8", "postCode": "062",
                                 "postName": "供应商专家",
                                 "postSort": "3", "status": "0", "level": 1}],
                   "render": "{\"brandList\":[\"104113\"],\"RoleList\":[{\"id\":83,\"orderNum\":null,\"remark\":\"\",\"disabled\":null,\"deleted\":null,\"createdBy\":\"system\",\"modifiedBy\":null,\"gmtCreated\":1599384173000,\"gmtModified\":null,\"params\":{},\"postId\":\"A563913EF2874788A2C5DC91F7FC0F8E\",\"personId\":null,\"companyId\":\"FCA54A71DF7D419794DCF5F7809317B8\",\"postCode\":\"062\",\"postName\":\"供应商专家\",\"postSort\":\"3\",\"status\":\"0\",\"flag\":false,\"level\":1}]}"}
    # 创建流程前先获取一次列表第一条数据的id
    process_id_old = get_processlist(data_get).json()['data']['rows'][0]['id']
    response = create_process(data_create)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
    # 创建后再获取一次最新列表第一条数据的id
    process_id_new = get_processlist(data_get).json()['data']['rows'][0]['id']
    # 判断最新列表第一条数据的id自增1
    assert process_id_new == process_id_old + 1
