from Tkinter import *
import time

def Visual(data1, data2, data3, data4):
        win = Tk()
	win.title("Toothtest Visualization")
	win.geometry("1280x700+100+50")
	win.resizable(False, False)

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

	image1 = Label(win, textvariable=str_data1, width=28, height=13, relief="groove")
	image2 = Label(win, textvariable=str_data2, width=28, height=13, relief="groove")
	image3 = Label(win, textvariable=str_data3, width=28, height=13, relief="groove")
	image4 = Label(win, textvariable=str_data4, width=28, height=13, relief="groove")

	if data1<500:
		image1["bg"] = "red"
	elif data1>=500 and data1<1000:
		image1["bg"] = "orange"
	elif data1>=1000 and data1<1500:
		image1["bg"] = "yellow"
	elif data1>=1500 and data1<2000:
		image1["bg"] = "greenyellow"
	elif data1>=2000 and data1<2500:
		image1["bg"] = "aqua"
	elif data1>=2500 and data1<3000:
		image1["bg"] = "blue"
	elif data1>=3000 and data1<3500:
		image1["bg"] = "navy"
	else:
		image1["bg"] = "purple"

	if data2<500:
		image2["bg"] = "red"
	elif data2>=500 and data2<1000:
		image2["bg"] = "orange"
	elif data2>=1000 and data2<1500:
		image2["bg"] = "yellow"
	elif data2>=1500 and data2<2000:
		image2["bg"] = "greenyellow"
	elif data2>=2000 and data2<2500:
		image2["bg"] = "aqua"
	elif data2>=2500 and data2<3000:
		image2["bg"] = "blue"
	elif data2>=3000 and data2<3500:
		image2["bg"] = "navy"
	else:
		image2["bg"] = "purple"

	if data3<500:
		image3["bg"] = "red"
	elif data3>=500 and data3<1000:
		image3["bg"] = "orange"
	elif data3>=1000 and data3<1500:
		image3["bg"] = "yellow"
	elif data3>=1500 and data3<2000:
		image3["bg"] = "greenyellow"
	elif data3>=2000 and data3<2500:
		image3["bg"] = "aqua"
	elif data3>=2500 and data3<3000:
		image3["bg"] = "blue"
	elif data3>=3000 and data3<3500:
		image3["bg"] = "navy"
	else:
		image3["bg"] = "purple"

	if data4<500:
		image4["bg"] = "red"
	elif data4>=500 and data4<1000:
		image4["bg"] = "orange"
	elif data4>=1000 and data4<1500:
		image4["bg"] = "yellow"
	elif data4>=1500 and data4<2000:
		image4["bg"] = "greenyellow"
	elif data4>=2000 and data4<2500:
		image4["bg"] = "aqua"
	elif data4>=2500 and data4<3000:
		image4["bg"] = "blue"
	elif data4>=3000 and data4<3500:
		image4["bg"] = "navy"
	else:
		image4["bg"] = "purple"

	image1.place(x=80,y=250)
	image2.place(x=380,y=250)
	image3.place(x=680,y=250)
	image4.place(x=980,y=250)
        win.update()
        time.sleep(1)
        win.destroy()
