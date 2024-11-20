# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

Purpose: Read the data from a file to a table (class code)  
Name: read_file  
Parameters: File name  
Return: Table  
Algorithm:
1. Prompt the user to input the name of the file they want to read data from
2. Open the file with the intent to read
3. Read each line of the file into a table
4. Close the file

Purpose: Update the table by adding one element in each row to hold the profit  
Name: add_profit  
Parameters:   
Return:   
Algorithm:
1. For row in table:
   1. If an element is a number
      1. Convert the element to an integer
   2. Calculate the profit with the budget, domestic gross, and worldwide gross
   3. Append the profit to the row

Purpose: Write the new table onto an output file  
Name: write_to_file  
Parameters: File name  
Return:   
Algorithm:
1. Open a file for writing
2. Write each line from the table into the output file
3. Close the file

Purpose: Run the program  
Name: main
Parameters:   
Return:   
Algorithm:   
1. Output the purpose of the program
2. Call the read_file function
3. Call the add_profit function
4. Call the write_to_file function