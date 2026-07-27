class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s) if len(s) >= len(t) else len(t)
        count = 0

        find = s if len(s) > len(t) else t
        what = t if len(t) < len(s) else s
        print('find', find)
        print('what', what)
        find_ = sorted(find)
        what_ = sorted(what)
        for i in range(len(find_)):
            if find_[i] == what_[i]:
                count += 1
        
        if count == length:
            return True
        return False