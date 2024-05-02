# 26 Remove Duplicates from Sorted Array

## Description
The removeDuplicates.py contains a solution to the "Remove Duplicates from Sorted Array" problem, along with additional information such as the problem statement, examples, and constraints.

### Problem Statement
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

### Custom Judge
The judge will test your solution with the provided code snippet. If all assertions pass, your solution will be accepted.

```python
nums = [...] # Input array
expectedNums = [...] # The expected answer with correct length

k = removeDuplicates(nums) # Calls your implementation

k == expectedNums.length
for index in range(k) {
    nums[index] == expectedNums[index];
}

```
#### Example 1
<b>Input:</b> nums = [1,1,2] <br>
<b>Output:</b>2, nums = [1,2,_] <br>
<b>Explanation:</b> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores). <br>

#### Example 2:
<b>Input:</b> nums = [0,0,1,1,1,2,2,3,3,4]<br>
<b>Output:</b> 5, nums = [0,1,2,3,4,,,,,_]<br>
<b>Explanation:</b> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.<br>
It does not matter what you leave beyond the returned k (hence they are underscores).<br>

# 27. Remove Element
## Description
The removeElement.py contains a solution to the "Remove Element" problem, along with additional information such as the problem statement, examples, and constraints.

### Problem Statement
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed. Then return `k` after removing all occurrences of `val` where `k` is the new length of the array after removal.

### Custom Judge
The judge will test your solution with the provided code snippet. If all assertions pass, your solution will be accepted.

```python
nums = [...] // Input array
val = ... // Value to remove
expectedNums = [...] // The expected answer with correct length

k = removeElement(nums, val) // Calls your implementation

k == expectedNums.length
for index in range(k) {
    nums[index] == expectedNums[index];
}
```
#### Example 1
<b>Input:</b> nums = [3,2,2,3], val = 3 <br>
<b>Output:</b> 2, nums = [2,2,,] <br>
<b>Explanation:</b> Your function should return k = 2, with the first two elements of nums being 2 and 2 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores). <br>

#### Example 2:
<b>Input:</b> nums = [0,1,2,2,3,0,4,2], val = 2<br>
<b>Output:</b> 5, nums = [0,1,3,0,4,,,,,_]<br>
<b>Explanation:</b> Your function should return k = 5, with the first five elements of nums being 0, 1, 3, 0, and 4 respectively.<br>
It does not matter what you leave beyond the returned k (hence they are underscores).<br>