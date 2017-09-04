class Solution(object):
    def constructRectangle(self, area):
        current_value = int(math.sqrt(area))

        while current_value * (area / current_value) != area:
            current_value -= 1

        return [max(current_value, area / current_value), min(current_value, area / current_value)]