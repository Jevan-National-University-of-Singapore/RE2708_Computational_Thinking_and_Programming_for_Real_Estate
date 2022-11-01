class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = x

        if x < 0:
            x = -x
        
        if x < 10: return True

        x_list = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

        i = 0
        while x > 0:
            x_list[i] = x%10
            x //= 10
            i += 1


        x_reverse = 0
        for idx in range(i):
            x_reverse += x_list[idx] * (10 ** (i-1-idx))

        return True if x_reverse == x_copy else False


solution = Solution()

print(solution.isPalindrome(10))
