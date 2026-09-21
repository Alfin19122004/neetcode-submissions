class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1   # ✔ correctly update dictionary

        max_count = -1
        ans = -1

        for key, value in count.items():
            if value > max_count:   # ✔ use value, NOT 'val'
                max_count = value
                ans = key
        
        return ans

