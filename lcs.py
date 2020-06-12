def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        nums_set = set(nums)
        print("set:", nums)

        max_value = 0
        count = 1
        for i in range(len(nums)):
            adj = nums[i]+1
            while adj in nums_set:
                count += 1
                adj += 1
            if count > max_value:
                max_value = count
            count = 1
        return max_value

print(longestConsecutive([]))
