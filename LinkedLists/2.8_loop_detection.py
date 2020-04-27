def detect_loop(self):
    current = self.head
    fast = slow = current
    prev = current

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return None

def detect_loop_2(self):
    current = self.head
    fast = slow = current

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = current
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None

#         s = set()
#         while head:
#             if head in s:
#                 return head
#             else:
#                 s.add(head)
#                 head = head.next

#         return None