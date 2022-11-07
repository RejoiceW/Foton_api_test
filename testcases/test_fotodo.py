# 测试待办

from business.common import get_fotodo


# 测试获取待办列表
def test_get_fotodo(get_token):
    response = get_fotodo()
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
