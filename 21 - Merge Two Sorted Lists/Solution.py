class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = []

        i1 = 0
        i2 = 0
        while i1 < len(list1) or i2 < len(list2):

            if i1 >= len(list1):
                currentElement = list2[i2]
                i2 += 1
                newList.append(currentElement)
                continue
            
            if i2 >= len(list2):
                currentElement = list1[i1]
                i1 += 1
                newList.append(currentElement)
                continue

            if list1[i1] < list2[i2]:
                currentElement = list1[i1]
                i1 += 1
            else:
                currentElement = list2[i2]
                i2 += 1
            
            newList.append(currentElement)
            
        return newList
        
