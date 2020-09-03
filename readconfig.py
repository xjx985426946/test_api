import configparser
import os
def readconfig():
    dir = str((os.path.dirname(os.path.abspath(__file__))))
    dir = dir.replace('\\', '/')
    file_path = dir + "/config.conf"
    con = configparser.ConfigParser()
    con.read(file_path)
    ClientService_url = con.get("url", "ClientService_url")
    MerchantService_url = con.get("url", "MerchantService_url")
    zeno_url=con.get("url","zeno_url")
    url = dict()
    url['ClientService_url']=ClientService_url
    url['MerchantService_url'] = MerchantService_url
    url['zeno_url']= zeno_url
    return url

