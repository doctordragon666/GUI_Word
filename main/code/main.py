# -*- coding:utf-8 -*-
# 时间：2022年1月16日21点17分
# 功能：记单词
# 目的：
# 注意事项
from fun import Fun
import os

if __name__ == '__main__':
    start = Fun()  # 实例化操作对象
    while True:
        print('---------------------')
        print('------1.增加单词-------')
        print('------2.记忆单词-------')
        print('------3.展示单词-------')
        print('------4.单词听写-------')
        print('------0.退出系统-------')
        print('---------------------')
        select = input('请输入你的操作')
        if select == '0':
            os.system("pause")
            break
        elif select == '1':
            start.add_word()
        elif select == '2':
            start.memory_word()
        elif select == '3':
            start.show_word()
        os.system("pause")
        os.system("cls")

# 运行结果
