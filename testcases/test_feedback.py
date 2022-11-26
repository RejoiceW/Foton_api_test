"""测试意见反馈"""

import allure
from business.common import get_web_feedback, get_mobie_feedback


@allure.feature("意见反馈模块")
class TestFeedback:
    @allure.title('测试获取意见反馈列表')
    @allure.story('正常获取')
    def test_get_web_feedback(self, get_token):
        data = "pageNum=1&pageSize=10&fdType=1"
        response = get_web_feedback(data)
        assert response.status_code == 200
        assert response.json()['msg'] == '成功'
