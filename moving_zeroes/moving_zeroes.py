'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr): #runtime O(n?)
    # check for numbers that are not 0; these will be to the left
    # check for numbers that are zero; these will be on the right
    
    # chain these two checks together and return
    return [num for num in arr if num != 0] + [zero for zero in arr if zero == 0]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")