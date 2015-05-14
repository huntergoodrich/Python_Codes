#This is a letter-grade calculator
def letter_grade(number):
    if 100 >= number and number >= 90.5:
        return "A"
    elif 90.4 >= number and number >= 80.5:
        return "B"
    elif 80.4 >= number and number >= 70.5:
        return "C"
    elif 70.4 >= number and number >= 60.5:
        return "D"
    else:
        return "F"
print(letter_grade(70.9385639376548347))
