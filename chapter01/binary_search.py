def binary_search(item_list, item):
    low = 0
    high = len(item_list) - 1
    while low <= high:
        mid = (low + high) // 2
        res = item_list[mid]
        if res == item:
            # 找到元素，返回索引
            return mid
        elif res < item:
            # 中间元素小于目标元素，继续查找(mid,high]之间的元素
            low = mid + 1
        else:
            # 中间元素大于目标元素，继续查找[low,mid)之间的元素
            high = mid - 1
    return None
