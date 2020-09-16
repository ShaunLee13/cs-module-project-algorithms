'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # create an array to store all of the max values
    max_vals = []
    
    # if our window size is larger than our array, return None
    if k > len(nums):
        return
    else:
        # loop through the range of our array, creating a new temp array each time
        # to hold the contents of our window
        # NOTE: (- k + 1) is used to ensure that our loop stops when the end of our window == end of our array
        for num in range(len(nums) - k + 1):
            win = []
            # then determine the current window and append those values to temp array
            for i in range(k): 
                win.append(nums[num+i]) # the index at num+i is represented as current index + value as determined by the range of our window; from 0-max
            # using python's max, determine the max value in the window and append it to max_vals
            high = max(win)
            max_vals.append(high)
        # when all loops have ran, return max vals
        return max_vals


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
