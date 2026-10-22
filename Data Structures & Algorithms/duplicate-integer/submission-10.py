class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        haseset = set()
        for n in nums:
            if n in haseset:
                return True
            haseset.add(n)
        return False