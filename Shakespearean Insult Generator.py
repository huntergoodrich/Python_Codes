import random
insults_1 = ["artless",
             "bawdy",
             "beslubbering",
             "bootless",
             "clouted",
             "craven",
             "dissembling",
             "droning",
             "lumpish",
             "reeky",
             "surly",
             "saucy",
             "vain",
             "mangled",
             "fobbing"]
insults_2 = ["base-court",
             "clay-brained",
             "dizzy-eyed",
             "hell-hated",
             "rump_fed",
             "shard_borne",
             "spur-galled",
             "swag-bellied",
             "ill-breeding",
             "idle-headed",
             "tardy-gaited",
             "weather-bitten",
             "elf-skinned",
             "crook-pated",
             "pox-marked"]
insults_3 = ["apple-john",
             "giglet",
             "dewberry",
             "lout",
             "scut",
             "vassal",
             "wagtail",
             "harpy",
             "hedge-pig",
             "foot-licker",
             "pig-nut",
             "moldwarp",
             "haggard",
             "malt-worm",
             "varlot",]
precursor = ["Thou",
             "Ye",
             "You",
             "Thee"]

repeat = "yes"
while repeat == "Yes" or repeat == "yes":
    print (random.choice(precursor) + " " + random.choice(insults_1) + " " +  random.choice(insults_2) + " " +  random.choice(insults_3))
    condition = input("Do you want to hear more? Yes or No? ")
    if condition == "yes" or condition == "Yes":
        repeat = "yes"
    else:
        print ("You're missing out.")
        repeat = "no"

    
