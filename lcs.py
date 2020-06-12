def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count_set = set()
        max_value = 0
        count = 1
        is_cons = False
        for i in range(len(nums)):
            count = 1
            cons = nums[i]+1
                # check consucative number
            for j in range(len(nums)):
                #check for consucative conucative if it exisits
                for k in range(len(nums)):
                    is_cons = False
                    if cons == nums[k]:
                        is_cons = True
                        count += 1
                        break
                if not is_cons:
                    break
                elif is_cons:
                    cons += 1
            if count > max_value:
                max_value = count
            # count_set.add(count)
            # count = 0
        # print("count: ", count)
        # print("count_set: ", max_value)
        return max_value
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
