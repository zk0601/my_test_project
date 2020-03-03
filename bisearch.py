#  最常见的形式,采用左右闭区间（<=, +1 -1都于此有关）
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 找寻左边界
def leftboundSearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == len(nums) or nums[left] != target:
        return -1
    return left


def rightboundSearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[right] != target or right == -1:
        return -1
    return right


a = [1,2,2,2,3,4,5,5]
print(rightboundSearch(a, 5))