# 测试流程管理

from business.common import get_processlist


# 测试获取流程管理列表
def test_get_processlist():
    data = {"processId": "", "processName": "", "createStartTime": "", "createEndTime": "", "reviewStartTime": "",
            "reviewEndTime": "", "pageNum": 1, "pageSize": 10}
    response = get_processlist(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
