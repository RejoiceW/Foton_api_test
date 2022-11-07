# 测试公告

from business.common import get_adverlist, create_adver
import time

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


# 测试获取公告列表
def test_get_adver():
    response = get_adverlist()
    # print(response.json()['data']['rows'][0]['id'])
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'


# 测试新建公告
def test_create_adver(get_token):
    data = {"title": now, "adverType": 24, "adverBrandList": [{"brandId": "2b2a38b6-1076-11ec-9d3d-00163e20"}],
            "content": now, "adverRoleList": [{"roleId": "111111"}], "carModelList": [],
            "status": 3, "spId": "4A9AD2C56A5B424198EEBDC5056A65BD"}
    # 创建公告前先获取一次列表第一条数据的id
    adverlist_id_old = get_adverlist().json()['data']['rows'][0]['id']
    # print(adverlist_id_old)
    response = create_adver(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
    # 创建后再获取一次最新列表第一条数据的id
    adverlist_id_new = get_adverlist().json()['data']['rows'][0]['id']
    print(adverlist_id_new)
    # 判断最新列表第一条数据的是否自增1
    assert adverlist_id_new == adverlist_id_old + 1
