######################################################################
# Authors: Ntentia Dimitrios   TODO:
# Username: ntentiad                       TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Authors: Dimitrios Ntentia
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################

array = [["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig"],
[1972, 1984, 1996],
[1973, 1985, 1997],
[1974, 1986, 1998],
[1975, 1987, 1999],
[1976, 1988, 2000],
[1977, 1989, 2001],
[1978, 1990, 2002],
[1979, 1991, 2003],
[1980, 1992, 2004],
[1981, 1993, 2005],
[1982, 1994, 2006],
[1983, 1995, 2007],]

# (Required) Task 1
# TODO Ask user for their birth year
year = int(input("What year were you born?"))

active = True
arraycounter= 1
yearcounter= 1


if year < 1972:
    print("Please give me a date that is between and including 1972 and 2007.")
elif year > 2007:
    print("Please give me a date that is between and including 1972 and 2007.")
else:
    while active:
        if year == array[arraycounter][yearcounter - 1]:
            active = False
        else:
            yearcounter += 1
        if yearcounter == 4:
            yearcounter = 1
            arraycounter += 1
    zodiac= array[0][arraycounter-1]
    print("You're a " + zodiac + "!")
    year2 =int(input("What year was your friend born in?"))
    active = True
    arraycounter = 1
    yearcounter = 1
    if year2 < 1972:
        print("Please give me a date that is between and including 1972 and 2007.")
    elif year2 > 2007:
        print("Please give me a date that is between and including 1972 and 2007.")
    else:
        while active:
            if year2 == array[arraycounter][yearcounter - 1]:
                active = False
            else:
                yearcounter += 1
            if yearcounter == 4:
                yearcounter = 1
                arraycounter += 1
        zodiac = array[0][arraycounter - 1]
        print("Your friend is a " + zodiac + "!")












# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples

# Task 1 needs to consider only the years between your birth year and the following 11 years.
# For example, Dr. Scott Heggen was born in 1982, so his submission of Task 1 will consider the years 1982 to 1993.

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
