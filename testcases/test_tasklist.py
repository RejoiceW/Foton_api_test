# 测试任务记录
import allure
from business.common import get_tasklist


@allure.title('测试获取任务列表')
def test_get_tasklist(get_token):
    data = {'inTaskStatus': 0, 'pageNum': 1, 'pageSize': 10}
    response = get_tasklist(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
