#Lovescore: Calculates matches from name compared to str letter of TRUE and LOVE, and combines them as a str. For example: truescore = 4, lovescore = 5, combined_lovescore 45.


name1 = "Nakke Nakuttaja"
name2 = "Hessu Hopo"

def calculate_love_score(name1, name2):
    truescore = 0
    lovescore = 0
    
    list_name1 = list(name1.lower())
    list_name2 = list(name2.lower())
    combined_names = list_name1 + list_name2
    list_TRUE = ["t","r","u","e"]
    list_LOVE = ["l","o","v","e"]
    
    for i in list_TRUE:
        for x in combined_names:
            if i == x:
                truescore += 1
    
    for i in list_LOVE:
        for x in combined_names:
            if i == x:
                lovescore += 1
    
    str_truescore = str(truescore)
    str_lovescore = str(lovescore)
    combined_lovescore = str_truescore + str_lovescore
    print(combined_lovescore)

calculate_love_score(name1, name2)
        