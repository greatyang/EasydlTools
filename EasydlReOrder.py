#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os

#均值哈希算法
def aHash(img):
    #缩放为8*8
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s=0
    hash_str=''
    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s=s+gray[i,j]
    #求平均灰度
    avg=s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if  gray[i,j]>avg:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str
 
#差值感知算法
def dHash(img):
    #缩放8*8
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if   gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str
 
#Hash值对比
def cmpHash(hash1,hash2):
    n=0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
        #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n+1
    return n


def main():
    dst_compare_dir='C:\\Users\\greatyang\\Downloads\\easydl2labelImg-master\\shanxi\\'
    src_compare_dir='E:\\apple\\yantai\\'    
    dstfiles = os.listdir(dst_compare_dir)
    dstjpg = []
    dsthash = []
    for j in range(0, len(dstfiles)):
        dstpath = os.path.join(dst_compare_dir, dstfiles[j])
        if os.path.isfile(dstpath) and dstpath.endswith(".jpg"):
            img2=cv2.imread(dstpath)
            hash2= aHash(img2)
            dsthash.append(hash2)
            dstjpg.append(dstpath)
    
    files = os.listdir(src_compare_dir) 
    for i in range(0, len(files)):
        path = os.path.join(src_compare_dir, files[i])
        #print("file ",path,"\n")
        if os.path.isfile(path) and path.endswith(".jpg"):
            
            valueindex = 0
            value = 65
            img1=cv2.imread(path)
            hash1= aHash(img1)
            print("src hash"+hash1)
            for j in range(0, len(dsthash)):
                n=cmpHash(hash1,dsthash[j])
                #print('均值哈希算法相似度：'+ str(n))
                #hash1= dHash(img1)
                #hash2= dHash(img2)
                #print(hash1)
                #print(hash2)
                #n=cmpHash(hash1,hash2)
                #print '差值哈希算法相似度：'+ str(n)
                if(n < value):
                    value = n
                    valueindex = j
            print("max value is "+str(value)+" index "+str(valueindex)+" src "+files[i]+" dst "+dstjpg[valueindex])
            #remove labelme json file to labelme_json_dir
            src_path = dstjpg[valueindex].replace('.jpg','.json')
            new_path = os.path.join(src_compare_dir, files[i]).replace('.jpg','.json')
            os.system("copy "+src_path+" "+new_path)

if __name__ == '__main__':
    main()
