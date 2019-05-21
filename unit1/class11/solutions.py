#############################
### Chapter 12: Exercise 3  ###
#############################

    def reflect_x(self):
        return Point(self.x, self.y * 1)

#############################
### Chapter 12: Exercise 3  ###
#############################

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y/self.x



#############################
### Counting Studio       ###
#############################

    test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

    char_count = {}

    for char in test_string:

        if not char_count.get(char):
            char_count[char] = 1
        else:
            char_count[char] += 1

    for (char, count) in char_count.items():
        print(char + ":", count)
