class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define hash map
        result = {}

        # Iterate over the nums list
        for index, x in enumerate(nums):
            # Calculate the complement 
            complement = target - x

            # Check if complement exist in hash map or not
            if(complement in result):
                # We have found the result
                return [index, result[complement]]
            
            # Store the current number to hash map
            result[x] = index


        
