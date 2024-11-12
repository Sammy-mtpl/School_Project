# delete function
import csv
name=input("enter the name of the book ,which you want to delete")
 
def delete_row_from_csv(value_to_delete, column_name='bookName'):
    # Read all rows from the CSV file
    rows = []
    with open('main.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Keep rows that do not contain the value in the specified column
            if row[column_name] != value_to_delete.lower().replace(" ", ""):
                rows.append(row)
    
    # Write the filtered rows back to the CSV file
    with open('main.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        
            
delete_row_from_csv(name)