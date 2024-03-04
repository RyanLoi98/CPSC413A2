class Checker(object):
    def __init__(self, array):
        self.array = array

    # recursive function to determine the maximum sum of the inputted subarray with indices between start and end (inclusive)
    # returns 4 values: max_left_aligned_sum, max_right_aligned_sum, max_subarray_sum, sum_of_all_elements of the given array
    def lecture_algorithm(self, start, end):
        # recursive case when the array has more than one element
        if start != end:
            # recurse on the left side of the array
            L_max_left_aligned_sum, L_max_right_aligned_sum, L_max_subarray_sum, L_sum_of_all_elements = self.lecture_algorithm(start, ((start + end)//2))

            # recurse on the right side of the array
            R_max_left_aligned_sum, R_max_right_aligned_sum, R_max_subarray_sum, R_sum_of_all_elements = self.lecture_algorithm((((start + end)//2) + 1), end)

            # calculate the 4 return values
            max_left_aligned_sum = max(L_max_left_aligned_sum, (L_sum_of_all_elements + R_max_left_aligned_sum))
            max_right_aligned_sum = max(R_max_right_aligned_sum, (R_sum_of_all_elements + L_max_right_aligned_sum))
            max_subarray_sum = max((L_max_right_aligned_sum + R_max_left_aligned_sum), L_max_subarray_sum, R_max_subarray_sum)
            sum_of_all_elements = L_sum_of_all_elements + R_sum_of_all_elements

            return max_left_aligned_sum, max_right_aligned_sum, max_subarray_sum, sum_of_all_elements

        # base case when the array only has one element
        else:
            # values for an array with a single element
            max_left_aligned_sum = 0
            max_right_aligned_sum = 0
            max_subarray_sum = 0

            # if the single element is negative, all values for the array except the sum of all elements is 0
            if self.array[start] < 0:
                sum_of_all_elements = self.array[start]

            # otherwise all values for the array is equal to that element
            else:
                max_left_aligned_sum = self.array[start]
                max_right_aligned_sum = self.array[start]
                max_subarray_sum = self.array[start]
                sum_of_all_elements = self.array[start]

            return max_left_aligned_sum, max_right_aligned_sum, max_subarray_sum, sum_of_all_elements


    # function that determines the maximum sum of a subarray with indices between start and end (inclusive) with the help
    # of our recursive algorithm based on the lecture
    def max_sums(self, start, end):
        # calls our recursive function with the start and end indices
        max_left_aligned_sum, max_right_aligned_sum, max_subarray_sum, sum_of_all_elements = self.lecture_algorithm(start, end)

        # return the maximum possible sum of a subarray with indices between start and end (inclusive)
        return max_subarray_sum
