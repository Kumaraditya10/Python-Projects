import os

# Function to create a new file 
def create_file(filename):
    try:
        # 'x' mode creates a new file and fails if it already exists
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        print(f"Error: File '{filename}' already exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to view all files in the current directory
def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found in the directory.")
    else:
        print("Files in directory:")
        for file in files:
            print(f"- {file}")

# Function to delete a specific file 
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting: {e}")

# Function to read the content of a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"--- Content of '{filename}' ---\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to edit/append data to a file 
def edit_file(filename):
    try:
        with open(filename, 'a') as f: # 'a' stands for append mode
            content = input("Enter the data you want to add: ")
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully!")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle the Menu and User Choice 
def main():
    while True:
        print("\n--- FILE MANAGEMENT APP ---")
        print("1: Create a File")
        print("2: View All Files")
        print("3: Delete a File")
        print("4: Read a File")
        print("5: Edit a File")
        print("6: Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the file name to create (e.g., sample.txt): ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("Closing the app... Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()