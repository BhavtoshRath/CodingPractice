
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if len(stack) == 0:
        return False
    return stack.pop()


def peek(stack):
    return stack[len(stack) - 1]
