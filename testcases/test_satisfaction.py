# 测试任务满意度报表
import allure
from business.common import get_satisfaction
import datetime


@allure.title('测试获取任务满意度报表')
def test_get_satisfaction():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=30)
    last_month = today - oneday
    data = "pageNum=1&pageSize=10&source=1&startTime=%s&endTime=%s" % (last_month, today)
    response = get_satisfaction(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
