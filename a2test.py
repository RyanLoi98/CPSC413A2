import array_checker

checker = array_checker.Checker([-2, -3, 4, -1, -2, 1, 5, -3])
print(checker.max_sums(0, 7)) # 7
print(checker.max_sums(2, 7)) # 7
print(checker.max_sums(0, 5)) # 4
print(checker.max_sums(0, 0)) # -2