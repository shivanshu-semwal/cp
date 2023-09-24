---
template: leetcode
title: Two Sum
number: 1
link: https://leetcode.com/problems/two-sum
tags:
- array
- hash-table
---

Given target $t$, and a list $l$, find pair of items whose sum is equal to $t$.

## Brute Force

```py
{{ include_file("solution3.py")}}
```

- $n$ - length of list
- Time Complexity - $O(n^2)$
- Space Complexity - $O(1)$

## Hashmap

Here given no $x$, you have to find $t - n$.

```py
{{ include_file("solution1.py")}}
```

- $n$ - length of list
- Time Complexity - $O(n)$
- Space Complexity - $O(n)$

## Sorting and then two pointer

If we are given sorted array we can solve this using two pointer approach.
Since we have to return index and not the number, we have to create another list with no. and it's index.

```py
{{ include_file("solution2.py")}}
```

- $n$ - length of list
- Time Complexity - $O(n \log(n))$
- Space Complexity - $O(n)$
