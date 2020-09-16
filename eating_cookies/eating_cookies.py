'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    left = n
    # create a list that will hold possible combinations depending on how many cookies exist
    eaten = [0] * (n + 1)
    # set up base cases
    # if theres 0 or only one, theres only 1 way
    if left <= 1:
        eaten[left] = 1
    elif left == 2:
        # can be eaten 1 twice or 2 once
        eaten[left] = 2
    else:
        # if no other conditions passed, the combination will be equal to the sum of recursion
        # on all 3 possible outcomes (eating 1, 2 and 3 cookies each)
        eaten[left] = eating_cookies(left - 1) + eating_cookies(left - 2) + eating_cookies(left - 3)
    return eaten[left]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
