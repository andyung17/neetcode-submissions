class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        pointer_one = 0
        pointer_two = len(s)
        curr_iter_index = 1
        max_length = 1
        seen = {}

        if s == "":
            return 0

        for index,letter in enumerate(s):
            if letter in seen:

                # 2 - 1, 2 - 0, 2,
                max_length = max(index - pointer_one, max_length)
                pointer_one = max(seen[letter] + 1, pointer_one)
                seen[letter] = index
                # pointer_one = pointer_one + 1
                # pointer_two = None

            seen[letter] = index

        return max(pointer_two - pointer_one, max_length)