class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = ""
        mapping = {}
        for sym in s:
            mapping[sym] = mapping.get(sym, 0) + 1
        for sym in order:
            if sym in mapping:
                answer += sym * mapping[sym]
                mapping.pop(sym)
        for sym in mapping.keys():
            answer += sym * mapping.get(sym, 0)
        print(mapping)
        return answer