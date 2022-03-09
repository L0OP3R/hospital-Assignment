import sqlite3

new_connection = sqlite3.connect("Hospital.db")

new_connection.execute(''' CREATE TABLE PATIENT (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        PATIENT_ID INTEGER,
                        PATIENT_NAME,
                        PATIENT_ADDRESS TEXT,
                        PATIENT_PHONENUMBER INTEGER,PATIENT_EMAIL TEXT,
                        PATIENT_PINCODE INTEGER
                        ); ''')
print("Both the tables has been created succesfully")


getId = input("Enter Id : ")
getName = input("Enter the name of the patient: ")
getAddress = input("Enter the address of the patient: ")
getPhoneNumber = input("Enter the phone number of the patient: ")
getEmail = input("Enter the email-id: ")
getPincode = input("Enter the pincode: ")

new_connection.execute("INSERT INTO PATIENT(PATIENT_ID,PATIENT_NAME,PATIENT_ADDRESS,PATIENT_PHONENUMBER,PATIENT_PINCODE)\
 VALUES ("+getId+",'"+getName+"','"+getAddress+"',"+getPhoneNumber+","+getPincode+")")

new_connection.commit()
new_connection.close()
print("Executed succesfull")


