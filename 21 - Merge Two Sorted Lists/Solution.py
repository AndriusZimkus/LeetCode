from ListNode import ListNode
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        firstNode = None
        nextNode1 = list1
        nextNode2 = list2
        
        while nextNode1 is not None or nextNode2 is not None:

            if nextNode1 is None:
                nextNode = nextNode2
                nextNode2 = nextNode2.next

            elif nextNode2 is None:
                nextNode = nextNode1
                nextNode1 = nextNode1.next
            elif nextNode1.val < nextNode2.val:
                nextNode = nextNode1
                nextNode1 = nextNode1.next
            else:
                nextNode = nextNode2
                nextNode2 = nextNode2.next


            if nextNode is not None:
                currentNode = ListNode(nextNode.val)
                if firstNode is None:
                    firstNode = currentNode
                    previousNode = currentNode
                else:
                    previousNode.next = currentNode
                    previousNode = currentNode

        return firstNode
