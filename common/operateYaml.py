# -*- coding:utf-8 -*-
import yaml


def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到.yaml文件")
