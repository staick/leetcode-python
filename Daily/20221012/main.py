# 817. Linked List Components
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)  # 因为需要多次判断值是否位于数组中，用一个哈希集合保存数组中的点可以降低时间复杂度
        count = 0
        in_set = False
        while head:
            if head.val not in nums:
                in_set = False
            elif not in_set:
                in_set = True
                count += 1
            head = head.next

        return count
