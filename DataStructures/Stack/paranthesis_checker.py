def paranthesisChecker(expr):
    s = []

    for i in expr:
        if i == '(' or i == '[' or i =='{':
            s.append(i)
            continue

        if len(s) == 0:
            return False

        if i == ')':
            x = s.pop()
            if x == '[' or x == '{':
                return False

        if i == ']':
            x = s.pop()
            if x == '(' or x == '{':
                return False

        if i == '}':
            x = s.pop()
            if x == '(' or x == '[':
                return False

    if len(s):
        return True
    else:
        return False


paranthesisChecker("{()}[]")