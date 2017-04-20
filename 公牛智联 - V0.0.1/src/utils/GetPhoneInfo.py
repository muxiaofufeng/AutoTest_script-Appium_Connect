# coding=utf-8
import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

command = "adb devices -l"
devices = os.popen(command).read()
device_list = re.findall("(.+?)device product.+?model:(.+?) ", devices)
device = {}
for i in device_list:
    i0 = i[0].split()
    i1 = i[1].split()
    device[i1[0]] = {"udid": i0[0]}

selected_port = 4723
for k, v in device.items():
    command = "adb -s %s shell getprop ro.build.version.release" % v["udid"]
    platformVersion = os.popen(command).read().split()[0]
    device[k]["platformVersion"] = platformVersion

    command = "adb -s %s shell getprop ro.product.model" % v["udid"]
    deviceName = os.popen(command).read().split()[0]
    device[k]["deviceName"] = deviceName

    command = "adb -s %s shell getprop net.bt.name" % v["udid"]
    platformName = os.popen(command).read().split()[0]
    device[k]["platformName"] = platformName

    command = "adb -s %s shell dumpsys window displays" % v["udid"]
    try:
        DPI = os.popen(command).read()
        tmp = re.findall("init=(.+?) ", DPI)[0].split("x")
        device[k]["dpi"] = tmp
    except WindowsError:
        pass

    for i in xrange(selected_port, 4750):
        command = 'netstat -aon|findstr %s' % i
        used_port = re.findall(r".+LISTENING.+", os.popen(command).read())
        if used_port == []:
            selected_port += 1
            device[k]["port"] = i
            break
print device
