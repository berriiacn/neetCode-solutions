# 🧠 NeetCode 150 Solutions

Welcome to my repository of solutions for the [NeetCode 150](https://neetcode.io/roadmap) coding interview preparation roadmap. This is a collection of my personal solutions to popular LeetCode problems, structured by topic, written in Python.

---

## 🚀 Why I'm Doing This

I'm committed to sharpening my data structures and algorithms skills by following the structured and highly regarded NeetCode Roadmap. The goal is to build a strong foundation for technical interviews and deepen my problem-solving ability.

---

## 📚 Topics Covered

- ✅ Arrays & Hashing
- ✅ Two Pointers
- ✅ Sliding Window
- ✅ Stack
- ✅ Binary Search
- ✅ Linked List
- ⬜ Trees
- ⬜ Tries
- ⬜ Heap / Priority Queue
- ⬜ Backtracking
- ⬜ Graphs
- ⬜ 1D/2D Dynamic Programming
- ⬜ Greedy
- ⬜ Intervals
- ⬜ Math & Geometry
- ⬜ Bit Manipulation

(✅ = Completed, ⬜ = In Progress)

---

## 🛠️ How to Use

Each folder corresponds to a topic. Inside, you’ll find `.py` files for each problem with:
- Problem name and link
- My solution
- Optional time and space complexity notes

Example:
```python
# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Time: O(n), Space: O(n)
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
