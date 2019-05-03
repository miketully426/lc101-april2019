#############################
### Chapter 8: Exercise 9 ###
#############################

import image

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        new_r = (p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        new_g = (p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        new_b = (p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

        new_pixel = image.Pixel(new_r, new_g, new_b)

        new_img.setPixel(col, row, new_pixel)

new_img.draw(win)
win.exitonclick()

#############################
### If given the table below with high temps for each day 
### in a three week span, create a function that can print 
### out the average temp for each week.
#############################

table = [[56, 58, 53, 45, 56, 63, 59], [54, 63, 64, 68, 64, 63, 70], [73, 68, 65, 73, 67, 65, 74]]

def average_temps(temps):

  for row in range(len(temps)):
    temp_temps = 0
    for column in range(len(temps[row])):
       temp_temps += table[row][column]
       
    print(temp_temps)

average_temps(table)



