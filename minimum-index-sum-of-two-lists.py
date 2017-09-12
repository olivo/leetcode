class Solution(object):
    def findRestaurant(self, list1, list2):
        list1_map = dict()

        for index in range(len(list1)):
            list1_map[list1[index]] = index

        min_sum = len(list1) + len(list2)
        min_val_map = dict()

        for index in range(len(list2)):
            if list2[index] in list1_map:
                if min_sum >= list1_map[list2[index]] + index:

                    new_min_sum = list1_map[list2[index]] + index

                    if new_min_sum not in min_val_map:
                        min_val_map[new_min_sum] = []

                    min_sum = new_min_sum
                    min_val_map[min_sum].append(list2[index])

        return min_val_map[min_sum]