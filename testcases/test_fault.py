"""测试故障模式报表"""

import allure
from business.common import get_fault
import datetime


@allure.title('测试获取故障模式报表')
def test_get_fault():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=30)
    last_month = today - oneday
    data = "pageNum=1&pageSize=10&source=1&startTime=%s&endTime=%s" % (last_month, today)
    response = get_fault(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
