import datetime,time

#获取时间
def gettime(days):
    """
    :param days:  当前时间 + days （天）
    :return:
    """
    utime = (datetime.datetime.now()+datetime.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    print(utime)
    stamp_array = time.strptime(utime, '%Y-%m-%d %H:%M:%S')
    stamp = int(time.mktime(stamp_array) * 1000)
    return stamp

#获取当前时间戳
def getnow():
    t = time.time()
    return int(round(t * 1000))


def getstrtime(days):
    """
    :param days:  当前时间 + days （天）
    :return:
    """
    utime = (datetime.datetime.now()+datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    return utime
