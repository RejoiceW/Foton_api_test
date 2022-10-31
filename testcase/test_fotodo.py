# 测试待办

from business.common import get_fotodo


def test_fotodo():
    response = get_fotodo(13183886106)
    print(response.json())
    assert response.json()['msg'] == '成功'
