import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
from tkinter import *
# from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import os
import numpy as np
from tkinter import messagebox


# this is the main class.
class train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1344x690+0+0")
        self.root.title("Face recognition system")

                # the main title label 
        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1344, height=40)

                # the first image of page.
        img = Image.open('/home/jawadahmed/Face-Attandence/media/tech-bg-11.d855e9f.png')
        img = img.resize((1340, 275))
        self.photo_img = ImageTk.PhotoImage(img)

        st_img = Label(self.root, image=self.photo_img)
        st_img.place(x=0, y=42, width=1340, height=275)


        # train_data_btn 
        trin_btn = Button(self.root, text="TRAIN DATA", width=1344, command=self.train_classifier,font=("times new roman", 78, "bold"),
                          bg="red", fg="white")
        trin_btn.place(x=0,y=320,width=1340,height=91)


                # the last image of page.
        img1 = Image.open('/home/jawadahmed/Face-Attandence/media/tech-bg-11.d855e9f.png')
        img1 = img.resize((1340, 275))
        self.photo_img1 = ImageTk.PhotoImage(img1)
        
        fl_img1 = Label(self.root, image=self.photo_img1)
        fl_img1.place(x=0, y=412, width=1340, height=275)

    def train_classifier(self):
        data_dirt = ("data")
        path = [os.path.join(data_dirt,file) for file in os.listdir(data_dirt)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Convert to grayscale
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids =np.array(ids)


        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training completed successfully.")


if __name__ == "__main__":
    root = Tk()
    obj = train_data(root)
    root.mainloop()