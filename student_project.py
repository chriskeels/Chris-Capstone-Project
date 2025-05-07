"""
Data Structures
Student Project
Project Title:
"""
##-- Libraries --##
import requests
import random
##-- Main --##
# get api url
URL = "https://randomuser.me"
path = "/api/"

# assign a list for the volunteers
volunteers = [] 
# get 9 volunteers to do chores
for i in range(9):

    response = requests.get(URL + path)
    
    body = response.json()
    
    if "results" in body and len(body["results"]) > 0:
        first_name = body["results"][0]["name"]["first"]
        last_name = body["results"][0]["name"]["last"]
        name = first_name + " " + last_name
        name = name.replace("'", "")

        volunteers.append(name) 

print("These are the volunteers:")
for volunteer in volunteers:
    print(volunteer)
    
    import random
chores = ["Wash the Dishes", "Take out the trash", "Vacuum the house", 
          "Mop the floor", "Do the laundry", "Sweep the porch", 
          "Clean the bathroom", "Water the plants", "Organize the pantry"]
first_chores = []
second_chores = []
third_chores = []
all_chores = first_chores + second_chores + third_chores
print(len(all_chores))
# Opening Lines 
print("Hello, Welcome to the Chore Tracker")
print("This week we need 3 people to do chores. They will be picked randomly.\n ")
# Show user the available options
print("These are the people who could get assigned chores:", volunteers, "\n ")
input("Press enter to randomize the cleaners and their chores \n ")
print(" ")
# Randomize both of the lists
random.shuffle(chores)


# Choose who will do chores

while True:
    print("These are the three people who will do chores: \n ")
    cleaner1 = random.choice(volunteers)
    print(cleaner1)
    print(" ")
            
    cleaner2 = random.choice(volunteers)
    print(cleaner2)
    print(" ")
            
    cleaner3 = random.choice(volunteers)
    print(cleaner3)
    print(" ")
            
    chosen_people = cleaner1, cleaner2, cleaner3
    # check if there are any duplicate cleaners
    if cleaner1 == cleaner2 or cleaner2 == cleaner3 or cleaner1 == cleaner3:
        print("Sorry we got duplicates in our selection...\n Let's try again!!")
        print(" ")
            
        continue
    # remove the people that have already been chosen
    for i in chosen_people:
        volunteers.remove(i)
    break
## Slice list to divide 3 groups of 3 chores eaach 
first_chores = chores[::3]
second_chores = chores[1::3]
third_chores = chores[2::3]
    
# # Assign the people their chores 
print(cleaner1 + ":", len(all_chores), "chores assigned")
print(cleaner2 +":", len(all_chores), "chores assigned")
print(cleaner3 + ":", len(all_chores), "chores assigned\n ")
    
# # assign the 3 chores to person
input("Press Enter to Assign the people chores.")
print("Assigning chores...\n ")
print(cleaner1 + ":", len(first_chores), "chores assigned")
print(", ".join(first_chores).capitalize())
print(" ")
    
print(cleaner2 +":", len(second_chores), "chores assigned")
print(", ".join(second_chores).capitalize())
print(" ")
    
print(cleaner3 + ":", len(third_chores), "chores assigned")
print(", ".join(third_chores).capitalize())
print(" ")