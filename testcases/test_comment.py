"""测试评价管理"""

import allure
from business.common import get_comment


@allure.title('测试获取评价列表')
def test_get_comment(get_token):
    data = {"creatorName": "", "taskCode": "", "pageNum": 1, "pageSize": 10, "commentStatus": "0"}
    response = get_comment(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
