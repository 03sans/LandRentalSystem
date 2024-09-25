# Function to read data from a file and store it in a list of lists
def readFile(name):
    lands = []  # Initialize an empty list to store land data
    try: 
        with open(name, 'r') as file:  # Open the file in read mode
            for value in file:  # Iterate through each line in the file
                text = value.split(',')  # Split the line by comma to extract individual values
                # Extracting data and removing newline characters
                kitta = text[0].replace('\n', '')  # Extracting kitta number
                city = text[1].replace('\n', '')   # Extracting city
                direction = text[2].replace('\n', '')  # Extracting direction
                anna = text[3].replace('\n', '')  # Extracting anna
                price = text[4].replace('\n', '')  # Extracting price
                status = text[5].replace('\n', '')  # Extracting status
                data = [kitta, city, direction, anna, price, status]  # Creating a list of land data
                lands.append(data)  # Adding the land data to the list of lands
        return lands  # Returning the list of lands
    except FileNotFoundError:
        print("Invalid or absentee file")  # Handling file not found error
        return []  # Returning an empty list if file not found

# Function to display available lands
def showLands():
    landlist = readFile('data.txt')  # Reading land data from the file
    print("-"*81)
    print("|   Kitta   |     City    |   Direction  |   Anna  |   Price  |      Status     | ")
    print("-"*81)
    for items in landlist:  # Iterating through each land data in the list
        if 'Available' in items[5]:  # Checking if the land status is 'Available'
            # Printing land details with proper formatting
            print("|", items[0], " " * (8 - len(items[0])), "|", items[1], " " * (10 - len(items[1])), "|", items[2], " " * (11 - len(items[2])), "|", items[3], " " * (6 - len(items[3])), "|", items[4], " " * (7 - len(items[4])), "|", items[5], " " * (14 - len(items[5])), "|")
    print("-"*81)
