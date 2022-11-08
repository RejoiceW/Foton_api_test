# 测试评价管理

from business.common import get_comment


# 测试获取评价列表
def test_get_comment(get_token):
    response = get_comment()
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
