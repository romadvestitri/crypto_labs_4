from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import lab4 as cryp

loadpath = '' 
class Win:

	def sign_file(self):
		filename = askopenfilename()
		if filename:
			loadpath = filename
		else:
			messagebox.showwarning("Key error", "Cannot to open file")
		self.textFieldOut.delete(1.0, END)
		
		try:
			q = int(self.textKey.get())
			p = int(self.textP.get())
			h = int(self.textH.get())
			x = int(self.textX.get())
			k = int(self.textK.get())
			cryp.check_keys(q, p, h, x, k)
			if loadpath == "":
				messagebox.showwarning("Key error", "Choose file")
			else:
				result = cryp.create_file_signature(loadpath, q, p, h, x, k)
				self.textFieldIn.delete(1.0, END)
				self.textFieldIn.insert(1.0, cryp.read_file(loadpath))
				self.textFieldOut.delete(1.0, END)
				self.textFieldOut.insert(1.0, cryp.read_file(result[3]))

				out_str = f"Hash is - {result[2]}\nSignature1 is - {result[0]}\nSignature2 is - {result[1]}"
				self.textFieldOutData.delete(1.0, END)
				self.textFieldOutData.insert(1.0, out_str)

		except ValueError as err:
			messagebox.showwarning("Key error", str(err))

		


	def check_file(self):
		filename = askopenfilename()
		if filename:
			loadpath = filename
		else:
			messagebox.showwarning("Key error", "Cannot to open file")
		self.textFieldOut.delete(1.0, END)
	
		try:
			q = int(self.textKey.get())
			p = int(self.textP.get())
			h = int(self.textH.get())
			x = int(self.textX.get())
			k = int(self.textK.get())
			cryp.check_keys(q, p, h, x, k)
			if loadpath == "":
				messagebox.showwarning("Key error", "Choose file")
			else:
				result = cryp.check_file_signature(loadpath, q, p, h, x)
				self.textFieldIn.delete(1.0, END)
				self.textFieldIn.insert(1.0, cryp.read_file(loadpath))
				#self.textFieldOut.delete(1.0, END)
				#self.textFieldOut.insert(1.0, cryp.read_file(result[3]))
				if result[0] == result[1]:
					out_str = f"Hash is - {result[2]}\nr is - {result[0]}\nv is - {result[1]}\nfile is correct"
				else:
					out_str = f"Hash is - {result[2]}\nr is - {result[0]}\nv is - {result[1]}\nfile is not correct"
				self.textFieldOutData.delete(1.0, END)
				self.textFieldOutData.insert(1.0, out_str)

		except ValueError as err:
			messagebox.showwarning("Key error", str(err))

	def clear(self):
		self.textFieldIn.delete(1.0, END)
		self.textFieldOut.delete(1.0, END)
		self.textFieldOutData.delete(1.0, END)


	def __init__(self, width, height, title='Cipher'):
		self.color = '#c0c0c0'

		self.root = Tk()
		self.root['bg'] = self.color  # цвет фона
		self.root.title(title)
		self.root.geometry(f'{width}x{height}')

		self.frame = Frame(self.root, bg=self.color)  # frame fot textFiledIn
		self.frame1 = Frame(self.root, bg=self.color)
		self.frame2 = Frame(self.root, bg=self.color)


		self.entryFrame = Frame(self.root, bg=self.color)
		self.entryFrame1 = Frame(self.root, bg=self.color)
		self.entryFrame2 = Frame(self.root, bg=self.color)
		self.entryFrame3 = Frame(self.root, bg=self.color)
		self.entryFrame4 = Frame(self.root, bg=self.color)

		self.txtFrame = Frame(self.root, bg=self.color)
		self.txtFrame1 = Frame(self.root, bg=self.color)
		self.txtFrame2 = Frame(self.root, bg=self.color)
		self.txtFrame3 = Frame(self.root, bg=self.color)
		self.txtFrame4 = Frame(self.root, bg=self.color)
		self.txtFrame5 = Frame(self.root, bg=self.color)
		self.txtFrame6 = Frame(self.root, bg=self.color)
		self.txtFrame7 = Frame(self.root, bg=self.color)

		
		self.btnFrame = Frame(self.root, bg=self.color)
		self.btnFrame1 = Frame(self.root, bg=self.color)
		self.btnFrame2 = Frame(self.root, bg=self.color)

		self.textFieldIn = Text(self.frame, height=30, width=35, font='Consolas 15', wrap=WORD)
		self.textFieldOut = Text(self.frame1, height=30, width=35, font='Consolas 15', wrap=WORD)
		self.textFieldOutData = Text(self.frame2, height=30, width=35, font='Consolas 15', wrap=WORD)
		self.textKey = Entry(self.entryFrame,  font='Consolas 15')
		self.textP = Entry(self.entryFrame1,  font='Consolas 15')
		self.textH = Entry(self.entryFrame2,  font='Consolas 15')
		self.textX = Entry(self.entryFrame3,  font='Consolas 15')
		self.textK = Entry(self.entryFrame4,  font='Consolas 15')

		self.lblTextIn = Label(self.txtFrame, text='Plain File', font="Cosolas 20", bg=self.color, fg='black')
		self.lblTextOut = Label(self.txtFrame1, text='Ciphed File', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey = Label(self.txtFrame2, text='q', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey1 = Label(self.txtFrame3, text='p', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey2 = Label(self.txtFrame4, text='h', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey3 = Label(self.txtFrame5, text='x', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey4 = Label(self.txtFrame6, text='k', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey5 = Label(self.txtFrame7, text='Out Data', font="Cosolas 20", bg=self.color, fg='black')
		

		self.btnEcnrypt = Button(self.btnFrame, height=2, width=8, text="Sign", font="Consalas 20",
								 command=self.sign_file)
		self.btnDecrypt = Button(self.btnFrame1, height=2, width=8, text="Check", font="Consalas 20",
								 command=self.check_file)
		self.btnLoadFile = Button(self.btnFrame2, height=2, width=8, text="Clear", font="Consalas 20",
								  command=self.clear)
		
		

	def draw_win(self):
		self.txtFrame.place(x=70, y=20, width=200, height=30)
		self.txtFrame1.place(x=400, y=20, width=200, height=30)
		self.txtFrame2.place(x=700, y=20, width=200, height=30)
		self.txtFrame3.place(x=700, y=90, width=200, height=30)
		self.txtFrame4.place(x=700, y=160, width=200, height=30)
		self.txtFrame5.place(x=700, y=230, width=200, height=30)
		self.txtFrame6.place(x=700, y=300, width=200, height=30)
		self.txtFrame7.place(x=380, y=420, width=200, height=30)
		
		self.frame.place(x=25, y=50, width=300, height=350)
		self.frame1.place(x=355, y=50, width=300, height=350)
		self.frame2.place(x=380, y=460, width=300, height=200)

		self.entryFrame.place(x=695, y=50, width=300, height=30)
		self.entryFrame1.place(x=695, y=120, width=300, height=30)
		self.entryFrame2.place(x=695, y=190, width=300, height=30)
		self.entryFrame3.place(x=695, y=260, width=300, height=30)
		self.entryFrame4.place(x=695, y=330, width=300, height=30)

		self.btnFrame.place(x=25, y=420, width=90, height=50)
		self.btnFrame1.place(x=140, y=420, width=90, height=50)
		self.btnFrame2.place(x=255, y=420, width=90, height=50)

		self.textFieldIn.pack()
		self.textFieldOut.pack()
		self.textFieldOutData.pack()
		self.textKey.pack()
		self.textP.pack()
		self.textH.pack()
		self.textX.pack()
		self.textK.pack()
		

		self.lblTextIn.pack()
		self.lblTextOut.pack()
		self.lblKey.pack()
		self.lblKey1.pack()
		self.lblKey2.pack()
		self.lblKey3.pack()
		self.lblKey4.pack()
		self.lblKey5.pack()
		
		self.btnEcnrypt.pack()
		self.btnDecrypt.pack()
		self.btnLoadFile.pack()
		



	def run(self):  # запуск стартового окна
		self.draw_win()
		self.root.mainloop()


window = Win(1000, 700)
window.run()