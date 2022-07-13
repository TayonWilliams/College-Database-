#connecting python with MySQL
import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password='Steelers1!',
    database="university"
)
command_handler = db.cursor(buffered =True)



#admin power
def teacher_menu():
    print("")
    while 1:
        print("Teacher menu")
        print("1. Grade Students")
        print("2. View Students grades")
        print("3. logout")
        user_option = input(str("Option: "))
        print("")
        if user_option == '1':
            command_handler.execute("SELECT username_student From student")
            records = command_handler.fetchall()
            for record in records:
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                grade = input(f"Enter Grade for {record}: ")
                query_grade = (grade,str(record))
                command_handler.execute("UPDATE student SET grade = %s WHERE username_student = %s", query_grade)
                db.commit()
                print(f"{record} has a {grade} this semester")
                print("")

        elif user_option == '2':
            command_handler.execute("SELECT username_student,grade From student")
            records = command_handler.fetchall()
            print("All Students Grades")
            for record in records:
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                record = str(record).replace("'","")
                record = str(record).replace("None","N/A")
                print(record)
            print("")

        elif user_option == '3':
            main()
        else:
            print("Please pick a choice below")
            print("")
#admin power
def admin_menu():
    print("")
    while 1:
        print("Admin menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete existing Student")
        print("4. Delete existing Teacher")
        print("5. View all records")
        print("6. logout")
        user_option = input(str("Option: "))
        print("")
        #add user
        if user_option == "1":
           username = input(str("Enter student's username: "))
           password = input(str("Enter student's password: "))

           query_newStudent = (username, password)
           command_handler.execute("INSERT INTO student (username_student, password_student) Values (%s,%s)",
                                   query_newStudent)
           db.commit()
           print(f"{username} is now a student at University College")
           print("")
        elif user_option == "2":
            username = input(str("Enter Teacher's username: "))
            password = input(str("Enter Teacher's password: "))
            query_newStudent = (username, password)
            command_handler.execute("INSERT INTO teacher (username_teacher, password_teacher) Values (%s,%s)",
                                query_newStudent)
            db.commit()
            print(f"{username} is now a teacher at University College")
            print("")
            #Delete user
        elif user_option == "3":
            username = input(str("Enter Student's username: "))
            password = input(str("Enter Student's password: "))
            query_newStudent = (username, password)
            command_handler.execute("DELETE FROM student WHERE username_student = %s AND password_student = %s",
                                    query_newStudent)
            if command_handler.rowcount < 1:
                print("No student in our record")
                print("")
            db.commit()
            print(f"{username} is no longer a student at University College")
            print("")
        elif user_option == "4":
            username = input(str("Enter Teacher's username: "))
            password = input(str("Enter Teacher's password: "))
            query_newStudent = (username, password)
            command_handler.execute("DELETE FROM teacher WHERE username_teacher = %s AND password_teacher = %s",
                                query_newStudent)
            if command_handler.rowcount < 1:
                print("No student in our record")
                print("")
            db.commit()
            print(f"{username} is no longer a student at University College")
            print("")

        elif user_option == "5":
            command_handler.execute("SELECT username_teacher, password_teacher FROM teacher UNION ALL SELECT username_student, password_student FROM student")
            records = command_handler.fetchall()
            print("Records of Teachers and Students at University College")
            print("")
            for record in records:
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                record = str(record).replace("'","")
                print(record)
            print("")

        elif user_option == "6":
            main()
        else:
            print("Please pick a choice below")
            print("")

#Student authorization
def student_authorization():
    while 1:
        username = input(str("Enter Student Username: "))
        password = input(str("Enter Student Password: "))
        query_teacher = (username,password)
        command_handler.execute("SELECT username_student,grade FROM student WHERE username_student = %s AND password_student = %s", query_teacher)
        if command_handler.rowcount <= 0:
            print("Login not recognized")
            print("")

        else:
        #admin student
            while 1:
                print("")
                print("Student menu")
                print("1. View Students grades")
                print("2. logout")
                user_option = input(str("Option: "))
                print("")
                if user_option == "1":
                    record = command_handler.fetchall()
                    for records in record:
                        records = str(records).replace("(","")
                        records = str(records).replace(")","")
                        records = str(records).replace("'","")
                        print(records)
                elif user_option == '2':
                    main()


#teacher authorization
def teacher_authorization():
    while 1:
        username = input(str("Enter Teacher Username: "))
        password = input(str("Enter Teacher Password: "))
        query_teacher = (username,password)
        command_handler.execute("SELECT * FROM teacher WHERE username_teacher = %s AND password_teacher = %s", query_teacher)
        if command_handler.rowcount <= 0:
            print("Login not recognized")
            print("")

        else:
            teacher_menu()


    #admin authorization
def  admin_authorization():
    while 1:
        username = input(str("Enter Admin Username: "))
        password = input(str("Enter Admin Password: "))
        if username == "admin":
            password
            if password == "password":
                admin_menu()
            else:
                print("")
                print("Login not recognized")
        else:
            print("")
            print("Login not recognized")
            print("")

#menu
def main():
    while 1:
        print("Welcome to University College!")
        print("")
        print("Choose an option below")
        print("1. Student login")
        print("2. Teacher login")
        print("3. Admin login")
        user_option = input(str("Option: "))
        print("")
        #login
        if user_option == "1":
            student_authorization()
        elif user_option == "2":
            teacher_authorization()
        elif user_option == "3":
            admin_authorization()

main()