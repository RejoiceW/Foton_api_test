# 测试公告

from business.common import get_adverlist, create_adver


# 测试获取公告列表
def test_get_adver():
    response = get_adverlist()
    assert response.json()['msg'] == '成功'


# 测试新建公告
def test_create_adver():
    response = create_adver()
    assert response.json()['msg'] == '成功'
