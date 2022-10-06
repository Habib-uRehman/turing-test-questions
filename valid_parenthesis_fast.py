def is_valid(string):
    # this ['N'] is used to stop pop() give an error.
    stack = ['N']
    m = {')': '(', ']': '[', '}': '{'}
    for i in string:
        if i in m.keys():
            if stack.pop() != m[i]:
                return False
        else:
            stack.append(i)
    # To check that we only have ['N'] left in stack
    return len(stack) == 1