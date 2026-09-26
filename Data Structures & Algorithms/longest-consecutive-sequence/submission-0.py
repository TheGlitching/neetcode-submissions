class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:

            if (num-1) in nums_set:
                continue

            current_num = num
            current_sequence = 1

            while (current_num+1) in nums_set:
                current_sequence += 1
                current_num += 1

            longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence