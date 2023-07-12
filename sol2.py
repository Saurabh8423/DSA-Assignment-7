def is_strobogrammatic(num):
    left = 0
    right = len(num) - 1

    while left <= right:
        pair = num[left] + num[right]
        if pair not in ["00", "11", "69", "96", "88"]:
            return False
        left += 1
        right -= 1

    return True
num = "69"
print(is_strobogrammatic(num))  # Output: True
