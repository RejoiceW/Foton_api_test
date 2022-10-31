# 测试任务记录

from business.common import get_tasklist


def test_tasklist():
    response = get_tasklist(13183886106)
    print(response.json())
    assert response.json()['msg'] == '成功'
