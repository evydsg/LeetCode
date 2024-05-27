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

# 709. To Lower Case
Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.

#### Example 1
**Input:**
```python
s = "Hello"
```
**Output:** 
```python
"hello"

```

#### Example 2
**Input:**
```python
s = "here"
```
**Output:** 
```python
"here"

```

##### Constraints
- 1 <= s.length <= 100
- s consists of printable ASCII characters.

# 2469. Convert the Temperature
You are given a non-negative floating point number rounded to two decimal places `celsius`, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array `ans = [kelvin, fahrenheit]`.

Return the array `ans`. Answers within `10-5` of the actual answer will be accepted.

## Note that:
- `Kelvin = Celsius + 273.15`
- `Fahrenheit = Celsius * 1.80 + 32.00`

#### Example 1
**Input:**
```python
celsius = 36.50
```
**Output:** 
```python
[309.65000,97.70000]

```

#### Example 2
**Input:**
```python
celsius = 122.11
```
**Output:** 
```python
[395.26000,251.79800]

```

##### Constraints
- 0 <= celsius <= 1000

# 707. Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.<br>
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.<br>
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

## Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

#### Example 1
**Input:**
```python
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
```
**Output:** 
```python
[null, null, null, null, 2, null, 3]

```

##### Constraints
- 0 <= index, val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

# 1700. Number of Students Unable to Eat Lunch
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.<br>

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a <b>stack</b>. At each step:<br>

- If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
- Otherwise, they will leave it and go to the queue's end.<br>

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.<br>

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the j​​​​​​th student in the initial queue (`j = 0` is the front of the queue). Return the number of students that are unable to eat.


#### Example 1
**Input:**
```python
students = [1,1,0,0]
sandwiches = [0,1,0,1]
```
**Output:** 
```python
0
```
##### Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].<br>
Hence all students are able to eat.

##### Constraints
- 1 <= students.length, sandwiches.length <= 100
- students.length == sandwiches.length
- sandwiches[i] is 0 or 1.
- students[i] is 0 or 1.

# 225. Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).<br>

Implement the MyStack class:<br>

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

##### Notes:
- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid. <br>
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations. <br>
#### Example 1
**Input:**
```python
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
```
**Output:** 
```python
[null, null, null, 2, 2, false]
```
##### Explanation:
- MyStack myStack = new MyStack();
- myStack.push(1);
- myStack.push(2);
- myStack.top(); // return 2
- myStack.pop(); // return 2
- myStack.empty(); // return False

##### Constraints
-  <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty.
- All the calls to pop and top are valid.

# 509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,<br>

```python
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```
Given n, calculate F(n).<br>

#### Example 1
**Input:**
```python
n = 2
[[], [1], [2], [], [], []]
```
**Output:** 
```python
1
```
##### Explanation:
- F(2) = F(1) + F(0) = 1 + 0 = 1.

##### Constraints
-  0 <= n <= 30

# 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.<br>

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?<br>


#### Example 1
**Input:**
```python
n = 2
```
**Output:** 
```python
2
```
##### Explanation:
There are two ways to climb to the top.
1. step + 1 step
2. steps

##### Constraints
-  1 <= n <= 45

# 771. Jewels and Stones
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.<br>

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.


#### Example 1
**Input:**
```python
jewels = "aA"
stones = "aAAbbbb"
```
**Output:** 
```python
3
```

##### Constraints
- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters.
- All the characters of `jewels` are unique.<br>
<br>
# 2236. Root Equals Sum of Children
You are given the `root` of a binary tree that consists of exactly `3 `nodes: the root, its left child, and its right child.<br>


Return `true` if the value of the root is equal to the sum of the values of its two children, or `false` otherwise.<br>


#### Example 1
**Input:**
```python
root = [10,4,6]
```
**Output:** 
```python
true
```
<br>

##### Explanation:
The values of the root, its left child, and its right child are 10, 4, and 6, respectively.<br>
10 is equal to 4 + 6, so we return true.
<br><br>
##### Constraints
-  The tree consists only of the root, its left child, and its right child.
- 100 <= Node.val <= 100

<br>

# 1. Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.<br>

You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>

You can return the answer in any order.

#### Example 1
**Input:**
```python
nums = [2,7,11,15]
target = 9
```
**Output:** 
```python
[0,1]
```

##### Explanation:
Because nums[0] + nums[1] == 9, we return [0, 1].
<br><br>

##### Constraints
-  2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- Only one valid answer exists.

<br>

# 344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.<br>

You must do this by modifying the input array in-place with O(1) extra memory.<br>

#### Example 1
**Input:**
```python
s = ["h","e","l","l","o"]
```
**Output:** 
```python
["o","l","l","e","h"]
```

##### Constraints
- `1 <= s.length <= 105`
- `s[i]` is a printable ascii character.

<br>

# 912. Sort an Array
Given an array of integers `nums`, sort the array in ascending order and return it.<br>

You must solve the problem without using any built-in functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.<br>

## Example 1
**Input:**
```python
nums = [5,2,3,1]
```
**Output:** 
```python
[1,2,3,5]
```

### Explanation
After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
<br>

## Constraints
- `1 <= nums.length <= 5 * 104`
- `5 * 104 <= nums[i] <= 5 * 104`

# 1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. <br>

Return the merged string

## Example 1
```python
word1 = "abc"
word2 = "pqr"
```
**Output:** 
```python
"apbqcr"
```

### Explanation
The merged string will be merged as so:<br>
word1:  a   b   c<br>
word2:    p   q   r<br>
merged: a p b q c r
<br>

## Constraints
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.

# 912. Sort an Array
Given an array of integers `nums`, sort the array in ascending order and return it.<br>

You must solve the problem without using any built-in functions in  `O(nlog(n))` time complexity and with the smallest space complexity possible.<br>

Return the merged string

## Example 1
```python
 nums = [5,2,3,1]
```
**Output:** 
```python
[1,2,3,5]
```

### Explanation
After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

## Constraints
- 1 <= nums.length <= 5 * 104
- 5 * 104 <= nums[i] <= 5 * 104

# 1470. Shuffle the Array
Given the array nums consisting of 2n elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.<br>

<i>Return the array in the form `[x1,y1,x2,y2,...,xn,yn]`.</i>



## Example 1
```python
nums = [2,5,1,3,4,7], n = 3
```
**Output:** 
```python
[2,3,5,4,1,7] 
```

### Explanation
 Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

## Constraints
- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10^3

<br>

# 1470. Shuffle the Array
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.<br>

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.




## Example 1
```python
flowerbed = [1,0,0,0,1], n = 1
```
**Output:** 
```python
true
```

## Constraints
- 1 <= flowerbed.length <= 2 * 104
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

<br>

# 75. Sort Colors
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
<br>

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



## Example 1
```python
nums = [2,0,2,1,1,0]
```
**Output:** 
```python
[0,0,1,1,2,2]
```

## Constraints
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2