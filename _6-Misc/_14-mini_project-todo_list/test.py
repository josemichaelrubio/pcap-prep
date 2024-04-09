import csv

# Function to get the last ID from the CSV file
def get_last_id(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            # Read the CSV file and get the last row
            return int(list(csv.reader(csvfile))[-1][0])
    except (IOError, IndexError):
        # If the file doesn't exist or is empty, start with ID 0
        return 0

# Function to add a new entry with a unique ID
def add_entry_with_unique_id(filename, entry_data):
    # Get the last used ID and increment it
    last_id = get_last_id(filename)
    new_id = last_id + 1
    # Open the file in append mode, or create it if it doesn't exist
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the new entry with the unique ID
        writer.writerow([new_id] + entry_data)

# Your data to add (without the ID)
data_to_add = ['data1', 'data2', 'data3']

# Filepath for your CSV file
csv_file = 'tasks.csv'

# Add a new entry to the CSV file
add_entry_with_unique_id(csv_file, data_to_add)