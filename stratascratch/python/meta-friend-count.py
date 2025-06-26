# Friend Count in User Array


# Last Updated: June 2025

# Medium
# ID 10404

# Question

# Given a 2D array of user IDs, find the number of friends a user has. Note that users can have none or multiple friends.

# Constraints
# The input variable user_ids is a 2D array of user IDs.
# Each element in the user_ids array is a list of integers representing the user IDs.
# The user IDs can be any positive or negative integer value.
# The user_ids array can have any number of rows and columns.
# The user IDs within each row can be in any order.
# The user_ids array can contain duplicate user IDs.
# The output variable is a dictionary (Dict[int, int]) where the keys are the user IDs and the values are the count of friends for each user.


# Solution

def count_friends(user_ids):
    """
    :type user_ids: List[List[int]]
    :rtype: Dict[int, int]
    """
    everyone = []
    for group in user_ids:
        for person in group:
            everyone.append(person)
            
    users = list(dict.fromkeys(everyone))
    
    output = {}
    for user in users:
        friends = 0
        for person in everyone:
            if user == person:
                friends += 1
        output[user] = friends
    
    return output
