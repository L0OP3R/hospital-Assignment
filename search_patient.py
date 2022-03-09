import sqlite3
conn = sqlite3.connect("Hospital.db")
getID = input("Enter the Patient id- ")
result = conn.execute("SELECT * FROM PATIENT WHERE ID="+getID+"")
print("PATIENT DETAILS")
for i in result:
    print("id-", i[0])
    print("Name-", i[1])
    print("Address-", i[2])
    print("Phone Number-", i[3])
    print("Email-", i[4])
    print("Pincode-", i[5])