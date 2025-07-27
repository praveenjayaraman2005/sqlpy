import mysql.connector;

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pubg20114465@",
    database="project_db"
)
cursor=conn.cursor()

def add_employee():
    id=int(input("Enter a id: "))
    name=input("Enter a name: ")
    age=int(input("Enter a age: "))
    department=input("Enter a department: ")
    cursor.execute("INSERT INTO employee(id,name,age,department) VALUES (%s,%s,%s,%s)",(id,name,age,department))
    conn.commit()
    print("Employee Added")

def view_employees():
    cursor.execute("SELECT * FROM employee")
    rows=cursor.fetchall()
    for row in rows:
        print(f"ID:{row[0]} Name:{row[1]} Age:{row[2]} DEPT:{row[3]}")
def update_employee():
    id = int(input("Enter employee ID to update: "))
    name = input("New name: ")
    age = int(input("New age: "))
    dept = input("New department: ")
    cursor.execute("UPDATE employee SET name=%s, age=%s, department=%s WHERE id=%s", (name, age, dept, id))
    conn.commit()
    print("🔁 Updated.")
def delete_employee():
    id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM employee WHERE id=%s", (id,))
    conn.commit()
    print("❌ Deleted.")



while True:
    print("\n1. Add\n2. View\n3. Update\n4. Delete\n5. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        break
    else:
        print("❗ Invalid choice.")
conn.close()