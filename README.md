# 项目名及简介
* 此项目是基于Appium+python的基础，用来执行Android自动化测试

# 功能
* 基于python3
* 基于webdriver
* 支持多设备andoird并行

# 用法

**配置devices.yaml**

```
appium:
 - devices: 0021119e # 小米3
   port: 4725
   config: appium -p 4725 -bp 4735 --udid 0021119e
   platformName: android
   platformVersion: 4.4.4
 - devices: 76UBBKR224R8 # MX4 Pro
   port: 4726
   config: appium -p 4726 -bp 4736 --udid 76UBBKR224R8
   platformName: android
   platformVersion: 5.1.1
```

**配置监听HOST、PORT**

```
configs/config
class GetVariable(object):
    HOST = '192.168.xx.xx'
    PORT = 8088
```

**命名行运行:**

```
pyhton3 runner.py
```








