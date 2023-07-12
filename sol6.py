def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    concatenated = s + s
    return goal in concatenated
s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))  # Output: True
