class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current, reversedList = head, None

        while current:
            previous = current.next
            current.next = reversedList
            reversedList = current
            current = previous
        
        return reversedList