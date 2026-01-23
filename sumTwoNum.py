# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # stores the value of the node
        self.next = next    # pointer to the next node


# Function to create a linked list from a normal Python list
# Example: [2,4,3] → 2 -> 4 -> 3 -> None
def create_linked_list(arr):
    dummy = ListNode(0)     # dummy node (temporary head)
    current = dummy         # used to move through the list

    for x in arr:
        current.next = ListNode(x)  # create a new node
        current = current.next      # move to next node

    return dummy.next       # return actual head of linked list


# Function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


class Solution:
    def addTwoNumbers(self, l1, l2):

        # Dummy node to store result list
        head = ListNode(0)
        root = head          # keep reference to head
        carry = 0            # store carry value

        # Loop until both lists are finished
        while l1 or l2:
            # If l1 exists, take its value, else take 0
            v1 = l1.val if l1 else 0

            # If l2 exists, take its value, else take 0
            v2 = l2.val if l2 else 0

            # Add both digits and carry
            s = v1 + v2 + carry

            # Update carry (if sum ≥ 10)
            carry = s // 10

            # Store remainder as new node
            head.next = ListNode(s % 10)

            # Move result pointer
            head = head.next

            # Move l1 pointer if not None
            if l1:
                l1 = l1.next

            # Move l2 pointer if not None
            if l2:
                l2 = l2.next

        # If carry is still left, add new node
        if carry:
            head.next = ListNode(carry)

        # Return the result list (skip dummy node)
        return root.next


# ---------------- MAIN CODE (Testing in VS Code) ----------------

# Create first linked list: 2 -> 4 -> 3
l1 = create_linked_list([2, 4, 3])

# Create second linked list: 5 -> 6 -> 4
l2 = create_linked_list([5, 6, 4])

# Call function
result = Solution().addTwoNumbers(l1, l2)

# Print output
print("Result Linked List:")
print_linked_list(result)
