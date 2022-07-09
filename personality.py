# Personality test program - Task One (Day 2)

# no. of books
# no. of points awarded

numberOfBooks = int(input ("enter the number of books:"))

# elif condition for our program
if (numberOfBooks == 0):
    points = 0
elif (numberOfBooks == 1):
    points = 6
elif (numberOfBooks == 2):
    points = 16
elif (numberOfBooks == 3):
    points = 32
elif (numberOfBooks >=4):
    points = 60

# final output of number of points
print ("Number of Points:", points)