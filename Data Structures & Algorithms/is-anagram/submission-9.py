
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_dict = Counter(s)
        # t_dict = Counter(t)

        # return s_dict == t_dict
        s_dict = dict()
        t_dict = dict()

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1

        return s_dict == t_dict
       