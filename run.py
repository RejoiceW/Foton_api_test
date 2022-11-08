import pytest
import os

if __name__ == '__main__':
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    --clean-alluredir:每次执行前清空数据，这样在生成的报告中就不会追加，只显示当前执行的用例
    '''
    pytest.main(['-s', '-q', './', '--clean-alluredir', '--alluredir=report'])
    # 执行测试用例时将环境信息复制到report目录下，避免被删除
    os.system('cp environment.properties ./report/environment.properties')
    # 在当前路径下生成测试报告，-c清空历史数据 -o指定输出测试报告路径
    # os.system("allure generate -c -o allure-report")
