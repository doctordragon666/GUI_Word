# -*- coding:utf-8 -*-
# 时间：
# 功能：GUI功能实现的测试
# 目的：
# 需求分析：
#

# msg = "Enter logon information"
# title = "Demo of multpasswordbox"
# fieldNames = ["Server ID", "User ID", "Password"]
# fieldValues = []  # we start with blanks for the values
# fieldValues = multpasswordbox(msg, title, fieldNames)
#
# # make sure that none of the fields was left blank
# while 1:
#     if fieldValues is None:
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         if fieldValues[i].strip() == "":
#             errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
#     if errmsg == "":
#         break  # no problems found
#     fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
# print("Reply was:", fieldValues)

import random


def choose(self: list):
    while True:
        choice = random.randint(1, 100)
        print(choice)
        if choice > 100:
            break


choose([])
# 运行结果
