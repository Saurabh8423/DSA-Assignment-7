def reverseStr(s, k):
    s = list(s)
    i = 0
    while i < len(s):
        s[i:i+k] = reversed(s[i:i+k])
        i += 2 * k
    return ''.join(s)
s = "abcdefg"
k = 2
print(reverseStr(s, k))  # Output: "bacdfeg"
