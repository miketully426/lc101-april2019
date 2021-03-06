#############################
### Chapter 9: Exercise 4 ###
#############################

def reverse(text):
    result = ""
    for num in range(len(text) -1 , -1, -1):
        result += text[num]
    return result

#############################
### Chapter 9: Exercise 5 ###
#############################

def is_palindrome(text):
    return reverse(text) == text

#############################
### Chapter 9: Exercise 7 ###
#############################

def encrypt(message, key):
    new_message = ""
    for let in message.lower():
        if let.isalpha():  
            new_message += key[ord(let) - 97]
        else:
            new_message += let
    return new_message



