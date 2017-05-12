from tkinter import *

global num_rect
num_rect = 0
global num_circle
num_circle = 0
global current_y
current_y = 12.5
global canvas_width
global canvas_height
canvas_height = 600
canvas_width = 800 #continue here


class Application():

    def __init__(self,master):
        self.frame = Frame(master,width=100,height=800)
        self.create_gui()
        self.frame.pack()

    def create_gui(self):
        self.v = StringVar()
        self.num_ins =StringVar()
        # display_area label
        self.label1 = Label(self.frame,text="Display Area")
        self.label1.grid(row=1,column=1)
        #canvas area
        self.display_area = Canvas(self.frame,width=canvas_width,height=canvas_height,bg="#ECECEC")
        self.display_area.grid(column=1,row=2,rowspan=10,padx=5,pady=5)

        #Resource Area
        self.Resource_frame = LabelFrame(self.frame,text="Resource")
        self.Resource_frame.grid(row=2,column=2)
        self.label2 = Label(self.Resource_frame,text="Resource Name")
        self.label3 = Label(self.Resource_frame,text="# of Instances")
        self.res_name = Entry(self.Resource_frame,textvariable=self.v)
        self.res_instance = Entry(self.Resource_frame,textvariable=self.num_ins);
        self.button_add_resource = Button(self.Resource_frame,text="Add Resource",command=self.add_rect)
        self.label2.grid(row=1,column=1)
        self.res_name.grid(row=1,column=2)
        self.label3.grid(row=2,column=1)
        self.res_instance.grid(row=2,column=2)
        self.button_add_resource.grid(row=3,column=1,sticky="E"+"W",columnspan=2)


        #Process area
        self.Process_frame = LabelFrame(self.frame,text="Process")
        self.Process_frame.grid(row=3,column=2)
        self.label4 = Label(self.Process_frame,text="Process Name")
        self.process_name = Entry(self.Process_frame)
        self.button_add_process = Button(self.Process_frame,text="Add Process",command=self.add_circle)
        self.button_add_process.grid(row=2,column=1,sticky="E"+"W",columnspan=2)
        self.label4.grid(row=1,column=1)
        self.process_name.grid(row=1,column=2)

        #Request and allocation
        self.ReqAll_frame = LabelFrame(self.frame,text="Request and Allocate")
        self.ReqAll_frame.grid(row=4,column=2)
        #From Process
        self.label_from = Label(self.ReqAll_frame,text="From")
        self.label_from.grid(row=1,column=1)
        self.processfrom = StringVar()
        self.processfrom.set('red')
        self.choices1 = ['red', 'green', 'blue', 'yellow','white', 'magenta']
        self.fromprocess = OptionMenu(self.ReqAll_frame, self.processfrom, *self.choices1)
        self.fromprocess.grid(row=1,column=2)
        #To Resource
        self.label_to = Label(self.ReqAll_frame,text="To")
        self.label_to.grid(row=1,column=3)
        self.resto = StringVar()
        self.resto.set('red')
        self.choices2 = ['red', 'green', 'blue', 'yellow','white', 'magenta']
        self.request_to = OptionMenu(self.ReqAll_frame, self.resto, *self.choices2)
        self.request_to.grid(row=1,column=4)
        #add request button
        self.add_request = Button(self.ReqAll_frame,text="Add request")
        self.add_request.grid(row=1,column=5)


        #delete
        self.button_reset = Button(self.frame,text="Clear Screen",command=self.clear_canvas)
        self.button_reset.grid(row=8,column=2,sticky="E"+"W",columnspan=2)

    def add_rect(self):
        global num_rect
        global current_y
        s = self.v.get()
        numins =self.num_ins.get()
        x = canvas_width/2 - 25
        y = current_y
        if(s == ""):
            s = "R"+ str(num_rect)
        if(numins ==""):
            numins = "1"
        for i in range(int(numins)):
            coord = x,y,x+50,y,x+50,y+50,x+50,y+50,x,y+50
            cir_coord = x+22,y+22,x+28,y+28
            if(i==0):
                text = self.display_area.create_text(x+60,y+25,text = s,anchor = "nw")
            res1 = self.display_area.create_polygon(coord,fill="blue")

            self.display_area.create_oval(cir_coord,fill="black")
            y+=50
        current_y = y + 25
        num_rect+=1

    def add_circle(self):
        global num_circle
        if(num_circle<8):
            x=canvas_width/4 - 25
            y=12.5+num_circle*75
        else:
            x=3*canvas_width/4 - 25
            y=12.5+(num_circle-9)*75
        text = self.display_area.create_text(x+60,y+25,text = "P"+str(num_circle),anchor="nw")
        coord = x,y,x+50,y+50
        res1 = self.display_area.create_oval(coord,fill="blue")
        num_circle = num_circle+1

    def clear_canvas(self):
        global num_circle
        global num_rect
        global current_y
        self.display_area.delete("all")
        num_circle = 0
        num_rect = 0
        current_y =25

    def draw_arrow(x0,y0,x1,y1):
        self.display_area.create_line(x0,y0,x1,y1)



root = Tk()
app = Application(root)
root.mainloop()
