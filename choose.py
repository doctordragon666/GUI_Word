# -*- coding:utf-8 -*-
# 时间：2022年9月11日20点13分
# 功能：给初学者的测试案例
# 目的：
# 需求分析：做一个简单的选择题算法
#
import random

datadic = {
    'this': '这个',
    'that': '那个',
    'aid': '援助;辅助物品;帮助 ',
    'algorithm': '算法',
    'assault': '袭击',
    'assemble': '集合',
    'assembly': '会议',
    'assert': '断言',
    'assess': '评价',
    'asset': '天赋',
    'assign': '赋值',
    'assignment': '作业',
    'assimilate': '吸收',
    'auditorium': '听众席'
}

if __name__ == '__main__':
    lst = []
    key_lst = [i for i in datadic.keys()]
    used_key = []
    result_dic = {}
    alpha = 'ABCDEFGHIJKLMN'
    i = int(input('请输入你需要的选项个数'))
    if i > len(key_lst):
        print('超出字典上限重试')
        exit()
    pos = random.randint(0, len(datadic) - 1)
    answer = key_lst[pos]
    print(f"请输入单词{answer}的意思")
    res = datadic[answer]
    used_key.append(answer)
    result_dic[answer] = res
    while len(used_key) < i:
        pos = random.randint(0, len(datadic) - 1)
        result = key_lst[pos]
        if result not in used_key:
            used_key.append(result)
    count = 0
    for i in used_key:
        if count % 4 == 0:
            print()
        print(alpha[count] + "." + datadic[i], end='   ')
        result_dic[alpha[count]] = datadic[i]
        count += 1
    while True:
        reply = input('请输入答案')
        if reply not in result_dic.keys():
            print('请输入正确的字符')
            continue
        elif reply == 'q':
            break
        else:
            if res == result_dic[reply]:
                print('正确')
            else:
                print('错误')
            break

# 运行结果
