#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:09:16 2021

@author: CCloveHH
"""


from weiboa import get_topics
#换成自己的微博cookies啊
cookies = {'Cookie': 'Your own weibo Cookie'}
#设置相关参数
get_topics(topic='杨笠吐槽直男盲目自信', maxpage=40, cookies=cookies, csvf='#杨笠吐槽直男盲目自信#.csv')