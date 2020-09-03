import configparser
# 读取配置环境
class ReadConf:
    def read_conf(self,conf_file,section,option):
        cf = configparser.ConfigParser()
        cf.read(conf_file,encoding='utf8')
        value = cf.get(section,option)
        return value

