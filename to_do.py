import tkinter as tk
import sqlite3

current_id = 0

def main():
    #initializes the SQL table that will store the needed tasks
    conn = sqlite3.connect("to_do.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS toDoList(Id INT, Task TEXT)")
    conn.commit()
        
    def addToList():
        item = txt_field.get()
        txt_field.delete(0, 'end')
        global current_id
        current_id += 1
        c.execute("INSERT INTO toDoList (Id, Task) VALUES (?, ?)", (current_id, item))
        conn.commit()
        c.execute("SELECT Task FROM toDoList ORDER BY id DESC LIMIT 1")
        displayToDoList()
    def addToListEnter(e):
        item = txt_field.get()
        txt_field.delete(0, 'end')
        global current_id
        current_id += 1
        c.execute("INSERT INTO toDoList (Id, Task) VALUES (?, ?)", (current_id, item))
        conn.commit()
        c.execute("SELECT Task FROM toDoList ORDER BY id DESC LIMIT 1")
        displayToDoList()
 
    def displayToDoList():
        c.execute('SELECT Id, Task FROM toDoList')
        result = ""
        global current_id
        for row in c:
            result += "Task "+str(row[0]) +": " + row[1] + "\n"
        lbl_list.config(text=result,justify="left")
        
    def clearToDoList():
        c.execute('DELETE FROM toDoList')
        conn.commit()
        lbl_list.config(text="")
        global current_id
        current_id = 0
    
    def deleteRecent():
        c.execute('DELETE FROM toDoList WHERE id = (SELECT MAX(id) FROM toDoList)')
        conn.commit()
        displayToDoList()
        global current_id
        if current_id > 0:
            current_id += -1
    def deleteFirst():
        c.execute('DELETE FROM toDoList WHERE id = (SELECT MIN(id) FROM toDoList)')
        conn.commit()
        displayToDoList()
        global current_id
        if current_id > 0:
            current_id += -1

    #create basic layout of application
    window = tk.Tk()
    window.geometry("500x800+1200+50")
    window.title("To-Do List")
    
    #frame layout
    frameTop = tk.Frame(master=window, height = 300,bg='#e4d7d3')
    frameBottom = tk.Frame(master=window,bg='#b8b2b0')
    window.bind('<Return>',addToListEnter)
    window.resizable(False, False)
    
    #list layout
    lbl_list = tk.Label(master=frameTop, text="Placeholder List",anchor="n",font=("Arial", 14),bg='#e4d7d3')
    lbl_list.pack(anchor="w",padx=5,pady=5)
    
    #Data entry layout
    lbl_prompt = tk.Label(master=frameBottom, text="Enter new item into list:",font=("Arial"),bg='#b8b2b0')
    txt_field = tk.Entry(master=frameBottom,font=("Arial"),width=10)
    btn_addButton = tk.Button(master=frameBottom,text= "Enter into list",command=addToList,font=("Arial"),bg='lightgreen', fg='black')
    btn_clearButton = tk.Button(master=frameBottom,text= "Clear List",command=clearToDoList,font=("Arial"),bg='#e68e74', fg='black')
    btn_deleteButton = tk.Button(master=frameBottom,text= "Delete Last",command=deleteRecent,font=("Arial"),bg='#e68e74', fg='black')
    btn_deleteButtonFirst = tk.Button(master=frameBottom,text= "Delete First",command=deleteFirst,font=("Arial"),bg='#e68e74', fg='black')

    frameBottom.columnconfigure(0, weight=1)
    frameBottom.columnconfigure(1, weight=1)
    frameBottom.columnconfigure(2, weight=1)
    frameBottom.columnconfigure(3, weight=1)

    lbl_prompt.grid(row=0, column=0, padx=20, pady=10)
    txt_field.grid(row=0, column=1, padx=20, pady=10)
    btn_addButton.grid(row=0, column=2, padx=20, pady=10)
    btn_clearButton.grid(row=1, column=0, padx=20, pady=10)
    btn_deleteButton.grid(row=1, column=1, padx=20, pady=10)
    btn_deleteButtonFirst.grid(row=1, column=2, padx=20, pady=10)
    
    frameTop.pack(fill=tk.BOTH,expand=True,side="top")
    frameBottom.pack(fill=tk.BOTH,expand=False)
    
    frameBottom.pack_forget()
    frameBottom.place(x=0, y=700, width=500, height=300)

    displayToDoList()
    window.mainloop()

    
if __name__ == "__main__": 
    main()
    
    
