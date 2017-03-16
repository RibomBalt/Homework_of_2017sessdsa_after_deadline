'''
给定由大写，小写字母和空格组成的字符串，返回 最后 一个单词的长度。

如果输入中不存在单词，返回 00。

注意：

“单词”是指不包含空格符号的字符串

例如：

对于字符串"hello World"（不带引号）, 那么返回的结果是 55；

对于字符串"abc abc "（不带引号），那么返回的结果就是 33。

输入格式

输入仅一行，为字符串 ss（长度不超过 1000010000）。

输出格式

输出 ss 中最后一个单词的长度。
'''
try:
    wordList = input().split(' ')
    wordList.reverse()
    # 共n个元素，循环n次
    for i in range(len(wordList)):
        # 空字符串删除
        if wordList[0] is '':
            wordList.remove('')
            continue
        else:
            # 确定为单词，输出
            print(str(len(wordList[0])))
            break
    # 删除了所有元素，证明全是空格，没有单词
    else:
        print('0')
# Python中的EOF异常，防止出现全文空字符串导致一上来就EOF的情况
except EOFError as e:
    print('0')
