from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [prev_node] -> [head] -> [next_node] -> ...
        # [prev_node] <- [head] -> [next_node] -> ...
        prev_node = None
        while head is not None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node


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


def test_reverse_list():
    solution = Solution()

    # Example 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Input: {print_linked_list(head1)}")
    result1 = solution.reverseList(head1)
    print(f"Output: {print_linked_list(result1)}")
    print(f"Expected: [5, 4, 3, 2, 1]\n")

    # Example 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    print(f"Input: {print_linked_list(head2)}")
    result2 = solution.reverseList(head2)
    print(f"Output: {print_linked_list(result2)}")
    print(f"Expected: [2, 1]\n")

    # Example 3: [] -> []
    head3 = create_linked_list([])
    print(f"Input: {print_linked_list(head3)}")
    result3 = solution.reverseList(head3)
    print(f"Output: {print_linked_list(result3)}")
    print(f"Expected: []\n")

    # Example 4: [1] -> [1]
    head4 = create_linked_list([1])
    print(f"Input: {print_linked_list(head4)}")
    result4 = solution.reverseList(head4)
    print(f"Output: {print_linked_list(result4)}")
    print(f"Expected: [1]\n")


if __name__ == "__main__":
    test_reverse_list()
