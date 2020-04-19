#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19
# @Author  : Karobben
# @Site    : China
# @File    : VedioSlice.py
# @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',
                    help='Input vedio file')     #输入文件
parser.add_argument('-o','-U','--output', default = "out_test.avi",
                    help='Output vedio file, default as "out_test.avi"')     #输入文件
parser.add_argument('-f','-F','--FPS', type = int, default = 24,
                    help='Start from X second. default from 24')     #输入文件

#获取参数
args = parser.parse_args()
File = args.input
OUTPUT = args.output
fps = args.FPS

import cv2, os


List = os.popen('ls '+File).read().split('\n')[:-1]

img = cv2.imread(File +"/"+List[0])
#print(File +"/"+List[0])
size = (len(img[0]),len(img))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)
for i in List:
    img = cv2.imread(File +"/"+i)
    videowriter.write(img)

videowriter.release()



#for i in $(du Pic/*|tr '\t' '=');do if [ $(echo $i|awk -F'=' '{print $1}') -lt 1010 ]; then mv $(echo $i|awk -F'=' '{print $2}') trash;fi;done
