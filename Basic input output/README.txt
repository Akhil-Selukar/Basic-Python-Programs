#Basic input output

This program demonstrate basic input and output functinality in python with some important concepts like functions, function with parameters and basic input validation

After executing this code it will initially display the a list with values [1,2,3] and ask user for the index position at which user want to update the value.
Once the valid index i.e. 0, 1 or 2 is entered it will ask for value which user want to put at that index.
After the value is entered updated list will be displayed and user will be asked if he/she want to update again or not.
If user enter Y, same loop will execute again and if user enter N program will stop with THANK YOU message

below are the functions defined in the code:

1. disp(my_list):
    This funtion is used to display list value. It takes a parameter my_list and display it in output

2. get_index():
    This function ask user for index value at which user want to perfiorm update.
    The acceptable values are 0, 1 or 2. If user enter other that these values it shoes message 'Please enter value between 0 to 2' and ask user for index again.
    If user enter any string or char value then it will show message 'Please enter valid index' and ask user for index again.
    Finally it return the valid index position value.

3. get_value(index):
    It is a simple function to get the value which need to be updated at the given index.
    
4. update_list(index,value):
    This function take index value and value that need to be updated at that index and perforn the list manipulation.
    It returns the updated list at the end.
  
5. play_again():
    This function ask user if he/she want to update the list any further or not.
    Depending on user input it returns Y or N.
    
