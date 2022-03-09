import sqlite3
connection1 = sqlite3.connect("Hospital.db")
result = connection1.execute("SELECT * FROM DOCTOR")
for i in result:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])