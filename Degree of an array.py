# Given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


from collections import Counter

x = list(map(int, input().split(",")))
cnt = Counter(x)
degree = max(cnt.values())
print(cnt)
first = {}
last = {}
for i in x:
    if i not in first:
        first[i] = x.index(i)
    last[i] = x.index(i)

# for i,num in enumerate(x):
#     print(f"{i} : {num}")

for i,num in enumerate(x):
    if num not in first:
        first[num] = i
    last[num] = i

ans = [last[i] - first[i] + 1 for i in cnt.keys() if cnt[i] == degree]
# for i in cnt.keys():
#     if cnt[i] == degree:
#         ans.append(last[i] - first[i] + 1)

print(f"Degree of list({x}) : {min(ans)}")