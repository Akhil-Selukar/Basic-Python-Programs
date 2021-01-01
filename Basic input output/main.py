#DISPLAY CURRENT VALUE OF LIST
def disp(my_list):
    print('Current value of list is {}'.format(my_list))

#ASK FOR INDEX FROM USER
def get_index():
    index = 'dummy'
    acceptable_index = [0,1,2]
    while index not in acceptable_index:
        index = input('Enter index you want to update (0,1,2) : ')

        if index.isdigit() == False:
            print('Please enter valid index')
        elif index not in ['0','1','2']:
            print('Please enter value between 0 to 2')
        else:
            return int(index)

#ASK FOR VALUE NEED TO BE INSERTED AT GIVEN INDEX
def get_value(index):
    value = input('Enyter value to inset in list at index {} : '.format(index))
    return value

#UPDATE THE LIST
def update_list(index,value):
    my_list[index] = value
    return my_list

#PLAY AGAIN?
def play_again():
    choice = 'dummy'
    acceptable_values = ['Y','N']

    while choice not in acceptable_values:
        choice = input('Want to update list again? [Y/N] : ')
        if choice in acceptable_values:
            return choice
        else:
            print('Please enter valid choice i.e. Y or N')

#LOGIC i.e. FUNCTION CALLING
my_list = [1,2,3]
print('Initial value of list is : {}'.format(my_list))

game_on = 'Y'
while game_on == 'Y':
    index = get_index()
    value = get_value(index)
    update_list(index,value)
    disp(my_list)
    game_on = play_again()

print('THANK YOU!!')
