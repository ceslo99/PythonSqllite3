import sqlite3

conn = sqlite3.connect('local.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
         (CLASS_ACCOUNT INT  NOT NULL,
         LAST_NAME           TEXT    NOT NULL,
         FIRST_NAME            TEXT     NOT NULL);''')
print ("Table created successfully");

conn.execute("INSERT INTO STUDENTS (CLASS_ACCOUNT,LAST_NAME,FIRST_NAME) \
      VALUES (821807604, 'Lopez', 'Cesar' )");

conn.execute("INSERT INTO STUDENTS (CLASS_ACCOUNT,LAST_NAME,FIRST_NAME) \
      VALUES (2, 'Allen', 'smith' )");


conn.commit()
print ("Records created successfully");

cursor = conn.execute("SELECT class_account, last_name, first_name from STUDENTS")
for row in cursor:
   print ("CLASS_ACCOUNT = ", row[0])
   print ("LAST_NAME = ", row[1])
   print ("FIRST_NAME = ", row[2], "\n")

print ("Operation done successfully");

conn.close()
