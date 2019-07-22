# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:39:08 2019

@author: xiaobo
"""

import os, sys

# 列出目录
li = os.listdir(os.getcwd())
#print("目录为: %s"%li)
cnt = 0
for x in li:
#    print(x)
    
    strlist = x.split('.')
    if(strlist[1].find('py') < 0):
        # 截取
        strlist[0] = strlist[0][24:]
        # 替换
#        strlist[0] = strlist[0].replace('_', ' ')
        # 添加前后符号
#        strlist[0] = '[HorribleSubs] ' + strlist[0] +'[1080p]'
#        print(strlist[0])
        
        #拼接
        newName = strlist[0]#+'.'+strlist[1] +  '.'+strlist[2]
        print(newName)
        #重命名
#        os.rename(x,newName)
#    cnt = cnt + 1
#    if(cnt > 3):
#        break