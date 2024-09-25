#Importing necessary modules
from datetime import date
from read import*
from datetime import datetime

# Function to write a rent invoice
def writeInvoice(landlist, cName, cNum, months, kNum, rented, uniqueId):
    totalPrice = 0  # Initialize total price variable
    file = open("./Rent Invoices/" + cName + "-" + "Rent" + "-" + uniqueId + ".txt", "w")  # Open a file in write mode to write the invoice
    
    # Print header and customer details
    print("-" * 120)
    print(f"| Rent Invoice({cName}):\n")
    print("-" * 120)
    print(f'\t\t\t\t\t Customer Name: {cName}\n')
    print(f'\t\t\t\t\t Phone Number: {cNum}\n')
    print(f'\t\t\t\t\t Date and Time: {datetime.now()} \n')
    print("-"*120)
    print("| Kitta Number  | City       | Direction   | Anna   |  Duration        | Price   |")
    print("-" * 120)
    
    # Loop through rented items and print details
    for rentItem, months_rented in rented.items():
        singleLandPrice = int(landlist[rentItem][4]) * rented[rentItem]
        print(f"| {landlist[rentItem][0]} {' ' * (12 - len(landlist[rentItem][0]))} | {landlist[rentItem][1]} {' ' * (9 - len(landlist[rentItem][1]))} | {landlist[rentItem][2]} {' ' * (10 - len(landlist[rentItem][2]))} | {landlist[rentItem][3]} {' ' * (5 - len(landlist[rentItem][3]))} | {months_rented} months {' ' * (8 - len(str(months_rented)))} | {singleLandPrice} {' ' * (6 - len(str(singleLandPrice)))} |")
        totalPrice += singleLandPrice
    
    # Print total price
    print("-" * 120)
    print(f"| Total Price: {totalPrice}\n")
    print("-"*120)
    print()

    # Write invoice details to the file
    file.write("-" * 120 + "\n")
    file.write(f"| Rent Invoice({cName}):\n")
    file.write("-" * 120 + "\n")
    file.write(f'\t\t\t\t\t Customer Name: {cName}\n')
    file.write(f'\t\t\t\t\t Phone Number: {cNum}\n')
    file.write(f'\t\t\t\t\t Date and Time: {datetime.now()} \n')
    file.write("-"*120 + "\n")
    file.write("| Kitta Number  | City       | Direction   | Anna   |  Duration        | Price   |\n")
    file.write("-" * 120 + "\n")
    
    # Loop through rented items and write details to the file
    for rentItem, months_rented in rented.items():
        singleLandPrice = int(landlist[rentItem][4]) * rented[rentItem]
        file.write(f"| {landlist[rentItem][0]} {' ' * (12 - len(landlist[rentItem][0]))} | {landlist[rentItem][1]} {' ' * (9 - len(landlist[rentItem][1]))} | {landlist[rentItem][2]} {' ' * (10 - len(landlist[rentItem][2]))} | {landlist[rentItem][3]} {' ' * (5 - len(landlist[rentItem][3]))} | {months_rented} months {' ' * (8 - len(str(months_rented)))} | {singleLandPrice} {' ' * (6 - len(str(singleLandPrice)))} |\n")
    
    # Write total price to the file
    file.write("-" * 120 + "\n")
    file.write(f"| Total Price: {totalPrice}\n")
    file.write("-"*120 + "\n")

    file.close()  # Close the file

