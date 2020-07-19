from math import ceil
# List = [1, 2, 23, 12424, 3, 3, 344, 3, 56, 7, 87, 8, 9,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,5,6,10]


# class Solution(object):
#     def majorityElement(self, nums: List) -> int:
#         print(len(nums))
#         new_list = []
#         while True:
#             for i in range(len(nums) // 2):
#                 if nums[i] != nums[-i-1]:
#                     new_list.append(i)
#                     new_list.append(-i-1)
#             print(new_list)
#             temp=[]
#             for j in new_list:
#                 temp.append(nums[j])
#             for k in temp:
#                 nums.remove(k)
#             new_list=[]
#             print('nums:',nums)
#             if len(set(nums)) == 1:
#                 return nums[0]

List = [3,2,3]
class Solution(object):
    def majorityElement(self, nums: List) -> int:
        while True:
            temp = []
            for i in range(len(nums) // 2):
                if nums[i] == nums[-i - 1]:
                    temp.extend([nums[i],nums[-i - 1]])
            sorted(temp)
            nums = temp
            if len(set(nums)) == 1:
                break
        return nums[0]

test = Solution()
a = test.majorityElement(nums=List)
print(a)
