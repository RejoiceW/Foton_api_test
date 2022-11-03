# 测试人员管理

from business.common import get_userlist


# 测试获取人员管理列表
def test_get_userlist():
    data = {"startTime": "", "endTime": "", "realName": "", "deviceUserName": "", "pageNum": 1, "pageSize": 10}
    response = get_userlist(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
