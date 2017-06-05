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
global process_list

class Application():

    def __init__(self,master):
        self.frame = Frame(master,width=100,height=800)
        self.create_gui()
        self.frame.pack()

    def create_gui(self):
        global process_list
        self.v = StringVar()
        self.p = StringVar()
        self.num_ins =StringVar()
        self.om_variable1 = StringVar()
        self.om_variable2 = StringVar()
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
        self.process_name = Entry(self.Process_frame,textvariable=self.p)
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
        self.om_variable1.set('Process')
        self.choices1 = [""]
        self.fromprocess = OptionMenu(self.ReqAll_frame, self.om_variable1, *self.choices1)
        self.fromprocess.grid(row=1,column=2)
        #To Resource
        self.label_to = Label(self.ReqAll_frame,text="To")
        self.label_to.grid(row=1,column=3)
        self.resto = StringVar()
        self.om_variable2.set('Resource')
        self.choices2 = [""]
        self.request_to = OptionMenu(self.ReqAll_frame, self.om_variable2, *self.choices2)
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
        resource_list.add_node(resource_node(s,x,y,numins))
        num_rect+=1
        self.refresh_menu()

    def add_circle(self):
        global num_circle
        if(num_circle<8):
            x=canvas_width/4 - 25
            y=12.5+num_circle*75
        else:
            x=3*canvas_width/4 - 25
            y=12.5+(num_circle-9)*75
        p=self.p.get()
        if(p == ""):
            p = "P"+ str(num_circle)
        text = self.display_area.create_text(x+60,y+25,text = p,anchor="nw")
        coord = x,y,x+50,y+50
        res1 = self.display_area.create_oval(coord,fill="blue")
        process_list.add_node(process_node(p,x+25,y+25))    ## create process node and add to process_list
        num_circle+=1
        self.refresh_menu()


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

    def refresh_menu(self):
        process_menu = self.fromprocess['menu']
        process_menu.delete(0,"end")
        for i in range(0,len(process_list.get_List())):
            value = process_list.get_node_name(i)
            process_menu.add_command(label=value, command=lambda v=value: self.om_variable1.set(v))
        resource_menu = self.request_to['menu']
        resource_menu.delete(0,"end")
        for i in range(0,len(resource_list.get_List())):
            value = resource_list.get_node_name(i)
            resource_menu.add_command(label=value, command=lambda v=value: self.om_variable2.set(v))

class myList:
    def __init__(self):
        self.mylist =[]
        print("Create List")

    def add_node(self,node):
        self.mylist.append(node)
        print("Add node at index:"+str(len(self.mylist)-1))

    def get_node(self,name):
        i = 0
        for node in self.mylist:
            i+=1
            if(node.name==name):
                print(str(i))
            else:
                print("No node found")
    def get_List(self):
        return self.mylist
    def get_node_name(self,index):
        return self.mylist[index].name

class process_node:
    name = ""
    xpos = 0
    ypos = 0
    def __init__(self,name,xpos,ypos):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        print("Create process name: "+self.name +"At xpos:"+str(self.xpos)+" At ypos: "+str(self.ypos))

class resource_node:
     name=""
     xpos=0
     ypos=0
     instance=1
     def __init__(self,name,xpos,ypos,instance):
         self.name = name
         self.xpos = xpos
         self.ypos = ypos
         self.instance = instance
         print("Create resource name: "+self.name +" At xpos:"+str(self.xpos)+" At ypos: "+str(self.ypos)+" Instance: "+ str(self.instance))

resource_list = myList()
process_list = myList()
root = Tk()
app = Application(root)
root.mainloop()
