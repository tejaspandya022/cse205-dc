class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(list)
        most_common = []

        for num in nums:
            num_dict[num].append(num)

        val_list = sorted(num_dict.values(), key = len, reverse=True)

        for group in val_list[:k]:
            most_common.append(group[0])

        return sorted(most_common)

         
        