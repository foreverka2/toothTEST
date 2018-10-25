import process
import processNoCloud
from Tkinter import *
from tkFont import Font
from PIL import ImageTk, Image
import time

win = Tk()
win.title("Teethtest Visualization")
win.geometry("1280x600+80+30")
win.resizable(False, False)

font1=Font(size=18, slant="italic")
font2=Font(size=15, slant="italic")
font3=Font(size=40, slant="roman", weight="bold")

Title=Message(win, text="Teethtest Visualization", width=1200, relief="flat", font=font3)

message1=Message(win, text="Right molar", width=200, relief="flat", font=font2)
message2=Message(win, text="Right canine", width=200, relief="flat", font=font2)
message3=Message(win, text="Left canine", width=200, relief="flat", font=font2)
message4=Message(win, text="Left molar", width=200, relief="flat", font=font2)

path = "Legend_2.png"
img_legend = ImageTk.PhotoImage(Image.open(path))
legend = Label(win, image = img_legend)

Title.pack(ipady=30)

message1.place(x=1025,y=400)
message2.place(x=725,y=400)
message3.place(x=420,y=400)
message4.place(x=120,y=400)

legend.pack(side="bottom", ipady=25)

def main():
    print "Code start!"
    while True :
        #R0_data1, R0_data2, R0_data3, R0_data4 = process.SetR0()
        R0_data1, R0_data2, R0_data3, R0_data4 = processNoCloud.SetR0()
        if R0_data1 != -1 :
            break
    while True :    
        #data1, data2, data3, data4 = process.Cloud(R0_data1, R0_data2, R0_data3, R0_data4)
	data1, data2, data3, data4 = processNoCloud.Cloud(R0_data1, R0_data2, R0_data3, R0_data4)

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
	elif data1>=300 and data1<350:
   		image1["bg"] = "orange"
	elif data1>=350 and data1<400:
   		image1["bg"] = "yellow"
	elif data1>=400 and data1<450:
   		image1["bg"] = "greenyellow"
	elif data1>=450 and data1<500:
   		image1["bg"] = "aqua"
	elif data1>=500 and data1<550:
   		image1["bg"] = "blue"
	elif data1>=550 and data1<600:
   		image1["bg"] = "navy"
	else:
   		image1["bg"] = "purple"

	if data2<300:
   		image2["bg"] = "red"
	elif data2>=300 and data2<350:
   		image2["bg"] = "orange"
	elif data2>=350 and data2<400:
   		image2["bg"] = "yellow"
	elif data2>=400 and data2<450:
   		image2["bg"] = "greenyellow"
	elif data2>=450 and data2<500:
   		image2["bg"] = "aqua"
	elif data2>=500 and data2<550:
   		image2["bg"] = "blue"
	elif data2>=550 and data2<600:
   		image2["bg"] = "navy"
	else:
   		image2["bg"] = "purple"

	if data3<300:
   		image3["bg"] = "red"
	elif data3>=300 and data3<350:
		image3["bg"] = "orange"
	elif data3>=350 and data3<400:
		image3["bg"] = "yellow"
	elif data3>=400 and data3<450:
   		image3["bg"] = "greenyellow"
	elif data3>=450 and data3<500:
   		image3["bg"] = "aqua"
	elif data3>=500 and data3<550:
   		image3["bg"] = "blue"
	elif data3>=550 and data3<600:
   		image3["bg"] = "navy"
	else:
   		image3["bg"] = "purple"

	if data4<300:
   		image4["bg"] = "red"
	elif data4>=300 and data4<350:
   		image4["bg"] = "orange"
	elif data4>=350 and data4<400:
   		image4["bg"] = "yellow"
	elif data4>=400 and data4<450:
   		image4["bg"] = "greenyellow"
	elif data4>=450 and data4<500:
   		image4["bg"] = "aqua"
	elif data4>=500 and data4<550:
   		image4["bg"] = "blue"
	elif data4>=550 and data4<600:
   		image4["bg"] = "navy"
	else:
   		image4["bg"] = "purple"


	image1.place(x=80,y=180)
	image2.place(x=380,y=180)
	image3.place(x=680,y=180)
	image4.place(x=980,y=180)

        win.update()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
