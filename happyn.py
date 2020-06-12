def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    # 19
    # sumNum = 82
    # strNum = '82'
    # sumNum = 82
    # ele = 1
    seen_set = set()
    digit_sq_sum = 0
    while n != 1:
        strN = str(n) #'19'
        for ele in strN:
             digit_sq_sum += int(ele)**2
        n = digit_sq_sum #82
        if digit_sq_sum in seen_set:
            return False
        else:
            seen_set.add(digit_sq_sum)
            digit_sq_sum = 0
    return True

print(isHappy(5))
