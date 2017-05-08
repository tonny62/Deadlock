import tkinter as tk
global num_rect = 0

def add_rect():
    global num_rect
    x = 175
    y = 25 + num_rect*75

    mytext = display_area.create_text(x+60,y+25,text = "R"+str(num_rect))
    coord = x,y,x+50,y,x+50,y+50,x+50,y+50,x,y+50
    res1 = display_area.create_polygon(coord,fill="blue")
    num_rect = num_rect+1

top = tk.Tk()

frame = tk.Frame(top,width = 400,height=300)
frame.pack_propagate(0)
##        frame.grid_propagate(0)
label1 = tk.Label(frame,text ="Display Area").grid(row=1,column=1)
display_area = tk.Canvas(frame,width=400,height=300,bg="#ECECEC")
display_area.grid(column=1,row=2,rowspan=7,padx=5,pady=5)

label2 = tk.Label(frame,text ="Name").grid(row=2,column=2)
res_name = tk.Entry(frame)
res_name.grid(row=2,column=3,padx=5)
label3 = tk.Label(frame,text = "instances").grid(row=3,column=2)
res_instance = tk.Entry(frame).grid(row=3,column=3,padx=5)

b_add_resource = tk.Button(frame, text="Add resource")
b_add_resource.grid(column=2,row=4,sticky="E"+"W",columnspan=2)

b_add_process = tk.Button(frame,text="Add process")
b_add_process.grid(column=2,row=5)

frame.pack()

top.mainloop()
