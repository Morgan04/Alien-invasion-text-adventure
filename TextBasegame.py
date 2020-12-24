# declaration
rooms = {
     'Hall of education': {'South': 'Stairway to English 101', 'North': 'Main school entrance', 'East': 'Gym', 'West': 'Library', 'Item': 'skateboard'},
     'Stairway to English 101': {'North': 'Hall of education', 'East': 'English 101', 'Item': 'Bell'},
     'English 101': {'West': 'Stairway to English 101', 'Item': 'Books'},
     'Gym': {'East': 'Hall of education', 'Item': 'Alien'}, # The Games villian is located here
     'Main school entrance': {'East': 'Chemistry 101', 'South': 'Hall of education', 'Item': 'wooden sword'},
     'Chemisty 101': {'West': 'Main school entrance', 'Item': 'laser gun'},
     'Library': {'West': 'Hall of education', 'North': 'Math 101', 'Item': 'cell phone'},
     'Math 101': {'South': 'Library', 'Item': 'pencils'}

}
state = 'Hall of education'
# function
def get_new_state(state, direction):
    new_state = state  # declaraing
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state=rooms[i][direction] #assigning new_state

    return new_state  # return
def get_item(state):
    return rooms[state]['Item'] #returning Item value
#function
def show_instructions():
    #print a main menu and the commands
    print("Alien invasion text game")
    print("Collect 6 items and meet up at the 'gym' to fight the alien and win the game")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
show_instructions() #calling function
inventory=[]
while (1):  # gameplay loop
    print('You are in ', state)  # printing state
    print('Inventory:',inventory) #printing inventory
    item=get_item(state) #calling get_item function
    print('You see a',item) #print
    if item=='Alien': #if
        print('Your friends have died...GAME OVER!')
        exit(0)
    direction = input('Enter your move: ')  # asking user
    if (direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South'):  # if
        direction=direction[3:]
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('The room has wall in that direction enter other direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    elif direction==str('get '+item): #if
        if item in inventory: #if item already present in inventory
            print('Item already taken go to another room!!')
        else:
            inventory.append(item) #appending
    else:
        print('Invalid direction!!')  # print
    if len(inventory)==6:
        print('Congratulations! You have collected all items and defeated the alien, your friends are saved thanks to your help!') #print
        exit(0)