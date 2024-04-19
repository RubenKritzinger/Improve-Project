


name_length = len(input(" enter your name :" ))
surname_length = len(input(" enter your surname :"))

if name_length == 0:
    print ("enter a name")

elif surname_length == 0:
    print("enter a surname ")
        
elif name_length + surname_length == 0:
    print ("you have't enter anything. pleas enter your name ")
        
elif name_length + surname_length < 4:
    print ("you have enterd less than 4 characters. Pleas make sure that you have entered your name and surname")

elif name_length + surname_length > 25:
    print("you have enterd more than 25 characters.pleas make sure that you have only your full name")
        
else :
    print("thank you for entering your name")




''' note i do use a note book for my Pseudi Code and i have only used the 
reading material that whas provided by Hyperion Dev'''