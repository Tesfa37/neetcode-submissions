class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # 1. Ensure 'a' is the smaller array to minimize binary search range
        if len(b) < len(a):
            a, b = b, a

        # 2. Binary search pointers for array 'a'
        left, right = 0, len(a) - 1
        
        while True:
            # Midpoint index for array 'a'
            i = (left + right) // 2  
            # Corresponding index for array 'b' to maintain the half-size split
            j = half - i - 2         

            # 3. Retrieve partition boundaries with safety fallbacks for out-of-bounds
            aleft = a[i] if i >= 0 else float("-inf") # Note: Changed from inf to -inf
            aright = a[i+1] if (i + 1) < len(a) else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j+1] if (j + 1) < len(b) else float("inf")

            # 4. Check if we found the correct partition
            if aleft <= bright and bleft <= aright:
                # Odd total length: median is the minimum of the right elements
                if total % 2:
                    return min(aright, bright)
                # Even total length: average of the max-left and min-right elements
                return (max(aleft, bleft) + min(aright, bright)) / 2
            
            # 5. Adjust binary search window
            elif aleft > bright:
                right = i - 1  # Too many elements from 'a' on the left side
            else:
                left = i + 1   # Too few elements from 'a' on the left side