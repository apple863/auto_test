#coding=utf-8
import math
import httplib
import urllib


cName=[]
for i in range(0,50):
    cName.append("cytest"+bytes(i+1))
print cName
#    print len(cName)




for i in range(0,50):
    try:
        cName = ("cytest" + bytes(i + 1))
        url1="http://42.159.242.130:8080/vm/start?"
        param="serviceName=cytest56&deploymentName=cytest561&virtualMachineName=%s" %cName
        print url1+param
        #su=urllib.urlopen(url1+param)
        #print su.read()
    except Exception, e:
        print e










