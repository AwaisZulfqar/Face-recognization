import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox  # message box
import mysql.connector
import cv2  # use haar cascade algorithum for face decetion.
import os
import re



# this is the main class.
class Students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1344x690+0+0")
        self.root.title("face recognition system")

        # ==================== here we will creates the variables to add the data into the entry_field ====
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        # the first image of page.
        img = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img = img.resize((448, 150))
        self.photo_img = ImageTk.PhotoImage(img)
        st_img = Label(self.root, image=self.photo_img)
        st_img.place(x=0, y=0, width=448, height=150)

        # the image2 of the page.
        img1 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img1 = img1.resize((448, 150))
        self.photo_img1 = ImageTk.PhotoImage(img1)
        images = Label(self.root, image=self.photo_img1)
        images.place(x=448, y=0, width=448, height=150)

        # the image3 of the page.
        img2 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img2 = img2.resize((448, 150))
        self.photo_img2 = ImageTk.PhotoImage(img2)
        st1 = Label(self.root, image=self.photo_img2)
        st1.place(x=896, y=0, width=448, height=150)

        # the main back_ground image.
        img3 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img3 = img3.resize((1344, 540))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        bg1 = Label(self.root, image=self.photo_img3)
        bg1.place(x=0, y=149, width=1344, height=540)

        # the main title label on back_ground image
        title_lbl = Label(bg1, text="The Student Management System ", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1344, height=50)
        # the main frame on the background image.
        main_frame = Frame(bg1, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1324, height=485)

        # the left label frame in main frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Detail",
                                font=("times new roman", 18, "bold"), fg="darkred")
        left_frame.place(x=10, y=10, width=640, height=470)

        # the image in the left label frame.
        img_lf = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img_lf = img_lf.resize((630, 80))
        self.photo_img_lf = ImageTk.PhotoImage(img_lf)
        images = Label(left_frame, image=self.photo_img_lf)
        images.place(x=5, y=0, width=630, height=80)

        # Current course information frame
        Current_Course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 18, "bold"), fg="darkred")
        Current_Course_frame.place(x=10, y=110, width=638, height=90)

        # program label in Current_Course_frame.
        dep_lbl = Label(Current_Course_frame, text="Select-Program", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=5, sticky=W)

        # program_combo box with the help of ttk in front of dep_lbl
        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("BS", "ADP", "M.phil", "PHD", "Any-other")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        # department label in Current_Course_frame.
        course_lbl = Label(Current_Course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        course_lbl.grid(row=0, column=2, padx=5, sticky=W)

        # department_combo box with the help of ttk in front of course_lbl.
        course_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Department", "CS", "IT", "AI","soft.eng")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=2, sticky=W)

        # Year label in Current_Course_frame.
        year_lbl = Label(Current_Course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_lbl.grid(row=1, column=0, padx=5, sticky=W)

        # year_combo box with the help of ttk in front of course_lbl.
        year_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select year", 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=2, sticky=W)

        # Semester label in Current_Course_frame.
        semester_lbl = Label(Current_Course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_lbl.grid(row=1, column=2, padx=5, sticky=W)

        # semester_combo box with the help of ttk in front of course_lbl.
        sem_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_semester,
                                 font=("times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3th", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=2, sticky=W)

        # Class student information frame
        Class_std_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                     font=("times new roman", 18, "bold"), fg="darkred")
        Class_std_frame.place(x=10, y=202, width=638, height=277)

        # Student_ID_label in Class_std_frame .
        Student_ID_label = Label(Class_std_frame, text="Student_ID", font=("times new roman", 12, "bold"), bg="white")
        Student_ID_label.grid(row=0, column=0, padx=10, sticky=W)
        # student id entry field.
        stdID_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_std_id,
                                font=("times new roman", 12, "bold"))
        stdID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student_name_label in Class_std_frame .
        Student_Name_label = Label(Class_std_frame, text="Student_Name", font=("times new roman", 12, "bold"),
                                   bg="white")
        Student_Name_label.grid(row=0, column=2, padx=10, sticky=W)
        # student name entry_field.
        std_name_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_std_name,
                                   font=("times new roman", 12, "bold"))
        std_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class_division_label in Class_std_frame .
        class_division_label = Label(Class_std_frame, text="Course", font=("times new roman", 12, "bold"),
                                     bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        # combo box for div
        gen_combo = ttk.Combobox(Class_std_frame, textvariable=self.var_div, width=13,
                                 font=("times new roman", 12, "bold"), state="readonly")
        gen_combo["values"] = ("Select Course", "IOT", "MAD", "AI", "ML", "Psychology", "IR","opp","ict","networking","database","soft.req.eng","data mining")
        gen_combo.current(0)
        gen_combo.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        # Roll_no_label in Class_std_frame .
        Roll_no_label = Label(Class_std_frame, text="Roll_no", font=("times new roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=1, column=2, padx=10, pady=2, sticky=W)
        # Roll_no entry_field.
        Roll_no_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_roll_no,
                                  font=("times new roman", 12, "bold"))
        Roll_no_entry.grid(row=1, column=3, padx=10, pady=2, sticky=W)

        # Gender_label in Class_std_frame .
        Gender_label = Label(Class_std_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        # combo box for gender
        gen_combo = ttk.Combobox(Class_std_frame, textvariable=self.var_gender, width=13,
                                 font=("times new roman", 12, "bold"), state="readonly")
        gen_combo["values"] = ("Male", "Female", "Other")
        gen_combo.current(0)
        gen_combo.grid(row=2, column=1, padx=10, pady=2, sticky=W)

        # DOB_label in Class_std_frame .
        DOB_label = Label(Class_std_frame, text="Date_of_birth", font=("times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=2, sticky=W)
        # DOB entry_field.
        DOB_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_dob,
                              font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=2, sticky=W)

        # Email_label in Class_std_frame .
        Email_label = Label(Class_std_frame, text="Email", font=("times new roman", 11, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=2, sticky=W)
        # Email entry_field.
        Email_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_email,
                                font=("times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)

        # Phone_no_label in Class_std_frame .
        Phone_no_label = Label(Class_std_frame, text="Phone_no", font=("times new roman", 11, "bold"), bg="white")
        Phone_no_label.grid(row=3, column=2, padx=10, pady=2, sticky=W)
        # Phone number entry_field.
        Phone_no_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_phone,
                                   font=("times new roman", 12, "bold"))
        Phone_no_entry.grid(row=3, column=3, padx=10, pady=2, sticky=W)

        # Address_label in Class_std_frame .
        Address_label = Label(Class_std_frame, text="Adress", font=("times new roman", 11, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=2, sticky=W)
        # Address entry_field.
        Address_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_address,
                                  font=("times new roman", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)

        # Teacher_Name_label in Class_std_frame .
        Teacher_Name_label = Label(Class_std_frame, text="Teacher_Name", font=("times new roman", 11, "bold"),
                                   bg="white")
        Teacher_Name_label.grid(row=4, column=2, padx=10, pady=2, sticky=W)
        # Teacher_Name entry_field.
        Teacher_Name_entry = ttk.Entry(Class_std_frame, width=15, textvariable=self.var_teacher,
                                       font=("times new roman", 12, "bold"))
        Teacher_Name_entry.grid(row=4, column=3, padx=10, pady=2, sticky=W)

        # Radio_buttons for take photo sample
        self.var_radio1 = StringVar()
        Rd_btn1 = Radiobutton(Class_std_frame, variable=self.var_radio1, text="Take photo sample", value="yes")
        Rd_btn1.grid(row=6, column=0)

        Rd_btn1 = Radiobutton(Class_std_frame, variable=self.var_radio1, text="No photo sample", value="no")
        Rd_btn1.grid(row=6, column=1)

        # Button frame for (save,delete,update and reset button) in Class student information frame
        btn_frame = Frame(Class_std_frame, bd=2, relief=RIDGE, bg="lightblue")
        btn_frame.place(x=0, y=170, width=635, height=38)

        # save btn in button frame
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update btn in button frame
        update_btn = Button(btn_frame, text="Update", width=16, command=self.update_data,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        # delete btn for  in button frame
        delete_btn = Button(btn_frame, text="Delete", width=16, command=self.delete_data,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset btn in button frame
        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data,
                           font=("times new roman", 12, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # Button_photo_frame for ((take photo or update photo)) in Class student information frame
        btn_photo_frame = Frame(Class_std_frame, bd=2, relief=RIDGE, bg="lightblue")
        btn_photo_frame.place(x=0, y=205, width=635, height=38)

        # take_photo_btn in button_photo frame
        take_photo_btn = Button(btn_photo_frame, text="Take photo", width=69, command=self.generate_data,
                                font=("times new roman", 12, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        # the right label frame in main frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Detail",
                                 font=("times new roman", 18, "bold"), bg="white", fg="darkgreen")
        Right_frame.place(x=660, y=10, width=650, height=470)

        # the image in the right label frame.
        img_rf = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img_rf = img_rf.resize((645, 80))
        self.photo_img_rf = ImageTk.PhotoImage(img_rf)
        images = Label(Right_frame, image=self.photo_img_rf)
        images.place(x=5, y=0, width=640, height=80)

        # =========================search system in right label frame=============================

        # Class student information frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 18, "bold"), fg="darkred")
        search_frame.place(x=5, y=73, width=640, height=70)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=100, width=640, height=330)

        # scroll bar in table frame
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
            "Dep", "course", "year", "sem", "id", "name", "div", "roll", "gen", "dob", "email", "phone", "adr",
            "teacher",
            "img"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # how to show the header_names in Student_table.
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone_no")
        self.student_table.heading("adr", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("img", text="Photo_image")
        self.student_table["show"] = "headings"

        # how to set column width
        self.student_table.column("Dep", width=80)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=80)
        self.student_table.column("id", width=80)
        self.student_table.column("name", width=80)
        self.student_table.column("div", width=80)
        self.student_table.column("roll", width=80)
        self.student_table.column("gen", width=80)
        self.student_table.column("email", width=80)
        self.student_table.column("dob", width=80)
        self.student_table.column("phone", width=80)
        self.student_table.column("adr", width=80)
        self.student_table.column("teacher", width=80)
        self.student_table.column("img", width=80)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============== the function to add the data into database =============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id == "" or \
                self.var_semester == "" or self.var_course == "" or self.var_year == "" or self.var_div == "" or \
                self.var_roll_no == "" or self.var_gender == "" or self.var_dob == "" or self.var_email == "" \
                or self.var_phone == "" or self.var_address == "" or self.var_teacher == "" or self.var_radio1 == "":
            messagebox.showerror("Error", "All fields are required to fill", parent=self.root)
        name_pattern = r"^[A-Za-z\s]+$"
        phone_pattern =r"^\+92-\d{3}-\d{7}$"
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        name1_pattern = r"^[A-Za-z\s]+$"

        if not re.match(name_pattern, self.var_std_name.get()):
            messagebox.showerror("Error", "Invalid name. Please enter a valid name.", parent=self.root)
        elif not re.match(phone_pattern, self.var_phone.get()):
            messagebox.showerror("Error", "Invalid phone number. Please enter a valid phone number.", parent=self.root)
        elif not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror("Error", "Invalid email address. Please enter a valid email address.", parent=self.root)
        elif not re.match(name1_pattern, self.var_teacher.get()):
            messagebox.showerror("Error", "Invalid Teacher name. Please enter a valid Teacher name", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "awais",password = "Pass123!",database = "face_recognition")
                my_cursor =conn.cursor()
                my_cursor.execute("insert into students_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_std_id.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll_no.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get(),
                                   self.var_radio1.get()
                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "students detail has beeb successfully add", parent=self.root)
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # ============== fetch data  from database to our root table =================
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="awais",
                password="Pass123!",
                database="face_recognition"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM students_detail")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            else:
                print("No data found in the database.")  # Debug statement
            conn.close()
        except mysql.connector.Error as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # part1. work on update button(the work of this function is to load the data into frame fro update purpose)
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        # print("Data from table:", data)  # Debug statement

        if data:  # Check if data is not empty
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll_no.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        else:
            messagebox.showwarning("Warning", "No data selected or data is empty.", parent=self.root)

    # part2. work on update button(the main update function)
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or
                self.var_std_name.get() == "" or self.var_std_id == "" or
                self.var_semester == "" or self.var_course == "" or
                self.var_year == "" or self.var_div == "" or
                self.var_roll_no == "" or self.var_gender == "" or
                self.var_dob == "" or self.var_email == "" or
                self.var_phone == "" or self.var_address == "" or
                self.var_teacher == "" or self.var_radio1 == ""):
            messagebox.showerror("Error", "All fields are required to fill", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?",
                                             parent=self.root)
                if update:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "1122",database = "face_recognition")
                    my_cursor =conn.cursor()
                    # Use parameterized query to prevent SQL injection attacks
                    my_cursor.execute("UPDATE students_detail SET Department=%s, Course=%s, year=%s, Semester=%s, Name=%s, " \
                          "Division=%s, `Roll_no`=%s, Gander=%s, DOB=%s, Email=%s, `Phone_no`=%s, Address=%s, Teacher=%s, " \
                          "Photo_img=%s WHERE id=%s",(
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                            self.var_std_name.get(), self.var_div.get(), self.var_roll_no.get(), self.var_gender.get(),
                            self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                            self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get())

                          )
                    conn.commit()

                    # Close database connection
                    my_cursor.close()
                    conn.close()

                    messagebox.showinfo("Success", "The student detail update completed", parent=self.root)
                    self.fetch_data()
                else:
                    # User cancelled update
                    return
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please select a student record to delete", parent=self.root)
            return
        else:
            try:
                delete = messagebox.askyesno("Confirm", "Are you sure you want to delete this student record?",
                                             parent=self.root)
                if delete > 0:
                    # Connect to the database
                    conn = mysql.connector.connect(host = "localhost",username = "awais",password = "Pass123!",database = "face_recognition")
                    my_cursor =conn.cursor()

                    # Delete the selected student's record from the database
                    sql = "DELETE FROM students_detail WHERE id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                # Close database connection
                conn.close()
                messagebox.showinfo("Success", "The student record was successfully deleted", parent=self.root)
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Cource")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll_no.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        # Display a success message to the user
        messagebox.showinfo("Success", "Data has been reset", parent=self.root)

        # === Generate a Data set or Take Photo sample=====

    def generate_data(self):
        if (self.var_dep.get() == "Select Department" or
                self.var_std_name.get() == "" or self.var_std_id.get() == "" or
                self.var_semester.get() == "" or self.var_course.get() == "" or
                self.var_year.get() == "" or self.var_div.get() == "" or
                self.var_roll_no.get() == "" or self.var_gender.get() == "" or
                self.var_dob.get() == "" or self.var_email.get() == "" or
                self.var_phone.get() == "" or self.var_address.get() == "" or
                self.var_teacher.get() == "" or self.var_radio1.get() == ""):
            messagebox.showerror("Error", "All fields are required to fill", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="awais", password="Pass123!",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM students_detail")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE students_detail SET Department=%s, Course=%s, year=%s, Semester=%s, Name=%s, "
                                   "Division=%s, `Roll_no`=%s, Gender=%s, DOB=%s, Email=%s, `Phone_no`=%s, Address=%s, "
                                   "Teacher=%s, Photo_img=%s WHERE id=%s",
                                   (self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                                    self.var_semester.get(), self.var_std_name.get(), self.var_div.get(),
                                    self.var_roll_no.get(), self.var_gender.get(), self.var_dob.get(),
                                    self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                                    self.var_teacher.get(), self.var_radio1.get(),self.var_std_id.get() == id+1
                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("/home/jawadahmed/Face-Attandence/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    if len(faces) == 0:
                        print("No faces detected in the current frame. Please adjust your position or lighting conditions.")
                        return None
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id+=1
                        face = cv2.resize(cropped_face,(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0))
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()   
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generated dataset completed")

            except mysql.connector.Error as es:
                 messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

        



if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()
