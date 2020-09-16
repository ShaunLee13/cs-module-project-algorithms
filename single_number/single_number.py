'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # loop through every item in our list
    for i in range(len(arr)):
        # use python's count method to check whether an item
        # has only one occurence
        # if the check has a value of one,
        # we can return the value at this index
        if arr.count(arr[i]) == 1:
            return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")