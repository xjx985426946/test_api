import yaml
from common.logger import Log
import os

# 读取测试用例
def __read_yaml(path,test_file,test_url,token=None,Authorization = None):
    '''
    :param path:
    :param test_file:
    :param test_url:
    :return:
    '''
    try:
        yaml_data = open(path + test_file, encoding="utf-8")
        test_data = yaml.load(yaml_data)
        for i in test_data:
            i['url'] = test_url + i['url']
            if token != None:
                i['header']['access_token'] = token
            if Authorization != None:
                i['header']['Authorization'] = 'Basic ' + Authorization
        return test_data
    except Exception as e:
        Log().error('文件读取失败：{0}'.format(e))


def read_yaml(path, test_file, test_url, token=None, Authorization = None):

    """
    :param path:
    :param test_file:
    :param test_url:
    :param token:
    :param Authorization:
    :return:
    """
    test_data = __read_yaml(path, test_file, test_url, token, Authorization)
    if not test_data:
        test_data = []
        return test_data
    else:
        return test_data

def update_yaml(path,test_file,key):
    """
    :param path:
    :param test_file:
    :param key:
    :return:
    """
    if os.path.exists(path + 'data_new.yaml'):
        d = open(path + 'data_new.yaml',encoding="utf-8")
        data = yaml.load(d)
        data[key] = str(int(data[key]) + 1)
        f = open(path + 'data_new.yaml','w')
        yaml.dump(data,f)
        f.close()
        d.close()
        return data[key]
    else:
        d = open(path + test_file, encoding="utf-8")
        data = yaml.load(d)
        data[key] = str(int(data[key]) + 1)
        f = open(path + 'data_new.yaml', 'w')
        yaml.dump(data, f)
        f.close()
        d.close()
        return data[key]

#清除报告
def __clear(abs):
    dir_run = os.path.basename(abs)
    print(dir_run)
    dir_reportFile=dir_run.replace('py','YAML')
    dirpath = os.path.dirname(abs)+"\\report\\"+dir_reportFile
    print(dirpath)
    if os.path.isfile(dirpath):
        with open(dirpath,'w',encoding='utf-8') as f:
            f.write("")
    else:
        pass