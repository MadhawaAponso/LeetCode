from typing import List

class Solution:
    def stringToNumber(self, number: str) -> int:
        return sum(int(digit) for digit in number)

    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        num_dict = {}

        for num in nums:
            digit_sum = self.stringToNumber(str(num))
            if digit_sum in num_dict:
                max_sum = max(max_sum, num + num_dict[digit_sum])
                num_dict[digit_sum] = max(num_dict[digit_sum], num)
            else:
                num_dict[digit_sum] = num

        return max_sum
