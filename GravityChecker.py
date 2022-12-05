print("What would you weigh in these various planets?\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
#These are the various gravity levels. 
Venus = .91
Mars = .31
Jupiter = 2.34
Saturn = 1.06
Uranus = .92
Neptune = 1.19

#These are the inputs. 

print("First type in your weight") 
weight = input()
user_input = input("What planet would you like to look at? (type a number)")
#print (type(weight))

#These are the 7 different outputs. 
if user_input == "1":
  overall_weight = int(weight) * Venus
elif user_input == "2":
  overall_weight = int(weight) * Mars
elif user_input == "3":
  overall_weight = int(weight) * Jupiter
elif user_input == "4":
  overall_weight = int(weight) * Saturn
elif user_input == "5":
  overall_weight = int(weight) * Uranus
elif user_input == "6":
  overall_weight = int(weight) * Neptune
else: print("You haven't correctly chosen a planet number. Try again.")  

print(overall_weight)

