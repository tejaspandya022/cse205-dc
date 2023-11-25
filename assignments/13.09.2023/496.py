class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums2)-1
        st = []
        m = max(nums2)

        for i in range(len(nums1)):
            n = nums2.index(nums1[i])
            if n >= l or nums1[i] == m :
                st.append(-1)
            else:
                for j in range(n+1,len(nums2)):
                    if nums2[j] > nums1[i]:
                        st.append(nums2[j])
                        break
                else:
                    st.append(-1)
                    
            
        return st
            