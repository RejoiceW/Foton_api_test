# 测试待办
import allure
from business.common import get_fotodo


@allure.title('测试获取待办列表')
def test_get_fotodo(get_token):
    data = 'pageNum=1&pageSize=10&inputType=0'
    response = get_fotodo(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
