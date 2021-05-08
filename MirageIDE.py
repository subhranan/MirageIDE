from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
comp = Tk()
comp.title('Mirage IDE')
#compiler.attributes("-fullscreen",True)
filepath=''
def setfilepath(path):
    global filepath
    filepath=path
def openf():
    path=askopenfilename(filetypes=[('Python Files','*py ')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        setfilepath(path)
def save_as():
    if filepath=='':
        path= asksaveasfilename(filetypes=[('Python Files','*py ')])
    else:
        path=filepath
    with open(path,'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        setfilepath(path)
def runit():
    if filepath=="":
        save_prompt= Toplevel()
        text = Label(save_prompt, text='YOU NEED TO SAVE YOUR CODE')
        text.pack()
        return
    command = f'python {filepath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
menubr=Menu(comp)
filebr=Menu(menubr,tearoff=0)
filebr.add_command(label='open',command=openf)
filebr.add_command(label='Save',command=save_as)
filebr.add_command(label='Save as',command=save_as)
filebr.add_command(label='Exit',command=exit)
menubr.add_cascade(label='File', menu=filebr)
runbr=Menu(menubr,tearoff=0)
runbr.add_command(label='Run',command=runit)
menubr.add_cascade(label='Run', menu=runbr)
comp.config(menu=menubr,bg='black')
editor=Text(bg='black', fg='#adff2f', insertbackground='red')
editor.pack(fill=BOTH, expand=1)
code_output=Text(height=7,bg='black', fg='red')
code_output.pack(fill=BOTH, expand=1)
comp.mainloop()