from ListNode import ListNode
class Solution(object):
     
     def mergeTwoLists(self, list1, list2):
          """
          :type list1: Optional[ListNode]
          :type list2: Optional[ListNode]
          :rtype: Optional[ListNode]
          """
        
          firstNode = ListNode()
          currentNode = firstNode
          while list1 and list2:
               if list1.val < list2.val:
                    currentNode.next = list1
                    list1 = list1.next
               else:
                    currentNode.next = list2
                    list2 = list2.next

               currentNode = currentNode.next

          if list1:
               currentNode.next = list1
          if list2:
               currentNode.next = list2
               
          return firstNode.next
