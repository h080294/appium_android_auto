import pickle
import time
from common import operateFile


def getStrTime(t_time, format):
    # time.strftime("%Y-%m-%d %I%p %M:%S 今天是当年第%j天  当年第%U周  星期%w",time.localtime())
    # time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time.strftime(format, t_time)


def write_pickle(dict_data, path="data.pickle"):
    read = read_pickle(path)
    result = []
    if len(read) > 0:
        read.append(dict_data)
        result = read
    else:
        result.append(dict_data)
    with open(path, 'wb') as f:
        print(result)
        pickle.dump(result, f, 0)


def read_pickle(path):
    data = {}
    if operateFile.OperateFile(path).check_file():
        with open(path, 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                pass
    print(data)
    return data
