# 测试知识库

from business.common import get_knowledgemange


def test_knowledgemange():
    response = get_knowledgemange(13183886106)
    print(response.json())
    assert response.json()['msg'] == '成功'
