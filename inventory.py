
#=================================The beginning of the class============================
class Shoe:

    def __init__(self, country: str, code: str, product: str, cost: str, quantity: str):
        
        # Initialise the instance attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country
    
    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self.country} {self.code} {self.product} {self.cost} {self.quantity})"

#=====================================Shoe list=====================================
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#=====================================Functions outside the class=================================
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    shoe_list = []
    while True:
    
        # Implement try-except for error handling
        try:
            file = open("inventory.txt", "r")

            for lines in file:
                temp = lines.strip()
                temp = temp.split(",")

                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

            # Skip the first the first line using list comprehension        
            shoe_list = [shoe_list[i] for i in range(1,len(shoe_list))]

        except FileNotFoundError as error:
            print("Sorry! This file does not exist.")
            print(error)

        except Exception as error:
            print("Sorry! Something else went wrong.")
            print(error)

        else:
            return shoe_list

        finally:
            file.close()
            print("The inventory file is read and closed!\n")    

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Generate lists of each of the attributes via list comprehesion
    code_list = [shoe_list[i].code for i in range(len(shoe_list))]
    country_list = [shoe_list[i].country for i in range(len(shoe_list))]
    product_list  = [shoe_list[i].product for i in range(len(shoe_list))]

    # Input for the country attribute
    shoe_country = input("Enter the unique shoe country: ").title()
    # Country must be a unique input variable
    while shoe_country in country_list:
        shoe_country = input("Enter the unique shoe country the above exists: ").title()
    print("")

    # Input for the code attribute
    shoe_code = input("Emter the unique shoe code: ").upper()
    # Code must be a unique input variable
    while shoe_code in code_list:
        shoe_code = input("Emter the unique shoe code the above exists: ").upper()
    print("")

    # Input for the product attribute
    shoe_product = input("Enter the unique shoe product name: ").title()
    # Product must be a unique input variable
    while shoe_product in product_list:
        shoe_product = input("Enter the unique shoe product name the above exists: ").title()
    print("")

    # The class accepts the cost amount as a string
    shoe_cost = input("Enter the product cost amount: ")
    while int(shoe_cost) < 0:
        shoe_cost = input("Invalid input! Enter positive product cost amount: ")    
    print("")

    # The class accepts the quantity amount as a string
    shoe_quantity = input("Enter the product quantity amount: ")
    while int(shoe_quantity) < 0:
        shoe_quantity = input("Invalid input! Enter positive quantity amount: ")
    print("")

    # Create the shoe object
    shoe_obj = Shoe(
                country=shoe_country, 
                code=shoe_code, 
                product=shoe_product, 
                cost=shoe_cost, 
                quantity=shoe_quantity,
            )

    # Append this object inside the shoe list and display updated shoe list
    shoe_list.append(shoe_obj)

    return shoe_list


def view_all():
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for idx in range(0, len(shoe_list)):
        print(f"Shoe object: {idx} is {shoe_list[idx]}")


def re_stock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Generate list of the quantity via list comprehesions
    quantity_list = [int(shoe_list[i].quantity) for i in range(len(shoe_list))]

    # Find the minimum/lowest quantity in the quantity list
    min_quantity = min(quantity_list)

    # Find positions/indexes of the lowest quantity (min_quantity)
    min_list = []
    for quant in quantity_list:
        if quant == min_quantity:
            min_list.append(quantity_list.index(quant))
        elif quant != min_quantity:
            pass

    # Display the objects in shoe_list with the lowest quantity
    # Enable user to update the quntity
    for indx in min_list:
        print(f"{shoe_list[indx]} has the lowest quantity")
        update_quantity = int(input('''Enter one of the options:
        1. for update preference
        0. for non-update preference
                                         
        Enter selection:  '''))
        print("")

        if update_quantity == 0:
            # Display the object quantity won't be updated
            print(f"{shoe_list[indx]} quantity won't be updated!")
            
        elif update_quantity == 1:
            # Enable user to update the quantity value in the shoe object
            shoe_list[indx].quantity = input("Enter the updated quantity: ")
            print(f"The quantity is updated to {shoe_list[indx].quantity}")
            print(f"The corresponding updated object: {shoe_list[indx]}")   


def search_shoe():
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Generate list of the code attrubutes via list comprehesion
    code_list = [shoe_list[i].code for i in range(len(shoe_list))]
    
    # Request the user to enter the unique code
    shoe_code = input("Enter shoe code for search: ").upper()

    # Assume that the code input already exists
    while shoe_code not in code_list:
        shoe_code = input("Enter shoe code that exists: ").upper()

    # Find position/index of the shoe_code in the code_list,
    # and return/display the corresponding shoe oobject
    indx = code_list.index(shoe_code)
    print(f"The corresponding shoe object: {shoe_list[indx]}")


def value_per_item():
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Calculate the total value for each object in the shoe_list
    for i in range(len(shoe_list)):
        print(f"{shoe_list[i]} value: ${int(shoe_list[i].cost) * int(shoe_list[i].quantity)}")


def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Generate list of the quantity via list comprehesions
    quantity_list = [int(shoe_list[i].quantity) for i in range(len(shoe_list))]

    # Find the maximum/highest quantity in the quantity list
    max_quantity = max(quantity_list)

    # Find positions/indexes of the highest quantity (max_quantity)
    max_list = []
    for quant in quantity_list:
        if quant == max_quantity:
            max_list.append(quantity_list.index(quant))
        elif quant != max_quantity:
            pass

    # Display the objects in shoe_list with the highest quantity
    # Enable user to update the quntity
    for indx in max_list:
        print(f"Object: {shoe_list[indx]} has the highest quantity")
        print(f"Product: {shoe_list[indx].product} is for sale!")


#==============================Main Menu===============================
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read shoes data
    2. View all the shoes
    3. Re stock lowest quantity
    4. Search using shoe code
    5. View the value per item
    6. View for sale products
    7. Capture new shoes                                                                                                                     
    8. Quit application

    Enter selection: '''))
    print("")
       
    if user_choice == 1:
        #pass
        # Call the read_shoes_data() function
        shoe_list = read_shoes_data()
        print(shoe_list)
        print("")
        
    elif user_choice == 2:
        #pass
        # Call the view_all() function
        view_all()
        print("")

    elif user_choice == 3:
        #pass
        # Call the re_stock() function
        re_stock()
        print("")

    elif user_choice == 4:
        #pass
        # Call the search_shoe() function
        search_shoe()
        print("")    

    elif user_choice == 5:
        #pass
        # Call the value_per_item() function
        value_per_item()
        print("")    

    elif user_choice == 6:
        #pass
        # Call the highest_qty() function
        highest_qty()
        print("")    

    elif user_choice == 7:
        #pass
        # Call the capture_shoes() function
        shoe_list = capture_shoes()
        print("The updated shoe list:\n")
        print(shoe_list)
        print("")

    elif user_choice == 8:
        print("Thanks for using the App! Goodbye!!!\n")
        exit()

    else:
        print("Oops - incorrect input!\n")
        continue
       