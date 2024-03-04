import array_checker

checker = array_checker.Checker([-2, -3, 4, -1, -2, 1, 5, -3])

print(checker.max_sums(0, 7)) # 7
print(checker.max_sums(2, 7)) # 7
print(checker.max_sums(0, 5)) # 4
print(checker.max_sums(0, 0)) # 0
print(checker.max_sums(0, 1)) # 0
print(checker.max_sums(0, 2)) # 4
print(checker.max_sums(0, 3)) # 4
print(checker.max_sums(0, 4)) # 4
print(checker.max_sums(0, 5)) # 4
print(checker.max_sums(0, 6)) # 7
print(checker.max_sums(7, 7)) # 0
print(checker.max_sums(6, 7)) # 5
print(checker.max_sums(5, 7)) # 6
print(checker.max_sums(3, 3)) # 0
print(checker.max_sums(1, 3)) # 4
print(checker.max_sums(2, 5)) # 4


# Test cases from above with assert so you don't have to match the output to the comment...
assert checker.max_sums(0, 7) == 7, "Expected max_sums(0, 7) to be 7"
assert checker.max_sums(2, 7) == 7, "Expected max_sums(2, 7) to be 7"
assert checker.max_sums(0, 5) == 4, "Expected max_sums(0, 5) to be 4"
assert checker.max_sums(0, 0) == 0, "Expected max_sums(0, 0) to be 0"
assert checker.max_sums(0, 1) == 0, "Expected max_sums(0, 1) to be 0"
assert checker.max_sums(0, 2) == 4, "Expected max_sums(0, 2) to be 4"
assert checker.max_sums(0, 3) == 4, "Expected max_sums(0, 3) to be 4"
assert checker.max_sums(0, 4) == 4, "Expected max_sums(0, 4) to be 4"
assert checker.max_sums(0, 5) == 4, "Expected max_sums(0, 5) to be 4"
assert checker.max_sums(0, 6) == 7, "Expected max_sums(0, 6) to be 7"
assert checker.max_sums(7, 7) == 0, "Expected max_sums(7, 7) to be 0"
assert checker.max_sums(6, 7) == 5, "Expected max_sums(6, 7) to be 5"
assert checker.max_sums(5, 7) == 6, "Expected max_sums(5, 7) to be 6"
assert checker.max_sums(3, 3) == 0, "Expected max_sums(3, 3) to be 0"
assert checker.max_sums(1, 3) == 4, "Expected max_sums(1, 3) to be 4"
assert checker.max_sums(2, 5) == 4, "Expected max_sums(2, 5) to be 4"

print("All tests passed!")