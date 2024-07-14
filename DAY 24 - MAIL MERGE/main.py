#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../DAY 24 - MAIL MERGE/Input/Names/invited_names.txt","r") as file:
    names = file.readlines()

with open("../DAY 24 - MAIL MERGE/Input/Letters/starting_letter.txt","r") as file:
    letter = file.readlines()


final_names = []

for name in names:
    final_names.append(name.strip())

for name in final_names:
    with open(f"../DAY 24 - MAIL MERGE/Output/ReadyToSend/{name}.txt","w") as file:
        for i in range(len(letter)):
            if i ==0:
                file.write(letter[i].replace("[name]",name))
            else:
                file.write(letter[i])
