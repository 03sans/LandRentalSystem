# Importing necessary modules
import read  
from operations import *

# Function to display a welcome message to the user
def welcome():
    print("-"*125)
    print("\t\t\t\t\t\tTECHNO RENTAL PROPERTY")
    print("\n")
    print("\t\t\t\t\t\tAddress: Kamalpokhari")
    print("\t\t\t\t\t\tContact us at 9800000000")
    print("-"*125)
    print("\t\t\t\t\t\tWelcome to our system!")
    print("-"*125)

# Function to display the main menu options to the user
def menu():
    print("Please select an option!")
    print("i || Press 1 to rent")
    print("ii || Press 2 to return")
    print("iii || Press 3 to exit our system \n")

# Main function to run the rental management system
def main():
    # Displaying welcome message and main menu
    welcome()
    menu()
    
    # Loop to keep the program running until the user chooses to exit
    while True:
        # Asking the user for their choice of operation
        value = int(input("Enter your operation number here:"))
        print()
        
        # Performing actions based on user input
        if value == 1:
            # Renting process
            print("-"*125)
            print("\t\t\t\t Thank you for choosing to rent! Your renting process begins now.")
            print("-"*125)
            print()
            rentLand()  # Calling the function to handle the renting process
        elif value == 2:
            # Return process
            print("-"*125)
            print("\t\t\t\tThank you for choosing to return! Your return process begins now.")
            print("-"*125)
            print()
            returnLand()  # Calling the function to handle the return process
        elif value == 3:
            # Exiting the system
            print("-"*125)
            print("\t\t\t\tThank you for doing business with us! We hope to see you soon.")
            print("-"*125)
            break  # Exiting the loop and ending the program
        else:
            # Handling invalid input
            displayError()  
            print()

# Calling the main function to start the program
main()
