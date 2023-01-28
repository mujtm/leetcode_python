def twoSum(nums, target: int):
    output = [int]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    indices = twoSum(nums, target)
    print(indices)
