def threeSum(nums):
    np = []
    nums.sort()
    if (len(nums) < 3):
        return (np)
    else:
        di = {nums[i]: i for i in range(2, len(nums), 1)}
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                zero = 0 - (nums[i] + nums[j])
                if (zero in di.keys()) and (di.get(zero) > j):
                    num_sort = [nums[i], nums[j], zero]
                    #    num_sort.sort()
                    if not (num_sort in np):
                        np.append(num_sort)
        return (np)