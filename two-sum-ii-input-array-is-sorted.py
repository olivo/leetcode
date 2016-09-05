class Solution(object):
    def twoSum(self, numbers, target):
        lowIndex = 0
        highIndex = len(numbers) - 1
        while lowIndex < highIndex:
            if numbers[lowIndex] + numbers[highIndex] < target:
                lowIndex += 1
            elif numbers[lowIndex] + numbers[highIndex] > target:
                highIndex -= 1
            else:
                break
        return lowIndex + 1, highIndex + 1
