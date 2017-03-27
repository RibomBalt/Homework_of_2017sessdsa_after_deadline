import re


def html_match (html):
    '''
    判断字符串是否为标准HTML形式，是返回true，否则false

    不能判断含有诸如<br>这样标签的HTML
    :param html: 待匹配字符串
    :return: TRUE/False
    >>> html_match('<a><b></b></a><<')
    True

    '''
    # 正则表达式，仅匹配标签，得到两个组，分别是/和标识符
    pattern = r'<(/?)([A-Za-z][0-9A-Za-z]*)>'
    tags = re.findall(pattern, html)
    tag_stack = []
    try:
        for tag in tags:
            if tag[0] is '/':
                last_tag = tag_stack.pop()
                # 对比标识符内容是否相同
                if last_tag[1] != tag[1]:
                    return False
            else:
                tag_stack.append(tag)
        # 遍历完毕，若非空则
        return not bool(tag_stack)
    except IndexError as e:
        # 异常说明对空栈弹出，不匹配
        return False


# 测试从文件读入HTML文件，测试文件一同打包
if __name__ == '__main__':
    with open('html_test.html') as f:
        html_list = f.readlines()
        print(html_match(''.join(html_list)))
