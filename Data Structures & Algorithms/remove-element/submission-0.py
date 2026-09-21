class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for n in nums:
            if n != val:
                result.append(n)

        nums[:] = result  
        return len(nums)
