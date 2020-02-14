import os
import threading

def fn(series):
    os.system('adb -s '+ series + ' shell input swipe 300 700 300 150')
    timer = threading.Timer(3, fn, [series])
    timer.start()

devices = os.popen('adb devices').read()
devices_lists = devices.splitlines()
devices_counts = devices_lists.__len__()
for i in range(1, devices_counts - 1):
    device_info = devices.splitlines()[i]
    device_series = device_info.split( )[0]
    fn(device_series)