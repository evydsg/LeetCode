# 26. Remove Duplicates from Sorted Array

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
<b>**Input:**</b> nums = [1,1,2] <br>
<b>Output:</b>2, nums = [1,2,_] <br>
<b>Explanation:</b> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores). <br>

#### Example 2:
<b>**Input:**</b> nums = [0,0,1,1,1,2,2,3,3,4]<br>
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
<b>**Input:**</b> nums = [3,2,2,3], val = 3 <br>
<b>Output:</b> 2, nums = [2,2,,] <br>
<b>Explanation:</b> Your function should return k = 2, with the first two elements of nums being 2 and 2 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores). <br>

#### Example 2:
<b>**Input:**</b> nums = [0,1,2,2,3,0,4,2], val = 2<br>
<b>Output:</b> 5, nums = [0,1,3,0,4,,,,,_]<br>
<b>Explanation:</b> Your function should return k = 5, with the first five elements of nums being 0, 1, 3, 0, and 4 respectively.<br>
It does not matter what you leave beyond the returned k (hence they are underscores).<br>
<<<<<<< HEAD

# 1929. Concatenation of Array
### Problem Statement
Given an integer array `nums` of length `n`, you want to create an array `ans` of length 2`n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`for 0 <= i < n (0-indexed).<br>

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

#### Example 1
**Input:**
```python
nums = [1,2,1]
```
**Output:** 
```python
ans = [1,2,1,1,2,1]
```
**Explanation:** 
The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

#### Example 2:

**Input:** 
```python
nums = [1,3,2,1]
```
**Output:** 
```python
ans = [1,3,2,1,1,3,2,1]
```
**Explanation:** 
The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

## Constraints:
- n == nums.length
- 1 <= n <= 1000
- 1 <= nums[i] <= 1000

# 682. Baseball Game
### Problem Statement
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.<br>
You are given a list of strings `operations`, where `operations[i]`is the `ith` operation you must apply to the record and is one of the following:<br>

- An integer x: Record a new score of x.
- '+': Record a new score that is the sum of the previous two scores.
- 'D': Record a new score that is the double of the previous score.
- 'C': Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

#### Example 1
**Input:**
```python
ops = ["5","2","C","D","+"]
```
**Output:** 
```python
30
```
**Explanation:** 
- "5": Add 5 to the record, record is now [5].
- "2": Add 2 to the record, record is now [5, 2].
- "C": Invalidate and remove the previous score, record is now [5].
- "D": Add 2 * 5 = 10 to the record, record is now [5, 10].
- "+": Add 5 + 10 = 15 to the record, record is now [5, 10, 15].<br>
The total sum is 5 + 10 + 15 = 30.

#### Example 2:

**Input:** 
```python
ops = ["5","-2","4","C","D","9","+","+"]
```
**Output:** 
```python
27
```

**Explanation:**
- "5": Add 5 to the record, record is now [5].
- "-2": Add -2 to the record, record is now [5, -2].
- "4": Add 4 to the record, record is now [5, -2, 4].
- "C": Invalidate and remove the previous score, record is now [5, -2].
- "D": Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
- "9": Add 9 to the record, record is now [5, -2, -4, 9].
- "+": Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
- "+": Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

## Constraints:
- 1 <= operations.length <= 1000
- operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
- For operation "+", there will always be at least two previous scores on the record.
- For operations "C" and "D", there will always be at least one previous score on the record.

# 20. Valid Parentheses
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

#### Example 1
**Input:**
```python
s = "()"
```
**Output:** 
```python
true
```
#### Example 2:

**Input:** 
```python
s = "()[]{}"
```
**Output:** 
```python
 true
```

=======
>>>>>>> 86c3a337991ce2e04ac64d300b128ada885b339b

# 155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.<br><br>
Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

#### Example 1
**Input:**
```python
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```
**Output:** 
```python
[null,null,null,null,-3,null,0,-2]
```
##### Explanation
- MinStack minStack = new MinStack();
- minStack.push(-2);
- minStack.push(0);
- minStack.push(-3);
- minStack.getMin(); // return -3
- minStack.pop();
- minStack.top();    // return 0
- minStack.getMin(); // return -2

# 21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.<br>
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.<br>
Return the head of the merged linked list.<br>

#### Example 1
**Input:**
```python
list1 = [1,2,4], list2 = [1,3,4]
```
**Output:** 
```python
[1,1,2,3,4,4]
```
##### Explanation
- The number of nodes in both lists is in the range [0, 50].
- 100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

# 206. Reverse Linked List
Given the `head` of a singly linked list, reverse the list, and return the reversed list.


#### Example 1
**Input:**
```python
head = [1,2,3,4,5]
```
**Output:** 
```python
[5,4,3,2,1]

```

#### Example 2
**Input:**
```python
head = [1,2]
```
**Output:** 
```python
[2,1]
```

##### Constraints
- The number of nodes in the list is the range [0, 5000].
- 5000 <= Node.val <= 5000

# 58. Length of Last Word
Given a string `s` consisting of words and spaces, return the length of the last word in the string.<br>

A word is a maximal 
substring
 consisting of non-space characters only.

#### Example 1
**Input:**
```python
s = "Hello World"
```
**Output:** 
```python
5
```

#### Example 2
**Input:**
```python
s = "   fly me   to   the moon  "
```
**Output:** 
```python
4
```

##### Constraints
- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.

# 1672. Richest Customer Wealth
You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i​​​​​​​​​​​th​​​`​ customer has in the `j​​​​​​​​​th`​​​​ bank. Return the wealth that the richest customer has. <br>

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

#### Example 1
**Input:**
```python
accounts = [[1,2,3],[3,2,1]]
```
**Output:** 
```python
6
```

#### Example 2
**Input:**
```python
accounts = [[1,5],[7,3],[3,5]]
```
**Output:** 
```python
10
```

##### Constraints
- m == accounts.length
- n == accounts[i].length
- 1 <= m, n <= 50
- 1 <= accounts[i][j] <= 100

# 1480. Running Sum of 1d Array
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.



#### Example 1
**Input:**
```python
nums = [1,2,3,4]
```
**Output:** 
```python
[1,3,6,10]
```

#### Example 2
**Input:**
```python
nums = [1,1,1,1,1]
```
**Output:** 
```python
[1,2,3,4,5]
```

##### Constraints
- 1 <= nums.length <= 1000
- 10^6 <= nums[i] <= 10^6