# Function to write a return invoice
def writeReturnInvoice(landlist, cName, cNum, months, kNum, returned, uniqueId, rMonths):
    totalPrice = 0  # Initialize total price variable
    totalFine = 0  # Initialize total fine variable
    fine = 0  # Initialize fine variable
    file = open("./Return Invoices/" + cName + "-" + "Return" + "-" + uniqueId + ".txt", "w")  # Open a file in write mode to write the invoice
    
    # Print header and customer details
    print("-" * 120)
    print(f"| Return Invoice({cName}):\n")
    print("-" * 120)
    print(f'\t\t\t\t\t Customer Name: {cName}\n')
    print(f'\t\t\t\t\t Phone Number: {cNum}\n')
    print(f'\t\t\t\t\t Date and Time: {datetime.now()} \n')
    print("-"*120)
    print("| Kitta Number  | City       | Direction   | Anna   | Duration         | Returned in      | Price   |\n")
    print("-" * 120)
    
    # Loop through returned items and calculate total price and fine
    for returnItem, months_returned in returned.items():
        singleLandPrice = int(landlist[returnItem][4]) * returned[returnItem]
        if rMonths > months:
            extra_months = rMonths - months
            fine = (extra_months) * (0.1 * int(landlist[returnItem][4]))  # Calculate fine for extra months
            totalFine += fine  # Add fine to total fine
        totalPrice += singleLandPrice  # Add land price to total price
        grand = totalPrice + totalFine  # Calculate grand total
        
        # Print land details with proper formatting
        print(f"| {landlist[returnItem][0]} {' ' * (12 - len(landlist[returnItem][0]))} | {landlist[returnItem][1]} {' ' * (9 - len(landlist[returnItem][1]))} | {landlist[returnItem][2]} {' ' * (10 - len(landlist[returnItem][2]))} | {landlist[returnItem][3]} {' ' * (5 - len(landlist[returnItem][3]))} | {months} months {' ' * (8 - len(str(months)))} | {rMonths} months {' ' * (8 - len(str(rMonths)))} | {singleLandPrice} {' ' * (6 - len(str(singleLandPrice)))} |")
        
    # Print total price, total fine, and grand total
    print("-" * 120)
    print(f"| Total Price: {totalPrice}\n")
    print(f"| Total Fine: {totalFine}")
    print(f"| Grand Total: {grand}")
    print("-"*120)

    # Write header and customer details to the file
    file.write("-" * 120 + "\n")
    file.write(f"| Return Invoice({cName}):\n")
    file.write("-" * 120 + "\n")
    file.write(f'\t\t\t\t\t Customer Name: {cName}\n')
    file.write(f'\t\t\t\t\t Phone Number: {cNum}\n')
    file.write(f'\t\t\t\t\t Date and Time: {datetime.now()} \n')
    file.write("-" * 120 + "\n")
    file.write("| Kitta Number  | City       | Direction   | Anna   | Duration         | Returned in      | Price   |\n")
    file.write("-" * 120 + "\n")
    
    # Loop through returned items and write details to the file
    for returnItem, months_returned in returned.items():
        singleLandPrice = int(landlist[returnItem][4]) * returned[returnItem]
        if rMonths > months:
            extra_months = rMonths - months
            fine = (extra_months) * (0.1 * int(landlist[returnItem][4]))  # Calculate fine for extra months
            totalFine += fine  # Add fine to total fine
        totalPrice += singleLandPrice  # Add land price to total price
        grand = totalPrice + totalFine  # Calculate grand total
        
        # Write land details to the file
        file.write(f"| {landlist[returnItem][0]} {' ' * (12 - len(landlist[returnItem][0]))} | {landlist[returnItem][1]} {' ' * (9 - len(landlist[returnItem][1]))} | {landlist[returnItem][2]} {' ' * (10 - len(landlist[returnItem][2]))} | {landlist[returnItem][3]} {' ' * (5 - len(landlist[returnItem][3]))} | {months} months {' ' * (8 - len(str(months)))} | {rMonths} months {' ' * (8 - len(str(rMonths)))} | {singleLandPrice} {' ' * (6 - len(str(singleLandPrice)))} |\n")
    
    # Write total price, total fine, and grand total to the file
    file.write("-" * 120 + "\n")
    file.write(f"| Total Price: {totalPrice}\n")
    file.write(f"|Total Fine: {totalFine}\n")
    file.write(f"| Grand Total: {grand}\n")
    file.write("-"*120 + "\n")
    
    file.close()  # Close the file

# Function to update the data file with the new status of lands
def updateFile(landlist):
    file = open("data.txt", "w")  # Open the data file in write mode
    file.truncate()  # Clear the existing content of the file
    # Loop through landlist and write each land's data to the file
    for item in landlist:
        file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]}\n")
    file.close()  # Close the file
