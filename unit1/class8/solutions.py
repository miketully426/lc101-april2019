#############################
### Chapter 10: Exercise  ###
#############################

def sum_of_squares(nums):
    sum = 0
    for num in nums:
        sum += num ** 2
    return sum

#############################
### Chapter 10: Exercise 10 ###
#############################

def replace(word, old, new):
    return word.replace(old, new)

#############################
### Chapter 10: Exercise 11 ###
#############################

def sum_of_initial_odds(nums):
    sum = 0
    for num in nums:
        if num % 2 == 1:
            sum += num
        else:
            break
    return sum



