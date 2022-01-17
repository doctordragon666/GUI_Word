# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 注意事项
import random

from word import Word


class Fun:
    def __init__(self):
        self.word_lst = []
        self.init_lst()

    def init_lst(self):
        with open('words.txt', 'r', encoding='utf-8') as w:
            lst = w.readlines()
            for line in lst:
                w = line.strip('\n').split(',')
                self.word_lst.append(Word(w[1], w[0], w[2], w[3]))
                # 分别为中文，英语，练习次数，错误次数

    def add_word(self):
        while True:
            c = input('请输入中文意思,按q结束')
            if c == 'q':
                break
            e = input('请输入英语意思')
            self.word_lst.append(Word(c, e))
        self.save()

    def del_word(self):
        pass

    def memory_word(self):
        choice = input('请输入是中译英还是英译中\n1.记中文\n2.记英文\t')
        tmps = random.sample(self.word_lst, 10)
        if choice == '1':
            self.chinese_mode(tmps)
        elif choice == '2':
            self.english_mode(tmps)

    def english_mode(self, tmps):
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
        self.word_lst.sort()
        for word in self.word_lst:
            word.show_self()
        self.save()

    def save(self):
        with open('words.txt', 'w', encoding='utf-8') as w:
            for word in self.word_lst:
                w.write(word.put_in())
