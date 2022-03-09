import sqlite3
conn = sqlite3.connect("Hospital.db")
getPhoneNumber = input("ENter the phone number of the doctor that is to be deleted: ")
conn.execute("DELETE FROM DOCTORS WHERE PHONE_NUMBER="+getPhoneNumber+"")
conn.commit()
print("Deleted succesfully")
result  = conn.execute("SELECT * FROM DOCTORS")
print("UPDATED RECORD")
for i in result:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])