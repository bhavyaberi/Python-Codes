# Setup db connection
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost", user="root", password="123456789", database="bhavya_db"
)
db_cursor = db_connection.cursor()

# # Delete all tables
# db_cursor.execute('show tables')
# tables=db_cursor.fetchall()
# print(tables)
# for table in tables:
#     db_cursor.execute('drop table ' + str(table[0]))


student_table = """
CREATE TABLE IF NOT EXISTS Student (
    admNo VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    gender ENUM('Male', 'Female', 'Other'),
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255) UNIQUE,
    aadhar CHAR(12) UNIQUE,
    father VARCHAR(100),
    mother VARCHAR(100),
    admissionDate DATE,
    admissionClass INT
);
"""

employee_table = """
CREATE TABLE IF NOT EXISTS Employee (
    eid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    gender ENUM('Male', 'Female', 'Other'),
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255) UNIQUE,
    aadhar CHAR(12) UNIQUE,
    role ENUM('Teacher', 'Staff'), 
    subjects TEXT DEFAULT NULL,
    offices TEXT DEFAULT NULL
) AUTO_INCREMENT = 1000;
"""

fees_table = """
CREATE TABLE IF NOT EXISTS Fees (
    admNo VARCHAR(20),
    month INT,
    year INT,
    date DATE,
    amount DECIMAL(10, 2),
    paid ENUM('Yes', 'No'),
    PRIMARY KEY (admNo, month, year),
    FOREIGN KEY (admNo) REFERENCES Student(admNo)
);
"""

salary_table = """
CREATE TABLE IF NOT EXISTS Salary (
    eid INT,
    month INT,
    year INT,
    date DATE,
    amount DECIMAL(10, 2),
    PRIMARY KEY (eid, month, year),
    FOREIGN KEY (eid) REFERENCES Employee(eid)
);
"""

db_cursor.execute(student_table)
db_cursor.execute(employee_table)
db_cursor.execute(fees_table)
db_cursor.execute(salary_table)
db_connection.commit()

def connection_close():
    db_cursor.close()
    db_connection.close()
