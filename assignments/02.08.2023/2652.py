
class Solution(object):
    def sumOfMultiples(self, n):
        total_sum = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                total_sum += num
        return total_sum