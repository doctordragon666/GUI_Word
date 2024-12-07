# -*- coding:utf-8 -*-
# 时间：2022年9月11日23点35分
# 功能：
# 目的：
# 注意事项
import random

from word import Word


class Fun:
    def __init__(self):
        """功能函数自定义"""
        self.word_lst = []
        self.init_lst()

    def init_lst(self):
        """
        初始化单词列表
        :return:
        """
        with open('src/word_for_test.txt', 'r', encoding='utf-8') as w:
            lst = w.readlines()
            for line in lst:
                w = line.strip('\n').split(',')
                self.word_lst.append(Word(w[1], w[0], w[2], w[3]))
                # 分别为中文，英语，练习次数，错误次数

    def add_word(self):
        """
        添加单词
        :return:
        """
        while True:
            c = input('请输入中文意思,按q结束')
            if c == 'q':
                break
            e = input('请输入英语意思')
            self.word_lst.append(Word(c, e))
        self.save()

    def del_word(self):
        """
        删除单词
        :return:
        """
        pass

    def memory_word(self):
        """记忆单词"""
        choice = input('请输入是中译英还是英译中\n1.记中文\n2.记英文\t')
        tmps = random.sample(self.word_lst, 10)
        if choice == '1':
            self.chinese_mode(tmps)
        elif choice == '2':
            self.english_mode(tmps)

    def english_mode(self, tmps):
        """
        英语模式
        :param tmps:单词样本
        :return:
        """
        while True:
            for tmp in tmps:
                print(tmp.chinese)
                answer = input('请输入英语')
                if answer == tmp.english:
                    print('正确')
                    tmp.times = str(int(tmp.times) + 1)
                    reply = input('您要删掉这个词吗按下1')
                    if reply == 1:
                        self.del_word()
                else:
                    print('错误')
                    tmp.times = str(int(tmp.times) + 1)
                    tmp.error = str(int(tmp.error) + 1)
            self.save()
            break

    def chinese_mode(self, tmps):
        """
        中文模式
        :param tmps:样本单词
        :return:
        """
        while True:
            for tmp in tmps:
                print(tmp.english)
                answer = input('请输入中文意思')
                if answer == tmp.chinese:
                    print('正确')
                    tmp.times = str(int(tmp.times) + 1)
                    reply = input('您要删掉这个词吗按下1')
                    if reply == 1:
                        self.del_word()
                else:
                    print('错误')
                    tmp.times = str(int(tmp.times) + 1)
                    tmp.error = str(int(tmp.error) + 1)
            self.save()
            break

    def show_word(self):
        """
        排序单词，并且打印单词
        :return:
        """
        self.word_lst.sort()
        for word in self.word_lst:
            word.show_self()
        self.save()

    def save(self, file_path='src/word_for_test.txt'):
        """
        保存文件
        :param file_path:文件路径，默认为项目下的src文件
        :return:
        """
        with open(file_path, 'w', encoding='utf-8') as w:
            for word in self.word_lst:
                w.write(word.put_in())

    def dictation_mode(self):
        """
        听写模式
        :return:
        """
        for word in self.word_lst:
            print(word.english)
            answer = input('输入中文意思')
            if answer == word.chinese:
                print("你答对了")
            elif answer == "q":
                break
            else:
                print("你打错了")