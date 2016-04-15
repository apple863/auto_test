#coding=utf-8
import math
import urllib
import threading
from time import sleep

threads=[]


#开始批量开关机
def startFunc(num):
    try:
        cName = ("cytest" + bytes(num))
        url1 = "http://42.159.242.130:8080/vm/shutdown?"
        param = "serviceName=%s&deploymentName=%s&virtualMachineName=%s" %(cName,cName,cName)
        print url1 + param
#            urllib.urlopen(url1 + param)
        su = urllib.urlopen(url1 + param)
        print su.read()
    except Exception, e:
        print e

#创建线程，并将方法加进线程中
def threadsCreat(threads1):
    for i in range(4,49):
        #将方法加进线程中，Thread方法说明（target为方法名，args为该方法的参数)
        thd=threading.Thread(target=startFunc,args=(i+1,))
        threads1.append(thd)


if __name__ == '__main__':
    threadsCreat(threads)
    print threads
    for ths in threads:
        ths.setDaemon(True)
        ths.start()
        sleep(1)
    ths.join()