# 测试意见反馈

from business.common import get_web_feedback, get_mobie_feedback


# 测试获取意见反馈列表
def test_feedback(get_token):
    response_web = get_web_feedback()
    response_mobie = get_mobie_feedback()
    assert response_web.status_code == 200
    assert response_web.json()['msg'] == '成功'
    assert response_mobie.status_code == 200
    assert response_mobie.json()['msg'] == '成功'
