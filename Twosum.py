class Solution(object):
    def twoSum(self, nums, target):
        """
        nums   : List of integers
        target : Integer value
        return : List containing indices of two numbers
        """

        seen = {}   # Dictionary to store number : index

        # Loop through the list
        for i in range(len(nums)):

            # Calculate the value needed to reach the target
            diff = target - nums[i]

            # Check if required value already exists
            if diff in seen:
                # If found, return the indices
                return [seen[diff], i]

            # Store the current number with its index
            seen[nums[i]] = i


# --------- VS CODE TESTING PART ---------

# Create object of Solution class
obj = Solution()

# Input values
nums = [2, 7, 11, 15]
target = 9

# Function call
result = obj.twoSum(nums, target)

# Print output
print("Indices:", result)
