from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        def get_map(g_items, g_char):
            g_map, count = [], 0
            for item in g_items:
                if g_char in item:
                    g_map.append(item.count(g_char))
                else:
                    g_map.append(0)

            if sum(g_map) == 0:
                return 0, 0

            max_travel = max([idx for idx, val in enumerate(g_map) if val != 0])
            return g_map, max_travel

        def get_garbage_time(garbage_item, travel_times, char):
            i, travel_time = 1, 0
            g_map, max_travel = get_map(garbage_item, char)
            if g_map == 0 and max_travel == 0:
                return 0

            while i < len(garbage_item):
                if i <= max_travel:
                    travel_time += travel_times[i-1]
                i+=1
            return travel_time + sum(g_map)

        paper_time = get_garbage_time(garbage, travel, 'P')
        glass_time = get_garbage_time(garbage, travel, 'G')
        metal_time = get_garbage_time(garbage, travel, 'M')

        return paper_time + glass_time + metal_time


# garbage = ["G", "P", "GP", "GG"]
garbage = ["MMM","PGM","GP"]
# travel = [2, 4, 3]
travel = [3,10]

result = Solution()
print(result.garbageCollection(garbage, travel))
