import sys
n=0
while True:
    try:
        s=input()
        # if s == '-1':
        #     break
        n+=list(s).count('$')
    except EOFError as e:
        print(n)
        break