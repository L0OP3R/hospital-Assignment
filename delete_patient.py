import sqlite3

connection1 = sqlite3.connect('Hospital.db')

getID = input("Enter id of the patient to be deleted: ")
result = connection1.execute("DELETE FROM PATIENT WHERE ID ="+getID)
print("Pateint deleted succesfully ")