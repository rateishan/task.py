import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")
root.resizable(False, False)
root.iconbitmap('todo1.ico')

tasklist=[]

def add_task(event):
    task=task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open('tasks.txt', 'a') as file:
            file.write(f"{task}\n")
        list_box.insert(tk.END, task)
        tasklist.append(task)
     
            

def delete_item(event):
    selected_task=list_box.get(tk.ANCHOR)
    list_box.delete(tk.ANCHOR)
    tasklist.remove(selected_task)
    with open('tasks.txt', 'w') as file:
        for task in tasklist:
            file.write(f"{task}\n")

def open_task():
    with open('tasks.txt', 'r') as file:
        tasks=file.readlines()
        for task in tasks:
            if task !='\n':
                list_box.insert(tk.END,task)
                tasklist.append(task)

heading =ttk.Label(root, text="ISHAN TASKS", font="Arial 20 bold")
heading.pack(pady=15)

frame =ttk.Frame(root, width=400,height=50)
frame.pack(pady=10)

task_entry=ttk.Entry(frame, font='arial 14',width=30)
task_entry.pack()

task_entry.bind('<Return>', add_task)

frame1 =ttk.Frame(root, width=400,height=250)
frame1.pack(pady=10)

list_box=tk.Listbox(frame1, font='arial 12', width=40,height=16)
list_box.pack()

open_task()

delete_btn=ttk.Button(frame1, text="Delete Task", width=10)
delete_btn.pack(pady=15)

delete_btn.bind('<Return>', delete_item)



root.mainloop()
