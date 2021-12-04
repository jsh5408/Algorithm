## 1. Two Sum
https://leetcode.com/problems/two-sum/

#### My Answer 1: Accepted (Runtime: 652 ms - 37.24% / Memory Usage: 14.9 MB - 80.43%)
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                j = nums[i+1:].index(target - nums[i])
                return [i, i+j+1]
```
`target - nums[i]` 이 있으면 index 찾아서 return

#### Solution 1: Accepted (Runtime: 60 ms - 23.57% / Memory Usage: 15.6 MB - 9.55%)
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i 
```
저번에 풀었던 방식...ㅎ

`dic` 에 `target - nums[i]` 이름으로 대응하는 값의 인덱스를 넣어줌
