#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#names = []
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    
for n in range(len(names)):
    names[n] = names[n].strip()

with open("Input/Letters/starting_letter.txt") as sample_letter:
    letter = sample_letter.readlines()

for n in range(len(names)):
    name_to_replace = "[name]" if n == 0 else names[n-1]
    letter[0] = letter[0].replace(name_to_replace, names[n])
    with open(f"Output/ReadyToSend/letter_for_{names[n]}.txt", "w") as output_file:
        output_file.writelines(letter)
    