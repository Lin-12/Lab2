metachar = {'*': 50, '+': 50, '?': 50, '.': 40, '|': 30}


def convert(infix):
    stack = []
    postfix = ""

    for c in infix:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':  # pop from stack and add to postfix until open bracket
                postfix += stack.pop()
            stack.pop()  # pop the open bracket off the stack
        elif c in metachar:
            while stack and metachar.get(c, 0) <= metachar.get(stack[-1], 0):
                postfix += stack.pop()
            stack.append(c)
        else:
            postfix += c

    while stack:
        postfix += stack.pop()
    return postfix
