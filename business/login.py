# 登录操作
import json
import requests
import yaml

url = 'https://srstest.foton.com.cn'
username = "13183880002"


# 打开登陆页
def openUrl():
    response = requests.get(url + '/login')
    return response


# 登陆获取token
def get_token():
    data = {
        "grantType": "companyAdmin",
        "username": username,
        "password": "BwLtwISfvI7mV6UFFGIW6Q==",
        "companyIndex": "foton",
        "appKey": "app",
        "captchaKey": ""
    }
    header = {'authorization': 'Basic YXBwOg==', 'Content-Type': 'application/json', 'client-type': 'web'}
    login_data = requests.post(url + '/api/auth/oauth/token', data=json.dumps(data), headers=header)
    token = 'Bearer ' + login_data.json()['data']['accessToken']
    # print(token)
    return token


# 写入yaml文件
def write_yaml(_token):
    data = {
        "token": _token
    }
    with open(".\\token.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    token = get_token()  # 获取token
    write_yaml(token)  # 将token值写入yaml文件
