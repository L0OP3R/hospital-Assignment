import sqlite3
new_connection = sqlite3.connect("Hospital.db")

new_connection.execute(''' CREATE TABLE DOCTORS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        DOCTOR_NAME TEXT,
                        EMAIL_ID TEXT,
                        QUALIFICATION TEXT,
                        ADDRESS TEXT,
                        PHONE_NUMBER INTEGER)
                        ; ''')


getName = input("Enter the name of the Doctor: ")
getEmail = input("Enter the email-id: ")
getQualification = input("Enter the Designation or Qualification of the doctor: ")
getAddress = input("Enter the address of the Doctor: ")
getPhoneNumber = input("Enter the phone number of the DOCTOR: ")


new_connection.execute("INSERT INTO DOCTORS(DOCTOR_NAME,EMAIL_ID,QUALIFICATION,ADDRESS,PHONE_NUMBER)\
 VALUES ('"+getName+"','"+getEmail+"','"+getQualification+"','"+getAddress+"',"+getPhoneNumber+")")
new_connection.commit()
new_connection.close()
print("completed")