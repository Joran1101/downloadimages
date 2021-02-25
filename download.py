#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021.2.25
# @Author  : Joran
# @Github    ：https://github.com/Joran1101

# 先获取html内容，进行提取标签，然后进行过滤获取地址，根据地址请求后保存本地

import requests
import re

num = 0
numPicture = 0
file = ''
List = []

def dowmloadPicture(html, keyword):
    global num
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url

    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = './' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        # if num >= numPicture:
        #     return


if __name__ == '__main__':  # 主函数入口
    header = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    word = input("请输入搜索关键词(可以是人名，地名等): ")

    num1 = 0
    while 1:
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
        r = requests.get(url + str(num1), headers=header, allow_redirects=False)
        r.encoding = 'utf-8'
        dowmloadPicture(r.text, word)
        num1 = num1+20
