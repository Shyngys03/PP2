import psycopg2

# connecting to database
conn = psycopg2.connect(
    host= "localhost",
    database= "TSIS",
    user= "postgres",
    password= "sh20030213"
)


# Create table
def create_table():
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE tsis_pp2 (
            name VARCHAR NOT NULL,
            id VARCHAR(9),
            points NUMERIC,
            submit_date VARCHAR(10)
        )
    """)
    cur.close()
    conn.commit()



# Insert data
def insert_data():
    cur = conn.cursor()

    name = input("Name: ")
    id = input("ID: ")
    point = float(input("Points: "))
    date = input("Submitted date: ")
    cur.execute("INSERT INTO tsis_pp2 (name, id, points, submit_date) VALUES (%s, %s, %s, %s)", (name, id, point, date))
    conn.commit()



# Update data
def update_data():
    cur = conn.cursor()

    
    cur.execute("""UPDATE tsis_pp2
                    SET points = 14
                    WHERE name = 'Shyngys'
        """)
    conn.commit()



# Query data
def query_data():
    cur = conn.cursor()

    cur.execute("SELECT name, id, submit_date FROM tsis_pp2 ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    


# Delete data
def delete_data():
    cur = conn.cursor()

    Name = input("Enter which do you to delete: ")
    cur.execute("DELETE FROM tsis_pp2 WHERE name = %s", (Name,))
    conn.commit()



def menu():
    print()
    print("         Choose the option: ")
    print("         1. Create table")
    print("         2. Insert data")
    print("         3. Update data")
    print("         4. Query data")
    print("         5. Delete data")
    print("         6. Exit")
    choose = int(input())
    if choose == 1:
        create_table()
        menu()
    elif choose == 2:
        insert_data()
        menu()
    elif choose == 3:
        update_data()
        menu()
    elif choose == 4:
        query_data()
        menu()
    elif choose == 5:
        delete_data()
        menu()
    elif choose == 6:
        exit()

menu()