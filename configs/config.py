#  /usr/bin/env python
#  -*- encoding: utf-8 -*-
class GetVariable(object):
    HOST = '192.168.73.33'
    PORT = 8088

# conflict_phone
# 适用场景：在相同case运行在多个终端时，每个终端通过相同的name调用方法self.get_conflict()能获取到不同数据
# 该配置解决在多个设备同时跑相同case的场景下可能存在的数据冲突
# 例如：两个手机同时跑登录的case，如果case内使用帐号相同则会存在帐号冲突，导致某一台手机case运行失败
# 数据格式----以name和value(list类型)：    name  |   value
# 用法：
#     username,password = self.get_conflict()
# [注意]：
#     在case内有使用的name，其value内配置的值个数不能少于使用的设备数！
conflict_phone = [('19977994426', '123456'), ('19906521511', '123456'), ('19904521511', '123456'),
                  ('19905521511', '123456'), ('19903521511', '123456'), ('19902521511', '123456')]
