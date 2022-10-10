from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None  # 设置头节点和尾节点
        carry = 0       # 设置进位

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            # head为None，添加第一个节点
            if not head:
                head = tail = ListNode(sum % 10)
            # head不为None，添加新节点
            else:
                tail = ListNode(sum % 10)
                tail = tail.next
            
            carry = sum // 10  # 进位

            # 获取l1, l2的下一个节点
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # 如果还有进位，则将进位放进下一个节点
        tail.next = ListNode(carry) if carry else None

        return head
