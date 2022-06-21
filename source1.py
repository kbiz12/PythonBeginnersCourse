import time


# Hiya, and welcome to my first github project, (not really), this is a project to intorudce you to python completely! Let's get started, shall we?

# Python was found in 1991, and is currently a really friendly beginner programming language, so its good you chose this language!

# This tutorial will help you with the understanding of python completely!

# Let's start with creating something really easy! Follow my steps!


# Let's do;

print('Hello there! And welcome to my tutorial!') # I'd like you to run this code and see the output! This should print "Hello there! And welcome to my tutorial!" . Press the play icon in the top right (for visual studio code)!

# Once you run this code, it should output the line we implemented in the print() section!

# Feel free to mess about with this code, and change it to what you like!

# Now that you know how to make a print() method, let's create some variables! 

# Variables are something like this;

my_age = 45

hiya_there_print = 'Hiya there! This is a variable (string)'

# Variables are alot more easy as you can input how many variables you'd like in one print! Instead of writing the whole text! Let me show you.

print(my_age, hiya_there_print)

# This should pring out the my_age = 45, and hiya_there_print string! Run the code and try it!

# As you can see, it has printed the correct information we gave the variables!

# This is awesome! You've learned 2 things in the space of 4 - 5 minutes! Well done!

# Now we'll create another variable, but this time, it's gonna be something called LEVEL!

# This is the fun part... We're going to create a little mini-game to get started!

# I will write the code for you and you can change anything you like! To get the game to your likings!

# Feel free to run this code to see what it will do!

# variable 1 = level

level = 0

# 0 is the current players level!

# FUNCTIONS!

# def Function(self): is a function!

def Play_1():
    import random
    random_num = random.randint(5,10) # IMPORT RANDOM! DO "import random" at the top of the code or in this function! # RANDOM_NUM WILL GENERATE A NUMBER BETWEEN (0, yournum)
    random_lucky = random.randint(5,10)
    level = 0
    print('Lucky number is', random_num)
    print('You`re random number is, ',random_num) # WILL PRINT THERE RANDOM NUMBER!
    if random_num == random_lucky:
        time.sleep(3) # DO "IMPORT TIME" above this command!
        print('\n\nYOU GOT THE LUCKY NUMBER! CONGRATULATIONS!')
        level =+ 5 # This will give them +5 LEVELS!
        print('\n\nYou`re level has updated, it`s now: ',level)
    else:
        time.sleep(3)
        print('\n\nOoh! Sorry you did not get the lucky number today!')
        print('Due to not getting the lucky number, this means you will not gain a level! Try again next time. Level is still at: ',level)
        level = 0
    
Play_1()

# RUN THIS CODE TO GET AN IDEA OF WHAT U CAN MAKE! 

# TRY CREATING UR OWN GAME UNDER THIS LINE NOW THAT I'VE GAVE YOU AN IDEA ON WHAT TO DO! FEEL FREE TO ADD : BUCKS, TIME, ETC! MAKE IT URS! 








# ------------------------------------------
# END OF SOURCE 1! PLEASE HEAD OVER TO SOURCE 2 TO GET ONTO THE NEXT STEP!
# ------------------------------------------

# CONGRATULATIONS FOR FINISHING THIS! 


print('YOU DID GREAT! ADIOS, ENJOY SOURCE 2!')