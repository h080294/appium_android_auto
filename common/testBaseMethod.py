# -*- coding: utf-8 -*-


def get_conflict(self, name):
    if name in self.conflict_datas.keys():
        try:
            data = self.conflict_datas[name].pop()
            return data
        except Exception as e:
            raise Exception("%s:got no more value to be popped(%s)" % (name, str(e)))
    else:
        raise Exception("undefined:%s check your 'androidConfig.py' to see if it is configured correctly" % name)
