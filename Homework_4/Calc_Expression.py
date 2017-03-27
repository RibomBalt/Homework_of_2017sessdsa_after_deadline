import doctest


def calc_Expression (s):
    '''
    Function: 计算中缀表达式.

    包含把中缀表达式转换为后缀以及后缀求值的两个算法。
    合法运算符：+-*/^
    :param s:
    :return: 函数的结果

    测试用例：
    >>> print(calc_Expression('1 + 2 * 3'))
    7
    >>> print(calc_Expression('8 ^ 2 - 5 * 3'))
    49
    >>> print(calc_Expression('8 - 6 / 2 ^ 1'))
    5.0
    >>> print(calc_Expression('( 10 + 5 ) / 5'))
    3.0
    >>> print(calc_Expression('1 + 1 / 3 + 5 / 3 ^ 2'))
    1.8888888888888888
    '''
    # 分隔字符串
    calc = s.split()
    # 防止读取空栈，用一对括号把整个函数围起来，也可以保证最后把栈清空
    calc.append(')')
    num_stack = []
    symbol_stack = ['(']
    numbers = '0123456789'
    symbols = '+-*/^('
    # 优先级字典
    symbol_priority = {
        '(': 0,
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '^': 3,
    }
    # 二元函数字典
    # lambda表达式定义匿名函数
    symbol_functions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y,
    }

    try:
        for item in calc:
            # 判断是否为数字，是则压栈
            if item[0] in numbers:
                # 如果是整数，可以这么写，浮点用float，混杂用eval
                num_stack.append(int(item))
            # 判断是否为操作符或(
            elif item in symbols:
                # 顺序弹出优先级高的操作符，进行操作，排除两个左括号的比较
                top = symbol_stack.pop()
                while symbol_priority[top] >= symbol_priority[item] and not (top is item is '('):
                    # 对弹出的运算符进行执行，注意逆序
                    b = num_stack.pop()
                    a = num_stack.pop()
                    # 调用函数，用字典归一化处理，结果压栈
                    c = symbol_functions[top](a, b)
                    num_stack.append(c)
                    # 弹出下一个运算符
                    top = symbol_stack.pop()
                # 放回去
                symbol_stack.append(top)
                symbol_stack.append(item)
            # 判断)
            elif item is ')':
                # 和上一段差不多，遇到(时即可以弹出并停止
                top = symbol_stack.pop()
                while top is not '(':
                    # 对弹出的运算符进行执行，注意逆序
                    b, a = num_stack.pop(), num_stack.pop()
                    # 调用函数，用字典归一化处理，结果压栈
                    c = symbol_functions[top](a, b)
                    num_stack.append(c)
                    # 弹出下一个运算符
                    top = symbol_stack.pop()
                    # 不用放回去
            # 出现了非法的字符
            else:
                raise ValueError
        # 判断最终栈中元素数量是否正确
        if len(symbol_stack) is 0 and len(num_stack) is 1:
            return num_stack.pop()
        else:
            raise ValueError
    # 数字中混有其他符号，或者出现非法字符
    except ValueError:
        raise ValueError('出现非法表达式！')
    except IndexError:
        raise ValueError('出现非法表达式！')


# 主函数，doctest测试上面那几个样例
if __name__ == '__main__':
    doctest.testmod()
