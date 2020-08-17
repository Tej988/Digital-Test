import sqlite3

    
def insert_sqlite_table(ques, opt1, opt2, opt3, opt4, ans):
    try:
        # Create Database
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()

        # Create Table
        cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
                    (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    Questions TEXT UNIQUE,
                    Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                    Answers TEXT)''')

        cur.execute('''INSERT INTO Teacher (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                    VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        conn.commit()

        print("Record inserted successfully into Teacher table", cur.rowcount)

        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into sqlite table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def question_data_fetch(ques_no):
    try:
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Teacher WHERE Ques_No = ?''', (ques_no))
        
        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_no))
            return list(row)
        
        cur.close()

    except sqlite3.Error as error:
        print("Failed to fetch record of sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def update_sqlite_table(ques, opt1, opt2, opt3, opt4, ans, ques_no):
    try:
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Teacher WHERE Ques_No = ?''', (ques_no, ))
        print("Reading single row")

        cur.fetchone()
        cur.execute('''UPDATE Teacher SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_no))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update multiple records of sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def delete_row(ques_no):
    try:
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''DELETE FROM Teacher WHERE Ques_No = ?''', (ques_no, ))

        conn.commit()

        print("Record deleted successfully")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def drop_sqlite_table():
    try:
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''DROP TABLE Teacher''')

        conn.commit()

        print("Table Dropped")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to drop table from a sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


if __name__ == '__main__':
    print("\n ***** Welcome Teachers ***** \n")
    print("1. Insert question")
    print("2. Fetch Data")
    print("3. Update question")
    print("4. Delete question")
    print("5. Delete data")
    print("6. Exit \n")
    
    val = input("Select your choice: ")

    if val == '1':
        for i in range(0, 3):
            n = 1
            ques = input('Enter the {} question: '.format(i + 1))
            opt1 = input('Enter the {} Option: '.format(1))
            opt2 = input('Enter the {} Option: '.format(2))
            opt3 = input('Enter the {} Option: '.format(3))
            opt4 = input('Enter the {} Option: '.format(4))  
            ans = input('Enter the correct answer: ')

            insert_sqlite_table(ques, opt1, opt2, opt3, opt4, ans)
    if val == '2':
        ques_no = input('Enter question number: ')

        fetched = question_data_fetch(ques_no)
        print(fetched)

    if val == '3':
        ques_no = input('Enter question number: ')
        
        ques = input('Enter the {} question: '.format(ques_no))
        opt1 = input('Enter the {} Option: '.format(1))
        opt2 = input('Enter the {} Option: '.format(2))
        opt3 = input('Enter the {} Option: '.format(3))
        opt4 = input('Enter the {} Option: '.format(4))  
        ans = input('Enter the correct answer: ')

        update_sqlite_table(ques, opt1, opt2, opt3, opt4, ans, ques_no)

    if val == '4':
        ques_no = input('Enter the row number which you want to delete: ')
        delete_row(ques_no)

    if val == '5':
        drop_sqlite_table()

    if val == '6':
        print('Thanks for vising here')
        quit()