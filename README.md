# Recursive Maximum Subarray Sum

This is my solution to **Assignment 2, Question #4** for **CPSC 413 (Design and Analysis of Algorithms I – Winter 2024)** at the University of Calgary.

This program implements a **recursive algorithm**—as taught in lecture—for computing the **maximum subarray sum** within a given range of an integer array. It follows the divide-and-conquer strategy from lecture and intentionally avoids optimizations such as dynamic programming or removing recursive calls, as per assignment instructions.

---

## 📘 Problem Description

Given:

* An array of integers (`array`)
* Two indices `start` and `end`

The program determines the **maximum possible sum** of any **contiguous subarray** that lies entirely between `start` and `end` (inclusive). The result is just the **maximum sum**, not the subarray or its indices.

---

## 🧠 Algorithm Details

The core of the solution is implemented in the `lecture_algorithm` method of the `Checker` class. It recursively computes the following values for a given subarray:

* `max_left_aligned_sum`: Maximum sum of a left-aligned subarray
* `max_right_aligned_sum`: Maximum sum of a right-aligned subarray
* `max_subarray_sum`: Maximum sum of any subarray
* `sum_of_all_elements`: Total sum of the current subarray

These values are combined recursively by dividing the array into halves, and merging results based on the classic divide-and-conquer subarray algorithm.

**Base Case**: When `start == end`, the result depends on whether the single element is negative or non-negative.

---

## ✅ Sample Usage

```python
from checker import Checker

my_array = [3, -2, 5, -1, 2, -4, 6]
checker = Checker(my_array)

# Find max subarray sum between indices 0 and 6
print(checker.max_sums(0, 6))  # Output: 9
```

---

## 🧪 Testing

You can run the program using the included `a2test.py` script, like so:

```bash
python3 a2test.py
```

Ensure both `array_checker.py` and the test file `a2test.py` are in the same directory.

Or you can create a different test script using `a2test.py` as a starting point.

---

## 🛠 Features

* Clean recursive implementation based on lecture material
* Returns maximum subarray sum between any two indices
* Handles all integers between 0 and 99,999
* No optimizations or iterative shortcuts—pure recursion

---

## 📌 Technologies

* Python 3
* No external dependencies

---

## 🧑‍🎓 Educational Value

This assignment showcases how to:

* Apply **divide and conquer** strategies for problem-solving
* Structure recursive functions for subarray problems
* Understand **maximum subarray** algorithms

---

## 🖼️ Screenshot of Example Run

![Example Output](https://imgur.com/shNBqtw.png)

