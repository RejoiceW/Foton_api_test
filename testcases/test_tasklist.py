# 测试任务记录

from business.common import get_tasklist


# 测试获取任务列表
def test_get_tasklist(get_token):
    response = get_tasklist()
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
