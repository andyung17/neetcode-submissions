class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list = [0] * 26
        for char in s1:
            s1_list[ord(char) - 97] += 1

        for i in range(len(s2)):
            s2_list = [0] * 26
            if s1_list[ord(s2[i]) - 97] >= 1:
                for char in s2[i: i + len(s1)]:
                    s2_list[ord(char) - 97] += 1
                    if s2_list == s1_list:
                        return True
        return False