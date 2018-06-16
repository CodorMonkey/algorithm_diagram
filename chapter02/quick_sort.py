import random

from common.log_time import log_time


def quick_sort1(nums):
    n = len(nums)
    if n < 2:
        return nums
    else:
        mid = n // 2
        pivot = nums[mid]
        less = []
        greater = []
        for num in nums[:mid] + nums[mid + 1:]:
            if num < pivot:
                less.append(num)
            else:
                greater.append(num)
        return quick_sort1(less) + [pivot] + quick_sort1(greater)


def quick_sort2(nums, start, end):
    if start >= end:
        return

    left = start
    right = end
    mid = nums[start]
    while left < right:
        # 如果right位置的对象大于等于mid，right向左侧移动
        while left < right and nums[right] >= mid:
            right -= 1
        # right位置的对象小于mid，将right位置的对象放到left位置
        nums[left] = nums[right]

        # left做对应操作
        while left < right and nums[left] < mid:
            left += 1
        nums[right] = nums[left]

    nums[left] = mid
    # left right 重叠时，左侧都小于mid，右侧都大于等于mid
    # 对左右两侧进行递归操作
    quick_sort2(nums, start, left - 1)
    quick_sort2(nums, left + 1, end)


def quick_sort3(nums, start, end):
    if start >= end:
        return

    left = start
    right = end
    mid = nums[(start + end) // 2]
    while left < right:
        # 如果right位置的对象大于等于mid，right向左侧移动
        while left < right and nums[right] >= mid:
            right -= 1

        # left做对应操作
        while left < right and nums[left] < mid:
            left += 1
        # 左右都不动的时候，交换left right位置的对象
        nums2[left], nums2[right] = nums2[right], nums2[left]

    # left right 重叠时，左侧都小于mid，右侧都大于等于mid
    # 对左右两侧进行递归操作
    quick_sort3(nums, start, left - 1)
    quick_sort3(nums, left + 1, end)


@log_time
def invoke1(*args):
    return quick_sort1(*args)


@log_time
def invoke2(*args):
    return quick_sort2(*args)


@log_time
def invoke3(*args):
    return quick_sort3(*args)


if __name__ == '__main__':
    # nums1 = [x for x in range(500, 0, -1)]
    nums2 = [x for x in range(100000)]
    random.shuffle(nums2)
    # print(nums2)

    # print(quick_sort(nums1))
    # print(count)

    invoke1(nums2)

    invoke3(nums2, 0, len(nums2) - 1)
    # print(nums2)

    # count = 0
    # quick_sort2(nums2, 0, len(nums2) - 1)
    # print(nums2)
    # print(count)
