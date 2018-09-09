from Tkinter import *
import random

def Visual(data1, data2, data3, data4):
	data1_str_value = str(data1)
	data2_str_value = str(data2)
	data3_str_value = str(data3)
	data4_str_value = str(data4)

	win = Tk()
	win.title("Toothtest Visualization")
	win.geometry("1280x700+100+50")
	win.resizable(False, False)

	str_data1 = StringVar()
	str_data2 = StringVar()
	str_data3 = StringVar()
	str_data4 = StringVar()

	str_data1.set(data1_str_value + "ohm")
	str_data2.set(data2_str_value + "ohm")
	str_data3.set(data3_str_value + "ohm")
	str_data4.set(data4_str_value + "ohm")

	image1 = Label(win, textvariable=str_data1, width=28, height=13, relief="groove")
	image2 = Label(win, textvariable=str_data2, width=28, height=13, relief="groove")
	image3 = Label(win, textvariable=str_data3, width=28, height=13, relief="groove")
	image4 = Label(win, textvariable=str_data4, width=28, height=13, relief="groove")

	if data1<4500:
		image1["bg"] = "red"
	elif data1>=4500 and data1<5000:
		image1["bg"] = "orange"
	elif data1>=5000 and data1<5500:
		image1["bg"] = "yellow"
	elif data1>=5500 and data1<6000:
		image1["bg"] = "greenyellow"
	elif data1>=6000 and data1<6500:
		image1["bg"] = "aqua"
	elif data1>=6500 and data1<7000:
		image1["bg"] = "blue"
	elif data1>=7000 and data1<7500:
		image1["bg"] = "navy"
	else:
		image1["bg"] = "purple"

	if data2<4500:
		image2["bg"] = "red"
	elif data2>=4500 and data2<5000:
		image2["bg"] = "orange"
	elif data2>=5000 and data2<5500:
		image2["bg"] = "yellow"
	elif data2>=5500 and data2<6000:
		image2["bg"] = "greenyellow"
	elif data2>=6000 and data2<6500:
		image2["bg"] = "aqua"
	elif data2>=6500 and data2<7000:
		image2["bg"] = "blue"
	elif data2>=7000 and data2<7500:
		image2["bg"] = "navy"
	else:
		image2["bg"] = "purple"

	if data3<4500:
		image3["bg"] = "red"
	elif data3>=4500 and data3<5000:
		image3["bg"] = "orange"
	elif data3>=5000 and data3<5500:
		image3["bg"] = "yellow"
	elif data3>=5500 and data3<6000:
		image3["bg"] = "greenyellow"
	elif data3>=6000 and data3<6500:
		image3["bg"] = "aqua"
	elif data3>=6500 and data3<7000:
		image3["bg"] = "blue"
	elif data3>=7000 and data3<7500:
		image3["bg"] = "navy"
	else:
		image3["bg"] = "purple"

	if data4<4500:
		image4["bg"] = "red"
	elif data4>=4500 and data4<5000:
		image4["bg"] = "orange"
	elif data4>=5000 and data4<5500:
		image4["bg"] = "yellow"
	elif data4>=5500 and data4<6000:
		image4["bg"] = "greenyellow"
	elif data4>=6000 and data4<6500:
		image4["bg"] = "aqua"
	elif data4>=6500 and data4<7000:
		image4["bg"] = "blue"
	elif data4>=7000 and data4<7500:
		image4["bg"] = "navy"
	else:
		image4["bg"] = "purple"

	image1.place(x=80,y=250)
	image2.place(x=380,y=250)
	image3.place(x=680,y=250)
	image4.place(x=980,y=250)

	win.mainloop()