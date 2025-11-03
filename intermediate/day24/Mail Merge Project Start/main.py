#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = open("./Input/Letters/starting_letter.txt")
content = letter.read()
letter.close()

names = open("./Input/Names/invited_names.txt")
str_names = names.read()
list_of_names = str_names.split()
names.close()

for name in list_of_names:
   new_content = content.replace("[name]", name)

   f = open(f"{name}.txt", "x")
   f.write(new_content)



