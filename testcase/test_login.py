# 测试登录
from business.common import login, openUrl

url = 'https://srstest.foton.com.cn/'


def test_openUrl():
    response = openUrl()
    assert response.status_code == 200


def test_login():
    response = login(13183880002)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
