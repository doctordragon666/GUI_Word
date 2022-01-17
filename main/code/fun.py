# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 注意事项
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
                self.word_lst.append(Word(w[0], w[1], w[2], w[3]))
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
        choice = input('请输入是中译英还是英译中\n1.记中文\n2.记英文')
        if choice == '1':
            pass
        else:
            pass

    def show_word(self):
        self.word_lst.sort()
        for word in self.word_lst:
            word.show_self()

    def save(self):
        with open('words.txt', 'w', encoding='utf-8') as w:
            for word in self.word_lst:
                w.write(word.put_in())
