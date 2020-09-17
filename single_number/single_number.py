'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr): runtime of O(n^2), space of O(1)
#     # loop through every item in our list
#     for i in range(len(arr)):
#         # use python's count method to check whether an item
#         # has only one occurence
#         # if the check has a value of one,
#         # we can return the value at this index
#         if arr.count(arr[i]) == 1:
#             return arr[i]

def single_number(arr): # runtime of O(n), space of O(1)
    # we use this code with the XOr operator
    # a will start as 0, and in our loop each number will be added to it as such:
    # xor = 0 ^ 1 ^ 1 ^ 2 etc. when two numbers match they will 0 each other out,
    # at the end leaving only 0 and our odd number out, which will give us our answer
    a = 0
    for i in arr:
        a ^= i
    return a

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")