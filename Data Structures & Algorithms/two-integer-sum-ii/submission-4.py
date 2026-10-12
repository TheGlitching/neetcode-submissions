class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            sum_current = numbers[start] + numbers[end]
            if sum_current==target:
                return [start+1, end+1]
            if sum_current<target:
                start += 1
            if sum_current>target:
                end -= 1