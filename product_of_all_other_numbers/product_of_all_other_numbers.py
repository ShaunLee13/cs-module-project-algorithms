'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # determine the size of our array to
    # allocate memory for a new array to store products
    # which will start at 1 
    size = len(arr)
    prod = [1] * size

    # set up loop to iterate over each item in list
    for val in range(size):
        # this will be the variable we are not multiplying with; so we will pop it off to skip
        # the value at that index and reattach it later
        jump = arr.pop(val)
        # for each number remaining in the array, multiply the placeholder value in our products index
        # with the current value at num
        for num in arr:
            prod[val] *= num
        # after we're done, insert the skipped value back into the original array
        arr.insert(val,jump)
    return prod


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
