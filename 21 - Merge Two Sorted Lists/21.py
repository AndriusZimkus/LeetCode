import Solution

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
        
def main():
     sol = Solution.Solution()
     print(sol.mergeTwoLists([1,2,4], [1,3,4]))

if __name__ == "__main__":
    main()
