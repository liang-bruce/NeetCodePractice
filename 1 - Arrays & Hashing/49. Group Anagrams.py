from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # special case
        if len(strs) == 1:
            return [strs]

        mapCollection = defaultdict(list)

        for i, val in enumerate(strs):
            currTuple = self.getCurrTuple(val)
            # same operation (syntax) for both first occurence and multiple occurence
            mapCollection[currTuple].append(val)
        
        # return result in specified format  
        return mapCollection.values()

    def getCurrTuple(self, string: str) -> dict[str: int]:
        # returning tuple for further operation because tuples are hashable (immutable)
        # orginally thought of returning dict but it is unhashable
        count = [0] * 26
        for char in string:
            count[ord(char) - ord('a')] += 1
        return tuple(count)