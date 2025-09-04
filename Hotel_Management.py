import mysql.connector

# Database setup
def setup_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@1012",
        database="hotel_management"
    )
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rooms (
            room_id INT AUTO_INCREMENT PRIMARY KEY,
            room_type VARCHAR(255) NOT NULL,
            price FLOAT NOT NULL,
            is_available TINYINT DEFAULT 1
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(15) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            room_id INT,
            FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM Rooms')
    if cursor.fetchone()[0] == 0:
        rooms = [("Single", 100.0), ("Double", 150.0), ("Suite", 300.0)]
        cursor.executemany('INSERT INTO Rooms (room_type, price) VALUES (%s, %s)', rooms)

    connection.commit()
    cursor.close()
    connection.close()

def show_available_rooms():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@1012",
        database="hotel_management"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Rooms WHERE is_available = 1')
    rooms = cursor.fetchall()
    cursor.close()
    connection.close()

    if rooms:
        print("\nAvailable Rooms:")
        for room in rooms:
            print(f"ID: {room[0]}, Type: {room[1]}, Price: {room[2]}")
    else:
        print("\nNo rooms available!")

def book_room():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@1012",
        database="hotel_management"
    )
    cursor = connection.cursor()

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    show_available_rooms()
    room_id = int(input("Enter Room ID to book: "))

    cursor.execute('SELECT is_available FROM Rooms WHERE room_id = %s', (room_id,))
    room_status = cursor.fetchone()

    if room_status and room_status[0] == 1:
        cursor.execute('INSERT INTO Customers (name, phone, email, room_id) VALUES (%s, %s, %s, %s)', (name, phone, email, room_id))
        cursor.execute('UPDATE Rooms SET is_available = 0 WHERE room_id = %s', (room_id,))
        connection.commit()
        print("\nRoom booked successfully!!")
    else:
        print("\nRoom is not available!")

    cursor.close()
    connection.close()

def view_customers():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@1012",
        database="hotel_management"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Customers')
    customers = cursor.fetchall()
    cursor.close()
    connection.close()

    if customers:
        print("\nCustomers:")
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Email: {customer[3]}, Room ID: {customer[4]}")
    else:
        print("\nNo customers found!")

def checkout_room():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devansh@1012",
        database="hotel_management"
    )
    cursor = connection.cursor()

    customer_id = int(input("\nEnter Customer ID for checkout: "))

    cursor.execute('SELECT room_id FROM Customers WHERE customer_id = %s', (customer_id,))
    result = cursor.fetchone()

    if result:
        room_id = result[0]

        # Delete customer record and make the room available
        cursor.execute('DELETE FROM Customers WHERE customer_id = %s', (customer_id,))
        cursor.execute('UPDATE Rooms SET is_available = 1 WHERE room_id = %s', (room_id,))

        connection.commit()
        print("\nCheckout successful! Room is now available.")
    else:
        print("\nNo such customer found!")

    cursor.close()
    connection.close()

def main():
    setup_database()
    while True:
        print("\n1. Show Available Rooms")
        print("2. Book a Room")
        print("3. View Customers")
        print("4. Checkout a Room")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_available_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            view_customers()
        elif choice == '4':
            checkout_room()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

main()
