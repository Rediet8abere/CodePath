# If we list all the natural numbers below 10 that
# are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of
# all the multiples of 3 or 5 below 1000.

def threeOrFive():
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # num = 1
    # sum = 23
    # store sum in a var
    three_five_sum = 0
    # generate numbers upto 1000
    for num in range(1, 1000):
        # add num if it is divisible by 3 or 5
        if num%3 == 0 or num%5 == 0:
            three_five_sum += num
    return three_five_sum
    # return the sum
print(threeOrFive())
