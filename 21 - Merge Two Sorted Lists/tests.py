import unittest
from Solution import Solution

class TestLists(unittest.TestCase):
    
    def test_emptylist(self):
        sol = Solution()
        actualResult = sol.mergeTwoLists([], [])
        expectedResult = []
        self.assertEqual(actualResult, expectedResult, 'The empty list is wrong.')

    def test_mergelists(self):
        sol = Solution()
        actualResult = sol.mergeTwoLists([1,2,4], [1,3,4])
        expectedResult = [1,1,2,3,4,4]
        self.assertEqual(actualResult, expectedResult, 'The list is wrong.')


    def test_mergelists2(self):
        sol = Solution()
        actualResult = sol.mergeTwoLists([], [0])
        expectedResult = [0]
        self.assertEqual(actualResult, expectedResult, 'The list is wrong.')

if __name__ == '__main__':
    unittest.main()
