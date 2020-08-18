from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):

                    # Process a
                    a = arr[i]
                    for num in range(i + 1, j):
                        a = a ^ arr[num]
                    
                    # Process b
                    b = arr[j]
                    for num in range(j + 1, k + 1):
                        b = b ^ arr[num]

                    if(a == b):
                        count += 1
                        print(i, j, k)

        return count


S = Solution()
print(S.countTriplets([1,1,1,1,1]))