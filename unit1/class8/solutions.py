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

#############################
### Sorted Studio and bonus ###
#############################

def is_sorted(string):
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            return False
        
    return True

def after_comma(phrase):
    idx = phrase.find(",")
    return len(phrase[idx + 1:])

def pig_latin(phrase):
    words = phrase.split(" ")
    new_phrase = ""
    space_iterator = 0
    for word in words:
        new_phrase += word[1:] + word[0] + "ay"
        space_iterator += 1
        if space_iterator < (len(words)):
            new_phrase += " "

    return new_phrase

def pig_latin_4real(phrase):
    VOWELS = "aeiou"
    words = phrase.split(" ")
    new_phrase = ""
    space_iterator = 0
    for word in words:
        word_length = len(word)
        new_word = ""
        if VOWELS.find(word[0]) == -1:
            new_phrase += word[1:] + word[0] + "ay"
        else:
            new_word = word + "ay"
        space_iterator += 1
        new_phrase += new_word
        if space_iterator < (len(words)):
            new_phrase += " "

    return new_phrase
                
