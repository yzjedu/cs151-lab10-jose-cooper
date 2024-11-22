#Programmers: Jose and Cooper
#Course: CS 151 Dr. Zee
#Problem: Analyze data on movies, their budgets, and their profits

# Purpose: Verify that a file exists then read data from that file into a table
# Parameters: None
# Return: None
def read_file():
    file_found = False
    file_name = "movies.csv"
    while file_found != True:
        file_name = input("Enter the input file name: ")
        try:
            with open(file_name, 'r') as file:
                table = [line.strip().split(',') for line in file]
                file_found = True
                return table
        except FileNotFoundError:
            print("File not found. Please try again.")

# Purpose: Calculate the movie's profit and add it to the table
# Parameters: Table
# Return: None
def add_profit(table):
    for row in table:
        try:
            budget = int(row[2])
            worldwide_gross = int(row[4])
            profit = worldwide_gross - budget
            row.append(str(profit))
        except ValueError:
            print(f"Skipping row due to invalid data: {row}")

# Purpose: Write the table's data to the file
# Parameters: Output file name, table
# Return: None
def write_to_file(output_file_name, table):
    with open(output_file_name, 'w') as file:
        for row in table:
            file.write(','.join(row) + '\n')

# Purpose: Run the program
# Parameters: None
# Return: None
def main():
    print("Welcome! This program processes movie data to calculate and add profits.")
    table = read_file()
    add_profit(table)
    output_file_name = input("Enter the output file name: ")
    write_to_file(output_file_name, table)
    print(f"Processing complete. Data with profit added has been written to {output_file_name}.")

if __name__ == "__main__":
    main()
