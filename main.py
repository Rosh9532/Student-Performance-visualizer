from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

root = Tk()
root.geometry("500x500+400+400")
root.title("Performance visualizer")

def f1():
	try:
		subjects=[]
		marks=[]
		name = ent_name.get()
		
		subject1 = (ent_subject.get())
		mark1 = (ent_subjectmark.get())
		subject = [(item) for item in subject1.split()]
		marks = [int(item) for item in mark1.split()]	
		

		plt.plot(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
		
		plt.bar(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
       
		plt.pie(marks, labels=subject, autopct='%.2f%%', shadow=True)
		plt.show()
	
	except ValueError:
		showerror("Mistake",'invalid marks')
		ent_subject.delet(0, END)
		ent_subjectmark.delet(0, END)
		
		ent_subject.focus()
	

	

f = ('Calibri', 20, 'bold')
lbl_name = Label(root, text="Name Of Student", font=f,)
ent_name = Entry(root, bd=5, font=f)
lbl_subject=Label(root, text="Enter Subjects separated by space", font=f,)
ent_subject=Entry(root, bd=5, font=f)
lbl_subjectmark=Label(root, text="Enter Marks of corresponding Subjects separated by space", font=f,)
ent_subjectmark=Entry(root, bd=5, font=f)

lbl_name.pack(pady=3)
ent_name.pack(pady=3)
lbl_subject.pack(pady=3)
ent_subject.pack(pady=3)
lbl_subjectmark.pack(pady=3)
ent_subjectmark.pack(pady=3)


btn_line = Button(root, text="Result Analysis", font=f, width=15, command=f1).pack(pady=10)


root.mainloop()