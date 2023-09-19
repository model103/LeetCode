from random import randint
class Helper:
    @staticmethod
    def partition(nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    @staticmethod
    def randomPartition(nums: List[int], l: int, r: int) -> int:
        i = randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return Helper.partition(nums, l, r)

    @staticmethod
    def quickSelected(nums: List[int], l: int, r: int, k: int) -> int:
        index = Helper.randomPartition(nums, l, r)
        if k == index:
            return nums[k]
        if k < index:
            return Helper.quickSelected(nums, l, index - 1, k)
        return Helper.quickSelected(nums, index + 1, r, k)

作者：力扣官方题解
链接：https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/solutions/1501230/zui-shao-yi-dong-ci-shu-shi-shu-zu-yuan-xt3r2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


@staticmethod
def quickSelected(nums: List[int], l: int, r: int, k: int) -> int:
    index = Helper.randomPartition(nums, l, r)
    if k == index:
        return nums[k]
    if k < index:
        return Helper.quickSelected(nums, l, index - 1, k)
    return Helper.quickSelected(nums, index + 1, r, k)
