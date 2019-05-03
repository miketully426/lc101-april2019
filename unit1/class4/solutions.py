#############################
### Chapter 6: Exercise 5 ###
#############################

def is_even(n):
    return n % 2 == 0

#############################
### Chapter 6: Exercise 7 ###
#############################

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

##############################
### Chapter 6: Exercise 11 ###
##############################

def date_of_easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = 22 + d + e
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        date = date - 7
    if date > 31:
        return "April " + str(date - 31)
    else:
        return "March " + str(date)


