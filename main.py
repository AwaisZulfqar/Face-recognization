from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from studentDetail import Students
from faceRecognition import face_recog
from Attandence import Attendance
import os 
import platform
import subprocess

class Face_Recognization:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1344x690+0+0")
        self.root.title("Face Recognition Software")
        
        
        # the image1 of the page.
        img = Image.open('/home/jawadahmed/Face-Attandence/media/pexels-photo-8090261.webp')
        img = img.resize((448, 150))
        self.photo_img = ImageTk.PhotoImage(img)
        st_img = Label(self.root, image=self.photo_img)
        st_img.place(x=0, y=0, width=448, height=150)

        # the image2 of the page.
        img1 = Image.open('/home/jawadahmed/Face-Attandence/media/face-id-scan-recognition-ai-260nw-2311399379.webp')
        img1 = img1.resize((448, 150))
        self.photo_img1 = ImageTk.PhotoImage(img1)
        images = Label(self.root, image=self.photo_img1)
        images.place(x=448, y=0, width=448, height=150)

        # the image3 of the page.
        img2 = Image.open('/home/jawadahmed/Face-Attandence/media/Uni chowk.jpg')
        img2 = img2.resize((448, 150))
        self.photo_img2 = ImageTk.PhotoImage(img2)
        st1 = Label(self.root, image=self.photo_img2)
        st1.place(x=896, y=0, width=448, height=150)

        # the main back_ground image.
        img3 = Image.open('/home/jawadahmed/Face-Attandence/media/tech-bg-11.d855e9f.png')
        img3 = img3.resize((1344, 540))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        bg1 = Label(self.root, image=self.photo_img3)
        bg1.place(x=0, y=149, width=1344, height=540)

        # the main title label on back_ground image
        title_lbl = Label(bg1, text="The Face Recognition Attandance Management System By Haroon Ahmad ",
                            font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1344, height=40)

        # the main student button
        img4 = Image.open('/home/jawadahmed/Face-Attandence/media/stu.webp')
        img4 = img4.resize((320, 180))
        self.photo_img4 = ImageTk.PhotoImage(img4)
        
        btn1 = Button(bg1, image=self.photo_img4, command=self.Std_detail, cursor="hand2")
        btn1.place(x=160, y=80, width=320, height=180)
        # the studen detail button on student button
        btn1_1 = Button(bg1, text="Student Details", command=self.Std_detail, cursor="hand2",
                        font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn1_1.place(x=160, y=240, width=320, height=40)

        # the main face detection button
        img5 = Image.open('/home/jawadahmed/Face-Attandence/media/10.webp')
        img5 = img5.resize((320, 180))
        self.photo_img5 = ImageTk.PhotoImage(img5)

        btn_1 = Button(bg1, image=self.photo_img5, cursor="hand2", command=self.face_recognation)
        btn_1.place(x=560, y=80, width=320, height=180)

        btn_1 = Button(bg1, text="Face Detection", cursor="hand2", command=self.face_recognation,  font=("times new roman", 15, "bold"), bg="darkblue",
                       fg="white")
        btn_1.place(x=560, y=240, width=320, height=40)

        # the main attandance button
        img6 = Image.open('/home/jawadahmed/Face-Attandence/media/att.webp')
        img6 = img6.resize((320, 180))
        self.photo_img6 = ImageTk.PhotoImage(img6)
        btn_1 = Button(bg1, image=self.photo_img6, cursor="hand2",command=self.Attendance)
        btn_1.place(x=960, y=80, width=320, height=180)
        btn_1 = Button(bg1, text="Attandance", cursor="hand2",command=self.Attendance, font=("times new roman", 15, "bold"), bg="darkblue",
                       fg="white")
        btn_1.place(x=960, y=240, width=320, height=40)

        # the help desk  button
        img7 = Image.open('/home/jawadahmed/Face-Attandence/media/help.webp')
        img7 = img7.resize((320, 180))
        self.photo_img7 = ImageTk.PhotoImage(img7)
        btn_1 = Button(bg1, image=self.photo_img7, cursor="hand2")
        btn_1.place(x=960, y=310, width=320, height=180)
        btn_1 = Button(bg1, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",
                       fg="white")
        btn_1.place(x=960, y=480, width=320, height=40)

        # the train data  button
        img8 = Image.open('/home/jawadahmed/Face-Attandence/media/train.webp')
        img8 = img8.resize((320, 180))
        self.photo_img8 = ImageTk.PhotoImage(img8)

        btn_1 = Button(bg1, image=self.photo_img8, cursor="hand2", command=self.train_data)
        btn_1.place(x=160, y=320, width=320, height=180)

        btn_1 = Button(bg1, text="Train Data", cursor="hand2", command=self.train_data,
                       font=("times new roman", 15, "bold"), bg="darkblue",
                       fg="white")
        btn_1.place(x=160, y=480, width=320, height=40)

        # the photos button
        img9 = Image.open('/home/jawadahmed/Face-Attandence/media/photos.webp')
        img9 = img9.resize((320, 180))
        self.photo_img9 = ImageTk.PhotoImage(img9)

        btn_1 = Button(bg1, image=self.photo_img9, cursor="hand2", command=self.open_img)
        btn_1.place(x=560, y=320, width=320, height=180)

        btn_1 = Button(bg1, text="Photos", cursor="hand2", command=self.open_img,
                       font=("times new roman", 15, "bold"), bg="darkblue",
                       fg="white")
        btn_1.place(x=560, y=480, width=320, height=40)

    def open_img(sefl):
        path = "data"
        if platform.system() == "Windows":
            os.startfile(path)
        else:
            subprocess.call(["xdg-open", path])

    def show_attendance_sheet(self, file_path):
        if platform.system() == "Windows":
            os.startfile(file_path)
        else:  
            subprocess.call(["xdg-open", file_path])


        #==============  Function Buttion  ===========================
    def Std_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Students(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = train_data(self.new_window)

    def face_recognation(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recog(self.new_window)

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization(root)
    root.mainloop()
  