---
template: leetcode
title: Two Sum
number: 1
link: https://leetcode.com/problems/two-sum
tags:
- array
- hash-table
---

{% for i in range(1,10) %}
```cpp
{% set file = "sol" + i| string() + ".cpp" %}
{{ include_file(file) }}
```
{% endfor %}