from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array = []
        for index, value in enumerate(strs):
            array.append((index, Counter(value)))

        result = {i:[] for i in range(len(array))}
        for i,j in array:
            for k,l in array:
                if j == l:
                    result[i].append(strs[k])
        
        final_result = []
        for i in result.values():
            if i not in final_result:
                final_result.append(i)
        
        return final_result
