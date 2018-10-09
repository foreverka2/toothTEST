from Tkinter import *
from tkFont import Font
from PIL import ImageTk, Image
import random
import time

win = Tk()
win.title("Teethtest Visualization")
win.geometry("1280x700+100+50")
win.resizable(False, False)

font1=Font(size=18, slant="italic")
font2=Font(size=15, slant="italic")
font3=Font(size=40, slant="roman", weight="bold")

data1_str_value = str(data1)
data2_str_value = str(data2)
data3_str_value = str(data3)
data4_str_value = str(data4)

str_data1 = StringVar()
str_data2 = StringVar()
str_data3 = StringVar()
str_data4 = StringVar()

str_data1.set(data1_str_value)
str_data2.set(data2_str_value)
str_data3.set(data3_str_value)
str_data4.set(data4_str_value)

image1 = Label(win, textvariable=str_data1, width=14, height=7, relief="groove", font=font1)
image2 = Label(win, textvariable=str_data2, width=14, height=7, relief="groove", font=font1)
image3 = Label(win, textvariable=str_data3, width=14, height=7, relief="groove", font=font1)
image4 = Label(win, textvariable=str_data4, width=14, height=7, relief="groove", font=font1)

if data1<300:
   image1["bg"] = "red"
elif data1>=340 and data1<380:
   image1["bg"] = "orange"
elif data1>=380 and data1<420:
   image1["bg"] = "yellow"
elif data1>=420 and data1<460:
   image1["bg"] = "greenyellow"
elif data1>=460 and data1<500:
   image1["bg"] = "aqua"
elif data1>=500 and data1<540:
   image1["bg"] = "blue"
elif data1>=540 and data1<580:
   image1["bg"] = "navy"
else:
   image1["bg"] = "purple"

if data2<300:
   image1["bg"] = "red"
elif data2>=340 and data2<380:
   image1["bg"] = "orange"
elif data2>=380 and data2<420:
   image1["bg"] = "yellow"
elif data2>=420 and data2<460:
   image1["bg"] = "greenyellow"
elif data2>=460 and data2<500:
   image1["bg"] = "aqua"
elif data2>=500 and data<540:
   image1["bg"] = "blue"
elif data2>=540 and data2<580:
   image1["bg"] = "navy"
else:
   image1["bg"] = "purple"

if data3<300:
   image1["bg"] = "red"
elif data3>=340 and data3<380:
   image1["bg"] = "orange"
elif data3>=380 and data3<420:
   image1["bg"] = "yellow"
elif data3>=420 and data3<460:
   image1["bg"] = "greenyellow"
elif data3>=460 and data3<500:
   image1["bg"] = "aqua"
elif data3>=500 and data3<540:
   image1["bg"] = "blue"
elif data3>=540 and data3<580:
   image1["bg"] = "navy"
else:
   image1["bg"] = "purple"

if data4<300:
   image1["bg"] = "red"
elif data4>=340 and data4<380:
   image1["bg"] = "orange"
elif data4>=380 and data4<420:
   image1["bg"] = "yellow"
elif data4>=420 and data4<460:
   image1["bg"] = "greenyellow"
elif data4>=460 and data4<500:
   image1["bg"] = "aqua"
elif data4>=500 and data4<540:
   image1["bg"] = "blue"
elif data4>=540 and data4<580:
   image1["bg"] = "navy"
else:
   image1["bg"] = "purple"

Title=Message(win, text="Teethtest Visualization", width=600, relief="flat", font=font3)

message1=Message(win, text="Right molar", width=200, relief="flat", font=font2)
message2=Message(win, text="Right canine", width=200, relief="flat", font=font2)
message3=Message(win, text="Left canine", width=200, relief="flat", font=font2)
message4=Message(win, text="Left molar", width=200, relief="flat", font=font2)

path = "Legend_2.png"
img_legend = ImageTk.PhotoImage(Image.open(path))
legend = Label(win, image = img_legend)

Title.pack(ipady=45)

legend.pack(side="bottom", ipady=30)

image1.place(x=980,y=220)
image2.place(x=680,y=220)
image3.place(x=380,y=220)
image4.place(x=80,y=220)

message1.place(x=1025,y=440)
message2.place(x=725,y=440)
message3.place(x=420,y=440)
message4.place(x=120,y=440)

win.update()
time.sleep(0.01)

win.mainloop()
