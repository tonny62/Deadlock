from tkinter import *

global num_rect
num_rect = 0
global num_circle
num_circle = 0
class Application():
    def __init__(self,master):
        self.frame = Frame(master,width=400,height=400)
        self.create_gui()
        self.frame.pack()

    def create_gui(self):
        self.v = StringVar()
        # display_area label
        self.label1 = Label(self.frame,text="Display Area")
        self.label1.grid(row=1,column=1)
        #canvas area
        self.display_area = Canvas(self.frame,width=400,height=300,bg="#ECECEC")
        self.display_area.grid(column=1,row=2,rowspan=7,padx=5,pady=5)

        #Resource Area
        self.label2 = Label(self.frame,text="Resource Name")
        self.label3 = Label(self.frame,text="# of Instances")
        self.res_name = Entry(self.frame,textvariable=self.v)
        self.res_instance = Entry(self.frame)
        self.button_add_resource = Button(self.frame,text="Add Resource",command=self.add_rect)
        self.label2.grid(row=2,column=2)
        self.res_name.grid(row=2,column=3)
        self.label3.grid(row=3,column=2)
        self.res_instance.grid(row=3,column=3)
        self.button_add_resource.grid(row=4,column=2,sticky="E"+"W",columnspan=2)


        #Process area
        self.label4 = Label(self.frame,text="Process Name")
        self.process_name = Entry(self.frame)
        self.button_add_process = Button(self.frame,text="Add Process",command=self.add_circle)
        self.button_add_process.grid(row=6,column=2,sticky="E"+"W",columnspan=2)
        self.label4.grid(row=5,column=2)
        self.process_name.grid(row=5,column=3)

        #delete
        self.button_reset = Button(self.frame,text="Clear Screen",command=self.clear_canvas)
        self.button_reset.grid(row=7,column=2,sticky="E"+"W",columnspan=2)
    def add_rect(self):
        global num_rect
        s = self.v.get()
        x = 175
        y = 25 + num_rect*75

        text = self.display_area.create_text(x+60,y+25,text = s)
        coord = x,y,x+50,y,x+50,y+50,x+50,y+50,x,y+50
        res1 = self.display_area.create_polygon(coord,fill="blue")
        num_rect = num_rect+1

    def add_circle(self):
        global num_circle
        if(num_circle<=3):
            x=75
            y=12.5+num_circle*75
        else:
            x=275
            y=12.5+(num_circle-4)*75
        text = self.display_area.create_text(x+60,y+25,text = "P"+str(num_circle))
        coord = x,y,x+50,y+50
        res1 = self.display_area.create_oval(coord,fill="blue")
        num_circle = num_circle+1

    def clear_canvas(self):
        global num_circle
        global num_rect
        self.display_area.delete("all")
        num_circle = 0
        num_rect = 0


root = Tk()
app = Application(root)
root.mainloop()
