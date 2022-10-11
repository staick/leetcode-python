# 1790. Check if One String Swap Can Make Strings Equal
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        str_list = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                str_list.append(s1[i])
                str_list.append(s2[i])

        if (
            len(str_list) == 4
            and str_list[0] == str_list[3]
            and str_list[1] == str_list[2]
        ):
            return True
        return False
