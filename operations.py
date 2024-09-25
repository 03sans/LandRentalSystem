# Import necessary modules and functions from other files
from read import*
from write import*
from datetime import datetime

# Function to rent land
def rentLand():
    # Get customer name and phone number
    cName = input("Enter your name here:").title()
    cNum = input("Enter your phone number here:")
    # Generate a unique ID based on phone number and timestamp
    uniqueId = str(cNum) + str(int(datetime.now().timestamp()))
    rented = {}  # Dictionary to store rented lands
    isRenting = True  # Variable to control renting loop
    while isRenting == True:
        # Display available lands
        print()
        print("Below are the lands in our directory. HAPPY RENTING!")
        print()
        showLands()
        # Get kitta number and validate it
        kNum = str(isValid())
        # Get number of months for renting
        months = isValidMonths()
        landlist = readFile('data.txt')  # Read land data from file
        # Update land status and add to rented dictionary
        for item in landlist:
            if item[0] == kNum:
                rented[landlist.index(item)] = months
                item[5] = 'Not Available'
        updateFile(landlist)  # Update file with new land status
        # Check if the user wants to rent more land
        pick = input("Do you want to rent more land from us? (y/n)").lower()
        if pick == 'n':
            isRenting = False  # Stop renting loop
    writeInvoice(landlist, cName, cNum, months, kNum, rented, uniqueId)  # Write rent invoice

# Function to validate kitta number for renting
def isValid():
    try:
        kNum = int(input("Enter the kitta number of the land you wish to rent:"))
        valid = False
        landlist = readFile('data.txt')  # Read land data from file
        # Check if the entered kitta number is valid and available for rent
        for item in landlist:
            if kNum == int(item[0]):
                if item[5] == 'Available':
                    valid = True
                else:
                    print('This land is unavailable! Choose a different kitta number')
                    return isValid()
        # If kitta number is not valid, prompt the user to enter again
        if valid == False:
            print('There is no such kitta number in the list, please enter a valid number')
            return isValid()
    except:
        displayError()  # Display error message if input is not valid
        showLands()  # Show available lands
        return isValid()
    if valid:
        return kNum

# Function to display error message for invalid inputs
def displayError():
    print('Enter a valid kitta number')

# Function to validate number of months for renting
def isValidMonths():
    try:
        months = int(input("Enter the number of months you will be renting this land:"))
    except:
        showLands()
        print('Invalid Value! Enter months in number')  
        return isValidMonths()
    return months

# Function to return land
def returnLand():
    # Get customer name and phone number
    cName = input("Enter your name here:").title()
    cNum = input("Enter your phone number here:")
    # Generate a unique ID based on phone number and timestamp
    uniqueId = str(cNum) + str(int(datetime.now().timestamp()))
    returned = {}  # Dictionary to store returned lands
    isReturning = True  # Variable to control returning loop
    while isReturning:
        # Display available lands
        print()
        print("Below are the lands in our directory. HAPPY RETURNING!")
        print()
        showLands()
        # Get kitta number and validate it
        kNum = str(isReturnValid())
        # Get number of months for returning
        months = isValidRMonths()
        rMonths = returnMonths()  # Get number of months after returning
        landlist = readFile('data.txt')  # Read land data from file
        # Update land status and add to returned dictionary
        for item in landlist:
            if item[0] == kNum:
                returned[landlist.index(item)] = months
                item[5] = 'Available'
        updateFile(landlist)  # Update file with new land status
        # Check if the user wants to return more land
        pick = input("Do you want to return more land? (y/n)").lower()
        if pick == 'n':
            isReturning = False  # Stop returning loop
    writeReturnInvoice(landlist, cName, cNum, months, kNum, returned, uniqueId, rMonths)  # Write return invoice

# Function to validate kitta number for returning
def isReturnValid():
    try:
        kNum = int(input("Enter the kitta number of the land you wish to return:"))
        valid = False
        landlist = readFile('data.txt')  # Read land data from file
        # Check if the entered kitta number is valid and not available for rent
        for item in landlist:
            if kNum == int(item[0]):
                if item[5] == 'Not Available':
                    valid = True
                else:
                    print('This land is for renting! Choose a different kitta number')
                    return isReturnValid()
        # If kitta number is not valid, prompt the user to enter again
        if valid == False:
            print('There is no such kitta number in the list, please enter a valid number')
            return isReturnValid()
    except:
        displayError()  # Display error message if input is not valid
        showLands()  # Show available lands
        return isReturnValid()
    if valid:
        return kNum

# Function to validate number of months for returning
def isValidRMonths():
    try:
        months = int(input("Enter the number of months you initially rented this land for:"))
    except:
        showLands()
        print('Invalid Value! Enter months in number')  
        return isValidRMonths()
    return months

# Function to validate number of months after returning
def returnMonths():
    try:
        rMonths = int(input("Enter the number of months you're returning after:"))
    except:
        showLands()
        print('Invalid Value! Enter months in number')  
        return returnMonths()
    return rMonths
