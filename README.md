智蜂接口自动化框架
----
- python 环境依赖
```
python 3.x.x

安装依赖包： pip3 install -r requirements.txt
```


拉取 http://git.smartfeng.com/intbee/intbee-test-script/blob/intbee_api/Test-api 项目


构建 执行 测试环境api测试

python3 run.py

XXX目录下有 pytest_result.html文件

且外部输入地址可以访问到  pytest_result.html文件

设置为每天早上八点钟定时执行一次


- 构建 执行 线上环境api测试

python3 run_production.py

XXX目录下有 pytest_result.html文件

且外部输入地址可以访问到  pytest_result.html文件