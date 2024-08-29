import collections
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        steps = collections.defaultdict(set)
        steps[0].add(0)

        for i in range(len(stones)):
            if stones[i] in steps:
                for prev_step in steps[stones[i]]:
                    if prev_step > 0:
                        steps[stones[i] + prev_step].add(prev_step)
                    if prev_step > 1:
                        steps[stones[i] + prev_step - 1].add(prev_step - 1)
                    steps[stones[i] + prev_step + 1].add(prev_step + 1)

        return stones[-1] in steps
