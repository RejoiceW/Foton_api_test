# 测试待办

from business.common import get_fotodo


def test_fotodo():
    response = get_fotodo()
    assert response.json()['msg'] == '成功'
