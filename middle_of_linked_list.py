from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head.next
        fast = head.next.next
        while fast is not None:
            if fast.next is not None:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        return slow


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    """Helper function to print linked list values."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_middle_node():
    solution = Solution()

    # Example 1: [1,2,3,4,5] -> middle is 3
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.middleNode(head1)
    print(f"Input: {print_linked_list(head1)}")
    print(f"Output node value: {result1.val if result1 else None}")
    print(f"Remaining list from middle: {print_linked_list(result1)}")
    print(f"Expected: 3 (remaining: [3, 4, 5])\n")

    # Example 2: [1,2,3,4,5,6] -> middle is 4
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    result2 = solution.middleNode(head2)
    print(f"Input: {print_linked_list(head2)}")
    print(f"Output node value: {result2.val if result2 else None}")
    print(f"Remaining list from middle: {print_linked_list(result2)}")
    print(f"Expected: 4 (remaining: [4, 5, 6])\n")

    # Example 3: [1] -> middle is 1
    head3 = create_linked_list([1])
    result3 = solution.middleNode(head3)
    print(f"Input: {print_linked_list(head3)}")
    print(f"Output node value: {result3.val if result3 else None}")
    print(f"Remaining list from middle: {print_linked_list(result3)}")
    print(f"Expected: 1 (remaining: [1])\n")

    # Example 4: [1,2] -> middle is 2
    head4 = create_linked_list([1, 2])
    result4 = solution.middleNode(head4)
    print(f"Input: {print_linked_list(head4)}")
    print(f"Output node value: {result4.val if result4 else None}")
    print(f"Remaining list from middle: {print_linked_list(result4)}")
    print(f"Expected: 2 (remaining: [2])\n")


if __name__ == "__main__":
    test_middle_node()
