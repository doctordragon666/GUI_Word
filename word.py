# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 注意事项

class Word:
    def __init__(self, chinese, english, times='0', error='0'):
        """单词类定义：中文英文次数错误"""
        # self.dic = {chinese:english}
        self.chinese = chinese
        self.english = english
        self.times = times  # 记忆次数
        self.error = error

    def put_in(self):
        """设置写入文件的格式"""
        return self.english + "," + self.chinese + "," + self.times + "," + self.error + "\n"

    def show_self(self):
        """设置打印的格式"""
        print(self.english, self.chinese, self.error, self.times)

    def __lt__(self, other):
        """重载比较符号"""
        if self.error > other.error:
            return True
        else:
            return False

# 运行结果
