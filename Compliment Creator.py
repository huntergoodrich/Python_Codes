import random
compliments_1 = ["pretty",
                 "handsome",
                 "nice",
                 "gorgeous",
                 "respectable",
                 "talented",
                 "kind",
                 "incredible",
                 "thoughtful",
                 "valuable",
                 "strong",
                 "great",
                 "radiant",
                 "awesome",
                 "respectful",
                 "amazing"]
compliments_2 = ["interesting",
                 "special",
                 "creative",
                 "artistic",
                 "athletic",
                 "fantastic",
                 "positive",
                 "tremendous",
                 "exemplary",
                 "marvelous",
                 "understanding",
                 "loving",
                 "fearless",
                 "tender",
                 "intelligent"]
compliments_3 = ["helpful",
                 "inspiring",
                 "trusworthy",
                 "unique",
                 "compassionate",
                 "delightful",
                 "joyful",
                 "dreamy",
                 "kindhearted",
                 "energetic",
                 "exciting",
                 "confident",
                 "jolly",
                 "beautiful"
                 "sightly"]
precursor = ["You are an extremely",
             "You are",
             "My mom is so",
             "My family is so"]
repeat = "yes"
while repeat == "yes" or repeat == "Yes":
    print (random.choice(precursor) + " " + random.choice(compliments_1) + "," + " " + random.choice(compliments_2) + "," + " " + "and" + " " + random.choice(compliments_3) + " " + "individual.")
    condition = input("Do you want to hear more? Yes or No?")
    if condition =="Yes" or condition == "yes":
        repeat = "yes"
    else:
        print ("Excuses, excues, excuses")
        repeat = "no"
