import Solution
from ListNode import ListNode


def produceListOfNodes(listToParse):
     firstNode = None
     for element in listToParse:
          currentNode = ListNode(element)
          if firstNode is None:
               firstNode = currentNode
               previousNode = currentNode
          else:
               previousNode.next = currentNode
               previousNode = currentNode
     return firstNode     

def printListOfNodes(firstNode):
     currentNode = firstNode
     while currentNode is not None:
          print(currentNode.val,end=' ')
          currentNode = currentNode.next
        
def main():
     sol = Solution.Solution()
     ListNode1 = produceListOfNodes([1,2,4])
     ListNode2 = produceListOfNodes([1,3,4])
     newNode = sol.mergeTwoLists(ListNode1, ListNode2)
     printListOfNodes(newNode)

if __name__ == "__main__":
    main()
