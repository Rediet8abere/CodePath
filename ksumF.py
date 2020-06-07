"""
Given k target find the minumum number
of fib numbers that can add to the target
"""
# 1, 1, 2, 3, 5, 8, 13, 21, 34 ....
# input 7 = 1, 1, 2, 3
# input 7 = 2, 5
# output: 2

# input 13 = 13
# output: 1
def kFib(target):
    fibSum1 = 0
    fibSum2 = 1
    fibSum = 0
    fibList = [0, 1]
    # [0, 1, 1, 2, 3, 5, 8]
    # # generate fib seq upto the target
    # while target is greater than fibSum keep generating
    while target >= fibSum:
        fibSum = fibSum1 + fibSum2
        fibSum1 = fibSum2
        fibSum2 = fibSum
        # store the fibSum in a list
        fibList.append(fibSum)




    # # [0, 1, 1, 2, 3, 5, 8, 13, 21]
    # target: 0
    # count: 1
    # ele: 2
    # print("fibList: ", fibList)
    count = 0
    index = len(fibList)-1
    # keep sub until target is zero
    while target > 0:
        print(fibList[index], target)
        # if ele is less than target or equal the target
        if fibList[index] <= target:
            # substract ele from the target and update the target
            target -=  fibList[index]
            # increament count
            count += 1
            # move the index to the left
            index -= 1
        else:
            # move the index to the left
            index -= 1
    # print("count: ", count)
    return count
print(kFib(7))  #result:2
print(kFib(13)) #result:1
print(kFib(19)) #result:3
