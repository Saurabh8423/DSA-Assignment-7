def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for ch_s, ch_t in zip(s, t):
        if ch_s in s_to_t:
            if s_to_t[ch_s] != ch_t:
                return False
        else:
            s_to_t[ch_s] = ch_t

        if ch_t in t_to_s:
            if t_to_s[ch_t] != ch_s:
                return False
        else:
            t_to_s[ch_t] = ch_s

    return True
s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True
