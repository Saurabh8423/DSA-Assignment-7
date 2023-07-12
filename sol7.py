def backspaceCompare(s, t):
    def process_string(string):
        stack = []
        for ch in string:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return ''.join(stack)

    s_processed = process_string(s)
    t_processed = process_string(t)

    return s_processed == t_processed
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))  # Output: True
