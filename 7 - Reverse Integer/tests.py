import unittest
from Solution_first import Solution

class TestLists(unittest.TestCase):
    
    def test_123(self):
        sol = Solution()
        actualResult = sol.reverse(123)
        expectedResult = 321
        self.assertEqual(actualResult, expectedResult, "321 test")

    def test_minus123(self):
        sol = Solution()
        actualResult = sol.reverse(-123)
        expectedResult = -321
        self.assertEqual(actualResult, expectedResult, "-321 test")
        
    def test_120(self):
        sol = Solution()
        actualResult = sol.reverse(120)
        expectedResult = 21
        self.assertEqual(actualResult, expectedResult, "120 test")

    def test_0(self):
        sol = Solution()
        actualResult = sol.reverse(0)
        expectedResult = 0
        self.assertEqual(actualResult, expectedResult, "0 test")

    def test_1534236469(self):
        sol = Solution()
        actualResult = sol.reverse(1534236469)
        expectedResult = 0
        self.assertEqual(actualResult, expectedResult, "1534236469 test")

if __name__ == '__main__':
    unittest.main()
