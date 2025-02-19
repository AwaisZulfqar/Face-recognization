import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np
import time
from tkinter import messagebox


# this is the main class.
class face_recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1344x690+0+0")
        self.root.title("face recognition system")

                # the main title label 
        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 30, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1344, height=40)

                  # the first image of page.
        img = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img = img.resize((450, 645))
        self.photo_img = ImageTk.PhotoImage(img)

        st_img = Label(self.root, image=self.photo_img)
        st_img.place(x=0, y=42, width=450, height=645)


                # the last image of page.
        img1 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img1 = img.resize((894, 645))
        self.photo_img1 = ImageTk.PhotoImage(img1)
        
        fl_img1 = Label(self.root, image=self.photo_img1)
        fl_img1.place(x=450, y=42, width=894, height=645)

                # face recognition in button frame
        face_recognition_btn = Button(fl_img1, text="Face Recognition", width=300,command=self.start_face_recognition,font=("times new roman", 25, "bold"),
                          bg="yellow", fg="darkgreen")
        face_recognition_btn.place(x=300,y=550,width=300,height=70)

        #================ mark attandence ===================




    def mark_attendance(self, id, name, roll_no, department):
        file_path = "attendance.csv"

        # Create the file with headers if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as f:
                f.write("ID,Name,Roll_no,Department,Time,Date,Status\n")

        # Append new attendance entry
        now = datetime.now()
        dtString = now.strftime("%H:%M:%S")
        dateString = now.strftime("%d/%m/%y")

        with open(file_path, "a", newline="") as f:
            f.write(f"{id},{name},{roll_no},{department},{dtString},{dateString},Present\n")
        messagebox.showinfo("Success", "Attendance Marked Successfully!")



        # ======face recognition==========
      # ====== face recognition ==========
    def start_face_recognition(self):
        face_cascade = cv2.CascadeClassifier("/home/jawadahmed/Face-Attandence/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # Start camera
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera could not be opened.")
            return

        detected = False
        start_time = None

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                if confidence > 70:
                    conn = mysql.connector.connect(
                        host="localhost", username="awais", password="Pass123!", database="face_recognition"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT id, Name, Roll_no, Department FROM students_detail WHERE id = %s", (id,))
                    result = my_cursor.fetchone()
                    conn.close()

                    if result:
                        id, name, roll_no, department = result
                        cv2.putText(img, f"ID: {id}", (x, y - 95), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                        cv2.putText(img, f"Name: {name}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(img, f"Roll No: {roll_no}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Department: {department}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

                        if not detected:
                            start_time = time.time()  # Start the 3-second timer
                            detected = True

            cv2.imshow("Face Recognition", img)
            cv2.waitKey(1)

            # After detection, wait for 3 seconds, then mark attendance
            if detected and (time.time() - start_time >= 3):
                self.mark_attendance(id, name, roll_no, department)
                break  # Exit the loop after marking attendance

        video_cap.release()
        cv2.destroyAllWindows()
        if detected:
            messagebox.showinfo("Success", "Attendance Marked Successfully!")
        else:
            messagebox.showwarning("Warning", "No face detected.")




if __name__ == "__main__":
    root = Tk()
    obj = face_recog(root)
    root.mainloop()
                

