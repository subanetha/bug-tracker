import sqlite3

def create_bug(title, description):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO bugs (title, description, status) VALUES (?, ?, ?)', (title, description, 'Open'))

    conn.commit()
    conn.close()

def list_bugs():
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bugs')
    bugs = cursor.fetchall()

    for bug in bugs:
        print(f'ID: {bug[0]}, Title: {bug[1]}, Status: {bug[3]}')

    conn.close()

def main():
    while True:
        print("\nBug Tracking System Menu:")
        print("1. Create a bug report")
        print("2. List all bug reports")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the bug title: ")
            description = input("Enter the bug description: ")
            create_bug(title, description)
        elif choice == '2':
            list_bugs()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()