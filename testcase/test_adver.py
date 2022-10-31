# 测试公告

from business.common import get_adverlist, get_token_fixture


def test_adver():
    response = get_adverlist()
    print(response.json())
    assert response.json()['msg'] == '成功'
