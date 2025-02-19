from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1344x690+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_depart = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()

        # Images and frames setup
        img = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img = img.resize((672, 200))
        self.photo_img = ImageTk.PhotoImage(img)
        st_img = Label(self.root, image=self.photo_img)
        st_img.place(x=0, y=0, width=672, height=200)

        img1 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img1 = img1.resize((672, 200))
        self.photo_img1 = ImageTk.PhotoImage(img1)
        images = Label(self.root, image=self.photo_img1)
        images.place(x=672, y=0, width=672, height=200)

        img3 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img3 = img3.resize((1344, 540))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        bg1 = Label(self.root, image=self.photo_img3)
        bg1.place(x=0, y=199, width=1344, height=540)

        title_lbl = Label(bg1, text="The Attendance Management System", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1344, height=50)

        main_frame = Frame(bg1, bd=2, bg="white")
        main_frame.place(x=2, y=55, width=1339, height=485)

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Detail", font=("times new roman", 18, "bold"), fg="darkred")
        left_frame.place(x=5, y=5, width=640, height=423)

        img_lf = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img_lf = img_lf.resize((630, 80))
        self.photo_img_lf = ImageTk.PhotoImage(img_lf)
        images = Label(left_frame, image=self.photo_img_lf)
        images.place(x=5, y=0, width=645, height=80)

        frame_inside_left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 18, "bold"), fg="darkred")
        frame_inside_left_frame.place(x=10, y=120, width=630, height=250)

        # Labels and entries
        Attendance_ID = Label(frame_inside_left_frame, text="Attendance ID", font=("times new roman", 12, "bold"), bg="white")
        Attendance_ID.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        attendance_id_entry = ttk.Entry(frame_inside_left_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        Student_Name_label = Label(frame_inside_left_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        Student_Name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        std_name_entry = ttk.Entry(frame_inside_left_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        std_name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        Roll_num_label = Label(frame_inside_left_frame, text="Roll.no", font=("times new roman", 12, "bold"), bg="white")
        Roll_num_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        attendance_student_name_entry = ttk.Entry(frame_inside_left_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        attendance_student_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        Department_label = Label(frame_inside_left_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        Department_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        Department_entry = ttk.Entry(frame_inside_left_frame, width=20, textvariable=self.var_atten_depart, font=("times new roman", 12, "bold"))
        Department_entry.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        Date_label = Label(frame_inside_left_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        Date_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        Date_entry = ttk.Entry(frame_inside_left_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        Date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        Attendance_Status_label = Label(frame_inside_left_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        Attendance_Status_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        Attendance_Status_combo = ttk.Combobox(frame_inside_left_frame, text="Attendance Status", width=17, textvariable=self.var_atten_status, font=("times new roman", 12, "bold"), state="readonly")
        Attendance_Status_combo["values"] = ("Select Attendance Status", "Present", "Absent", "Leave")
        Attendance_Status_combo.current(0)
        Attendance_Status_combo.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        btn_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="lightblue")
        btn_frame.place(x=10, y=350, width=630, height=75)

        import_btn = Button(btn_frame, text="Import CSV", width=22, height=3, command=self.import_Csv, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", width=22, height=3, command=self.export_Csv, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        reset_btn = Button(btn_frame, text="Reset", width=23, height=3, command=self.reset_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Detail", font=("times new roman", 18, "bold"), bg="white", fg="darkgreen")
        Right_frame.place(x=660, y=5, width=665, height=423)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=0, width=660, height=393)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.Attendance_Detail_Table = ttk.Treeview(table_frame, columns=("Attendance ID", "Student Name", "Roll num", "Department", "Date", "Attendance Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_Detail_Table.xview)
        scroll_y.config(command=self.Attendance_Detail_Table.yview)

        self.Attendance_Detail_Table.heading("Attendance ID", text="Attendance ID")
        self.Attendance_Detail_Table.heading("Student Name", text="Student Name")
        self.Attendance_Detail_Table.heading("Roll num", text="Roll num")
        self.Attendance_Detail_Table.heading("Department", text="Department")
        self.Attendance_Detail_Table.heading("Date", text="Date")
        self.Attendance_Detail_Table.heading("Attendance Status", text="Attendance Status")

        self.Attendance_Detail_Table["show"] = "headings"

        self.Attendance_Detail_Table.column("Attendance ID", width="150")
        self.Attendance_Detail_Table.column("Student Name", width="150")
        self.Attendance_Detail_Table.column("Roll num", width="150")
        self.Attendance_Detail_Table.column("Department", width="150")
        self.Attendance_Detail_Table.column("Date", width="150")
        self.Attendance_Detail_Table.column("Attendance Status", width="150")
        self.Attendance_Detail_Table.pack(fill=BOTH, expand=1)
        self.Attendance_Detail_Table.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self, rows):
        self.Attendance_Detail_Table.delete(*self.Attendance_Detail_Table.get_children())
        for row in rows:
            self.Attendance_Detail_Table.insert("", END, values=row)

    def import_Csv(self):
        global mydata
        mydata.clear()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        
        if file_path:
            with open(file_path) as myfile:
                csvread = csv.reader(myfile)
                next(csvread)  # Skip header
                for row in csvread:
                    # Ensure the row has the correct number of columns
                    if len(row) >= 6:  # Adjust based on your CSV structure
                        mydata.append(row)
                self.fetch_data(mydata)

    def export_Csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showinfo("No Data", "No Data found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", ".csv"), ("All file", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your Data Successfully Exported", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.Attendance_Detail_Table.focus()
        content = self.Attendance_Detail_Table.item(cursor_focus)
        rows = content.get('values')

        if rows and len(rows) >= 6:  # Ensure rows are not empty and have expected length
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_roll.set(rows[2])
            self.var_atten_depart.set(rows[3])
            self.var_atten_date.set(rows[4])
            self.var_atten_status.set(rows[5])
        else:
            print("No valid row selected or insufficient data.")

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_depart.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()