import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter.font import BOLD
from tkinter import END,CENTER
import pyperclip






def Run(text_entry,text_output,text_info):
    text_info.delete('1.0', END)
    text_output.delete('1.0', END)

    text=text_entry.get(1.0, END)
    if(text.strip()==''):
        try:
            text=pyperclip.paste()
            #text_entry.insert(1.0,text)
        except:
            text_info.insert(1.0,"Error! No valid input given!")



    lines=text.split('\n')
    dupes_removed = []
    dupes=0
    empty_lines=0
    for line in lines:
        if (line.strip()!=''):
            if (line not in dupes_removed):
                dupes_removed.append(line)
            else:
                dupes+=1
        else:
            empty_lines+=1
    out_text=''
    for item in dupes_removed:
        text_output.insert(1.0,item+'\n')
    
    pyperclip.copy(text_output.get(1.0, END))
    text_output.insert(1.0,out_text)
    
    text_info.insert(1.0,f"{dupes} Duplicate Lines Removed.\n{empty_lines} Empty Lines Removed\nOut of {len(lines)} Items\n{len(dupes_removed)} Lines Left\nOUTPUT copied to clipboard")
    text_entry.delete('1.0', END)

def main():
    root=tk.Tk()
    root.title('RMDupes')
    #photo = tk.PhotoImage(file = r"settings\icon.gif")
    #root.iconphoto(False, photo)
    root.geometry('1050x750')
    root.configure(bg='#635d5d')
    style = ttk.Style()
    comboboxstyle = ttk.Style()
    comboboxstyle.theme_create('combostyle', parent='clam', settings = {'TCombobox': 
                                                             {'configure': {'selectbackground': 'navajowhite',
                                                                            'fieldbackground': 'navajowhite',
                                                                            'background': 'white',
                                                                            'bordercolor':'black',
                                                                           'selectforeground': 'black'}}})

    style.theme_use('combostyle')
    label_entry=tk.Label(root,text=f'INPUT',font=('Helvetica',20,BOLD),bg='navajowhite')
    label_entry.grid(row=1,column=0,padx=(5,0),pady=(45,0))

    label_output=tk.Label(root,text=f'OUTPUT',font=('Helvetica',20,BOLD),bg='navajowhite')
    label_output.grid(row=1,column=1,padx=(5,0),pady=(45,0))

    text_entry = scrolledtext.ScrolledText(root,width=40,height=20,font=('Georgia 14'))
    text_entry.grid(row=2,column=0,pady=(10,10),padx=10)

    text_output = scrolledtext.ScrolledText(root,width=40,height=20,font=('Georgia 14'))
    text_output.grid(row=2,column=1,pady=(10,10),padx=10)

    text_info = scrolledtext.ScrolledText(root,width=28,height=5,font=('Georgia 18'))
    text_info.grid(row=3,column=1,pady=(10,10),padx=10)

    button_run=tk.Button(root,text='Run',font=('Helvetica',16,BOLD),height=1,width=30,bg='#ea6f04',command=lambda:Run(text_entry,text_output,text_info))
    button_run.configure(border='4')
    button_run.grid(row=3,column=0,pady=0,padx=5)
    

    root.mainloop()


    

main()