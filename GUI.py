# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：

import random

from easygui import *

from word import Word


#
# def save():
#
#
# if __name__ == '__main__':
#     try:
#         save()
#
#
#         #def msgbox(msg="(Your message goes here)", title="", ok_button="OK"):
#         ynbox()
#         buttonbox()
#         indexbox(msg="shall we go")
#         boolbox()
#         multchoicebox()
#         integerbox()
#         multenterbox()
#         multpasswordbox()
#         textbox()
#         codebox()
#         fileopenbox()
#         filesavebox()
#         diropenbox()
#         image = "OMEN Earth Day 2021.jpg"
#         msg = "Do you like this picture?"
#         choices = ["Yes", "No", "No opinion"]
#         reply = buttonbox(msg, image=image, choices=choices)
#         while 1:
#             msgbox("Hello, world!", "sad ")
#
#             msg = "What is your favorite flavor?"
#             title = "Ice Cream Survey"
#             choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
#             choice = choicebox(msg, title, choices)
#
#             # note that we convert choice to string, in case
#             # the user cancelled the choice, and we got None.
#             msgbox("You chose: " + str(choice), "Survey Result")
#
#             msg = "Do you want to continue?"
#             title = "Please Confirm"
#             if ccbox(msg, title):  # show a Continue/Cancel dialog
#                 pass  # user chose Continue
#             else:
#                 sys.exit(0)  # user chose Cancel
#     except:
#         exceptionbox()
#


class Setting(EgStore):
    def __init__(self, filename):
        """设置永久存储"""
        super(EgStore, self).__init__()
        self.file_pos = ""
        self.filename = filename


settingsFilename = r"D:\Python\Word_Memery\main\setting.txt"  # Windows example
settings = Setting(settingsFilename)


def init_lst(self: list):
    """初始化单词列表"""
    with open('src/word.txt', 'r', encoding='utf-8') as w:
        lst = w.readlines()
        for line in lst:
            w = line.strip('\n').split(',')
            self.append(Word(w[1], w[0], w[2], w[3]))
            # 分别为中文，英语，练习次数，错误次数


def add_word(self: list):
    """添加单词"""
    while True:
        c = enterbox(msg='请输入中英文意思，用空格隔开')
        if c is None:
            save(self)
            break
        if c == "":
            continue
        lst = c.split(' ')
        self.append(Word(lst[0], lst[1]))


def memory_word(self: list):
    """记单词模式：包含中文英文和混记"""
    mode = ['记中文', '记英文', '混记(开发中)']
    choice = indexbox("选择模式", choices=mode)

    if len(self) < 10:
        samples = self
    else:
        samples = random.sample(self, 10)
    if choice == 0:
        chinese_mode(self, samples)
    elif choice == 1:
        english_mode(self, samples)


def english_mode(self: list, tmps):
    """
    英语模式
    :param self:单词列表
    :param tmps:单词样本
    :return:
    """
    for tmp in tmps:
        answer = enterbox(msg=f'请输入{tmp.chinese}的英语')
        if answer is None:
            break
        elif answer == tmp.english:
            msgbox("正确")
            # tmp.times = str(int(tmp.times) + 1)
            # reply = input('您要删掉这个词吗按下1')
            # if reply == 1:
            #     del_word()
        else:
            msgbox(f'错误, 正确答案是{tmp.english}')
            tmp.times = str(int(tmp.times) + 1)
            tmp.error = str(int(tmp.error) + 1)
    save(self)


def chinese_mode(self: list, tmps):
    """
    中文选择模式
    :param self:单词列表
    :param tmps:
    :return:
    """
    for tmp in tmps:
        answer = enterbox(msg=f'请输入{tmp.english}的中文')
        if answer is None:
            break
        elif answer == tmp.chinese:
            msgbox("正确")
            # tmp.times = str(int(tmp.times) + 1)
            # reply = input('您要删掉这个词吗按下1')
            # if reply == 1:
            #     self.del_word()
        else:
            msgbox(f'错误, 正确答案是{tmp.english}')
            tmp.times = str(int(tmp.times) + 1)
            tmp.error = str(int(tmp.error) + 1)
    save(self)


def del_word(self, word: Word):
    if word in self:
        del word
    save(self)
    msgbox("已经删除该动词")


def save(self: list):
    """
    保存单词运行结果
    :param self: 要保存的单词列表
    :return: void
    """
    if settings.file_pos == "":
        settings.file_pos = fileopenbox("请选择自己的单词库")
        settings.store()
    with open(settings.file_pos, 'w', encoding='utf-8') as w:
        for word in self:
            w.write(word.put_in())


def show_word(self: list):
    """
    显示单词
    :param self:单词
    :return:
    """
    self.sort()
    seed = ''
    for word in self:
        seed += word.put_in() + '\n'
    textbox(msg="英文，中文，练习次数，错误次数", title="所有结果", text=seed)


def search_word(self: list):
    """
    查找单词
    :param self:
    :return:
    """
    while True:
        self_dic = {}
        for i in self:
            self_dic[i.english] = i.chinese
        substance = enterbox(msg="请输入要查询的单词", title="搜索")
        if substance is None:
            break
        elif substance in self_dic.keys():
            msgbox(f"结果已经找到, {self_dic[substance]}")
        elif substance in self_dic.values():
            key_list = []
            for key, value in self_dic.items():
                if value == substance:
                    key_list.append(key)
            msgbox(f"结果已经找到，{key_list}")
        else:
            msgbox("没有此单词")


def choose(self: list):
    while True:
        answer = random.randint(0, len(self) - 1)
        choice_lst = {self[answer].english}
        while len(choice_lst) < 4:
            choice_lst.add(self[random.randint(0, len(self))].english)
        choice_lst = list(choice_lst)
        random.shuffle(choice_lst)
        choice = choicebox(msg=f"选出{self[answer].chinese}的意思", title="选择题", choices=choice_lst)
        if choice is None:
            break
        elif choice == self[answer].english:
            msgbox("你的答案正确")
        else:
            msgbox(f"正确答案为：{self[answer].english}")
        del choice_lst


main_menu = ['增加单词',
             '记忆单词',
             '展示单词',
             '单词听写',
             '选择题',
             '搜索单词',
             '退出系统']

if __name__ == '__main__':
    word_lst = []
    init_lst(word_lst)
    while True:
        result = choicebox(title="主界面", choices=main_menu, msg="请选择你的操作, cancel退出系统")
        print(result)
        if result is None:
            break
        elif result == "增加单词":
            add_word(word_lst)
            continue
        elif result == "记忆单词":
            memory_word(word_lst)
            continue
        elif result == "展示单词":
            show_word(word_lst)
            continue
        elif result == "单词听写":
            continue
        elif result == "搜索单词":
            search_word(word_lst)
            continue
        elif result == "选择题":
            choose(word_lst)
            continue
        elif result == "退出系统":
            exit(1)
        else:
            continue
