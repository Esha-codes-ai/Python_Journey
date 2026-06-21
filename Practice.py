# In this file i wrote random codes to practice what output comes
# [1]
nums=[1,2,3,4,]
for n in nums:
    if n<3:
        nums.remove(n)
print(nums) #[2,3,4]

#[2]
nums=[10,20,30,40]
nums.remove(20) # remove the 20 value from the list
nums.pop(1)
print(nums) #[10,40]

#[3]

nums=[100,200,300,400]
nums.pop(3) # pop the 3rd index value of the list 
print(nums) #[100, 200, 400]
# [4]

nums=[1,2,3,4]
nums.append(5) # add 5 to the end of the list
print(nums) #[1, 2, 3, 4, 5]
