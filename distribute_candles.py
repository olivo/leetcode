class Solution(object):
    def distributeCandies(self, candies):
        candle_types = set()

        for candy in candies:
            candle_types.add(candy)

        return min(len(candle_types), len(candies) / 2)