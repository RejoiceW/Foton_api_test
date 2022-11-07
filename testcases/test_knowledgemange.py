# 测试知识库

import time
from business.common import get_knowledgemange, create_knowledgemange

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


# 测试获取知识库列表
def test_get_knowledgemange(first):
    response = get_knowledgemange()
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'


# 测试新建知识库
def test_create_knowledgemange(get_token):
    data = {"ktid": 35, "kname": now, "ktype": "电路图", "brandId": "2b2a38b6-1076-11ec-9d3d-00163e20",
            "brandName": "全品牌", "brandCode": "111111",
            "brandRelObjectInputList": [], "carname": "发动机",
            "carid": 244, "desc": "", "detail": "", "ossList": [], "commitOrDraft": 1}
    # 创建知识库前先获取一次列表第一条数据的id
    knowledgemange_id_old = get_knowledgemange().json()['data']['rows'][0]['id']
    # print(knowledgemange_id_old)
    response = create_knowledgemange(data)
    assert response.status_code == 200
    assert response.json()['msg'] == '成功'
    # 创建后再获取一次最新列表第一条数据的id
    knowledgemange_id_new = get_knowledgemange().json()['data']['rows'][0]['id']
    # print(knowledgemange_id_new)
    # 判断最新列表第一条数据的id自增1
    assert knowledgemange_id_new == knowledgemange_id_old + 1
