my_stuff = open("Hunter's_Eval.txt", "w")
print("Welcome to the course evaluation!")
print("Answer these questions as truthfully and as close to the truth as possible")

a = input("What did you like/dislike about Code Academy?")
b = input("What did you enjoy most about the class?")
c = input("How was the pace of the class? (Too fast, too slow, just right)")
d = input("What would you change about this class?")
e = input("Would you reccomend this class to a friend? Why or why not?")
print("Thank you for taking this course evaluation!")
my_stuff.write(a + b + c + d + e)
my_stuff.close()