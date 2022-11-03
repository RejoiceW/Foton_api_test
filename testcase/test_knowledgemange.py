# 测试知识库

from business.common import get_knowledgemange, create_knowledgemange


# 测试获取知识库列表
def test_get_knowledgemange():
    response = get_knowledgemange()
    assert response.json()['msg'] == '成功'


# 测试新建知识库
def test_create_knowledgemange():
    response = create_knowledgemange()
    print(response.json())
    assert response.json()['msg'] == '成功'
