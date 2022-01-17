# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 注意事项
class Word:
    def __init__(self, chinese, english, times='0', error='0'):
        self.chinese = chinese
        self.english = english
        self.times = times  # 记忆次数
        self.error = error

    def put_in(self):
        return self.english + "," + self.chinese + "," + self.times + "," + self.error + "\n"

    def show_self(self):
        print(self.english, self.chinese, self.error, self.times)

    def __lt__(self, other):
        if self.error > other.error:
            return True
        else:
            return False

# 运行结果
