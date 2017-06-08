from tkinter import *
import time as t

global num_rect
num_rect = 0
global num_circle
num_circle = 0
global current_y
current_y = 12.5
global canvas_width
global canvas_height
canvas_height = 600
canvas_width = 800  # continue here
global process_list
global resource_list
global line_list


def do_noting(void):
    i = 0


def time_delay(time):
    start = t.time()
    now = t.time()
    while (now - start < time):
        do_noting
        now = t.time()

class Application():
    def __init__(self, master):
        self.frame = Frame(master, width=100, height=800)
        self.create_gui()
        self.frame.pack()
        self.object_list = []

    def create_gui(self):
        global process_list
        global resource_list
        self.v = StringVar()
        self.p = StringVar()
        self.num_ins = StringVar()
        self.om_variable1 = StringVar()
        self.om_variable2 = StringVar()
        self.om_variable3 = StringVar()
        self.om_variable4 = StringVar()
        self.del_variable1 = StringVar()
        self.del_variable2 = StringVar()
        self.del_variable3 = StringVar()
        self.del_variable4 = StringVar()
        self.processfrom_del = StringVar

        # display_area label
        self.label1 = Label(self.frame, text="Display Area")
        self.label1.grid(row=1, column=1)
        # canvas area
        self.display_area = Canvas(self.frame, width=canvas_width, height=canvas_height, bg="#ECECEC")
        self.display_area.grid(column=1, row=2, rowspan=15, padx=5, pady=5)

        # Resource Area
        self.Resource_frame = LabelFrame(self.frame, text="Resource")
        self.Resource_frame.grid(row=2, column=2)
        self.label2 = Label(self.Resource_frame, text="Resource Name")
        self.label3 = Label(self.Resource_frame, text="# of Instances")
        self.res_name = Entry(self.Resource_frame, textvariable=self.v)
        self.res_instance = Entry(self.Resource_frame, textvariable=self.num_ins);
        self.button_add_resource = Button(self.Resource_frame, text="Add Resource", command=self.add_rect)
        self.label2.grid(row=1, column=1)
        self.res_name.grid(row=1, column=2)
        self.label3.grid(row=2, column=1)
        self.res_instance.grid(row=2, column=2)
        self.button_add_resource.grid(row=3, column=1, sticky="E" + "W", columnspan=2)

        # Process area
        self.Process_frame = LabelFrame(self.frame, text="Process")
        self.Process_frame.grid(row=3, column=2)
        self.label4 = Label(self.Process_frame, text="Process Name")
        self.process_name = Entry(self.Process_frame, textvariable=self.p)
        self.button_add_process = Button(self.Process_frame, text="Add Process", command=self.add_circle)
        self.button_add_process.grid(row=2, column=1, sticky="E" + "W", columnspan=2)
        self.label4.grid(row=1, column=1)
        self.process_name.grid(row=1, column=2)

        # Request and allocation
        self.ReqAll_frame = LabelFrame(self.frame, text="Request and Allocate")
        self.ReqAll_frame.grid(row=4, column=2)
        # Request
        # From Process
        self.label_from = Label(self.ReqAll_frame, text="From")
        self.label_from.grid(row=1, column=1)
        self.processfrom = StringVar()
        self.om_variable1.set('Process')
        self.choices1 = [""]
        self.fromprocess = OptionMenu(self.ReqAll_frame, self.om_variable1, *self.choices1)
        self.fromprocess.grid(row=1, column=2)
        # To Resource
        self.label_to = Label(self.ReqAll_frame, text="To")
        self.label_to.grid(row=1, column=3)
        self.resto = StringVar()
        self.om_variable2.set('Resource')
        self.choices2 = [""]
        self.request_to = OptionMenu(self.ReqAll_frame, self.om_variable2, *self.choices2)
        self.request_to.grid(row=1, column=4)
        # add request button
        self.add_request = Button(self.ReqAll_frame, text="Add request",
                                  command=lambda: self.add_req_edge(self.om_variable1.get(), self.om_variable2.get()))
        self.add_request.grid(row=1, column=5)

        # Allocate
        # From Resource
        self.label_from = Label(self.ReqAll_frame, text="From")
        self.label_from.grid(row=2, column=1)
        self.resfrom = StringVar()
        self.om_variable3.set('Resource')
        self.fromres = OptionMenu(self.ReqAll_frame, self.om_variable3, *self.choices1)
        self.fromres.grid(row=2, column=2)
        # To Process
        self.label_to = Label(self.ReqAll_frame, text="To")
        self.label_to.grid(row=2, column=3)
        self.processto = StringVar()
        self.om_variable4.set('Process')
        self.process_to = OptionMenu(self.ReqAll_frame, self.om_variable4, *self.choices2)
        self.process_to.grid(row=2, column=4)
        # add request button
        self.add_allocate = Button(self.ReqAll_frame, text="Add Allocate",
                                   command=lambda: self.add_allocate_edge(self.om_variable3.get(),
                                                                          self.om_variable4.get()))
        self.add_allocate.grid(row=2, column=5)

        #  Banker Frame
        self.banker_frame = LabelFrame(self.frame, text="Banker's Algoritm Section")
        self.banker_frame.grid(row=5, column=2)
        self.button_banker = Button(self.banker_frame, text="Banker's", command=self.run_banker)
        self.button_banker.grid(row=1, column=2, sticky="E" + "W", columnspan=2)

        # Deleting edge frame
        self.delete_frame = LabelFrame(self.frame, text="Deleting Edge Section")
        self.delete_frame.grid(row=6, column=2)

        # Deleting Request
        # From Process
        self.label_from = Label(self.delete_frame, text="From")
        self.label_from.grid(row=1, column=1)
        self.del_variable1.set('Process')
        self.choices1 = [""]
        self.delfromprocess = OptionMenu(self.delete_frame, self.del_variable1, *self.choices1)
        self.delfromprocess.grid(row=1, column=2)
        # To Resource
        self.label_to = Label(self.delete_frame, text="To")
        self.label_to.grid(row=1, column=3)
        self.resto_del = StringVar()
        self.del_variable2.set('Resource')
        self.choices2 = [""]
        self.delrequest_to = OptionMenu(self.delete_frame, self.del_variable2, *self.choices2)
        self.delrequest_to.grid(row=1, column=4)
        # add request button
        self.delete_request = Button(self.delete_frame, text="Delete request",
                                     command=lambda: self.delete_req_edge(self.del_variable1.get(),
                                                                          self.del_variable2.get()))
        self.delete_request.grid(row=1, column=5)

        # Deleting Allocate
        # From Resource
        self.label_from = Label(self.delete_frame, text="From")
        self.label_from.grid(row=2, column=1)
        self.resfrom_del = StringVar()
        self.del_variable3.set('Resource')
        self.delfromres = OptionMenu(self.delete_frame, self.del_variable3, *self.choices1)
        self.delfromres.grid(row=2, column=2)
        # To Process
        self.label_to = Label(self.delete_frame, text="To")
        self.label_to.grid(row=2, column=3)
        self.processto_del = StringVar()
        self.del_variable4.set('Process')
        self.delprocess_to = OptionMenu(self.delete_frame, self.del_variable4, *self.choices2)
        self.delprocess_to.grid(row=2, column=4)
        # add request button
        self.del_allocate = Button(self.delete_frame, text="Add Allocate",
                                   command=lambda: self.add_allocate_edge(self.del_variable3.get(),
                                                                          self.del_variable4.get()))
        self.del_allocate.grid(row=2, column=5)

    def run_banker(self):
        banker(resource_list, process_list, request_list, allocate_list)

    def add_rect(self):  ## create resource node and append resource into resource_list
        global num_rect
        global current_y
        s = self.v.get()
        numins = self.num_ins.get()
        x = canvas_width / 2 - 25
        y = current_y
        if (s == ""):  ##generate resource name
            s = "R" + str(num_rect)
        if (numins == ""):  ## set normal instance to 1
            numins = "1"
        for i in range(int(numins)):
            coord = x, y, x + 50, y, x + 50, y + 50, x + 50, y + 50, x, y + 50
            cir_coord = x + 22, y + 22, x + 28, y + 28
            if (i == 0):
                text = self.display_area.create_text(x + 60, y + 25, text=s, anchor="nw")
            res1 = self.display_area.create_polygon(coord, fill="blue")

            self.display_area.create_oval(cir_coord, fill="black")
            y += 50
        current_y = y + 25
        resource_list.add_node(resource_node(s, x, y, numins))  ## create process node and append to resource_list
        num_rect += 1
        self.refresh_menu()
        print_vectors(resource_list, process_list, request_list, allocate_list)

    def add_circle(self):  ## create process node and append to process_list
        global num_circle
        if (num_circle < 8):
            x = canvas_width / 4 - 25
            y = 12.5 + num_circle * 75
        else:
            x = 3 * canvas_width / 4 - 25
            y = 12.5 + (num_circle - 9) * 75
        p = self.p.get()
        if (p == ""):
            p = "P" + str(num_circle)
        text = self.display_area.create_text(x + 60, y + 25, text=p, anchor="nw")
        coord = x, y, x + 50, y + 50
        res1 = self.display_area.create_oval(coord, fill="blue")
        process_list.add_node(process_node(p, x + 25, y + 25))  ## create process node and add to process_list
        num_circle += 1
        self.refresh_menu()
        print_vectors(resource_list, process_list, request_list, allocate_list)

    def add_req_edge(self, fromnode, tonode):
        # print("Creating Request")
        if ((num_rect != 0) and (num_circle != 0)):
            self.fromnode1 = process_list.get_node(str(fromnode))
            self.tonode1 = resource_list.get_node(str(tonode))
            x0 = self.fromnode1.xpos
            y0 = self.fromnode1.ypos
            x1 = self.tonode1.xpos
            y1 = self.tonode1.ypos
            obj = self.display_area.create_line(x0 + 25, y0, x1, y1 - 25, arrow=LAST)
            line_obj = line_object(x0, y0, x1, y1, self.fromnode1, self.tonode1, obj)
            print(obj)
            request_list.add_line(line_obj)
            print_vectors(resource_list, process_list, request_list, allocate_list)

    def delete_req_edge(self, fromnode, tonode):
        self.fromnode1 = process_list.get_node(str(fromnode))
        self.tonode1 = resource_list.get_node(str(tonode))
        line_obj = request_list.get_line(self.fromnode1, self.tonode1)
        request_list.linelist.remove(line_obj)
        print("deleting")
        self.display_area.delete(line_obj.obj)
        self.refresh_menu()

    def add_allocate_edge(self, fromnode, tonode):
        # print("Creating Allocate")
        if ((num_rect != 0) and (num_circle != 0)):
            self.fromnode1 = resource_list.get_node(str(fromnode))
            self.tonode1 = process_list.get_node(str(tonode))
            if (int(self.fromnode1.instance) > 1):
                y0 = self.fromnode1.ypos - 50 * (int(self.fromnode1.instance_left - 1))
            else:
                y0 = self.fromnode1.ypos
            x0 = self.fromnode1.xpos
            x1 = self.tonode1.xpos
            y1 = self.tonode1.ypos
            obj = self.display_area.create_line(x0 + 25, y0 - 25, x1 + 25, y1, arrow=LAST)
            line_obj = line_object(x0 + 25, y0 - 25, x1 + 25, y1, self.fromnode1, self.tonode1, obj)
            allocate_list.add_line(line_obj)
            self.fromnode1.instance_left -= 1;
            print_vectors(resource_list, process_list, request_list, allocate_list)

    def clear_canvas(self):
        global num_circle
        global num_rect
        global current_y
        self.display_area.delete("all")
        num_circle = 0
        num_rect = 0
        current_y = 25

    def draw_req_arrow(self, x0, y0, x1, y1):
        self.display_area.create_line(x0, y0, x1, y1, arrow=LAST)

    def refresh_menu(self):
        process_menu = self.fromprocess['menu']
        process_menu2 = self.process_to['menu']
        process_menu3 = self.delfromprocess['menu']
        process_menu4 = self.delprocess_to['menu']
        process_menu2.delete(0, "end")
        process_menu.delete(0, "end")
        process_menu3.delete(0, "end")
        process_menu4.delete(0, "end")
        for i in range(0, len(process_list.get_List())):
            value = process_list.get_node_name(i)
            process_menu.add_command(label=value, command=lambda v=value: self.om_variable1.set(v))
            process_menu2.add_command(label=value, command=lambda v=value: self.om_variable4.set(v))
            process_menu3.add_command(label=value, command=lambda v=value: self.del_variable1.set(v))
            process_menu4.add_command(label=value, command=lambda v=value: self.del_variable4.set(v))
        resource_menu2 = self.fromres['menu']
        resource_menu = self.request_to['menu']
        resource_menu3 = self.delrequest_to['menu']
        resource_menu4 = self.delfromres['menu']
        resource_menu.delete(0, "end")
        resource_menu2.delete(0, "end")
        resource_menu3.delete(0, "end")
        resource_menu4.delete(0, "end")
        for i in range(0, len(resource_list.get_List())):
            value = resource_list.get_node_name(i)
            resource_menu.add_command(label=value, command=lambda v=value: self.om_variable2.set(v))
            resource_menu2.add_command(label=value, command=lambda v=value: self.om_variable3.set(v))
            resource_menu3.add_command(label=value, command=lambda v=value: self.del_variable2.set(v))
            resource_menu4.add_command(label=value, command=lambda v=value: self.del_variable3.set(v))


class myList:
    mylist = []

    def __init__(self):
        self.mylist = []
        print("Create List")

    def add_node(self, node):
        self.mylist.append(node)
        # print("Add node at index:"+str(len(self.mylist)-1))

    def get_node(self, name):
        # print(str(name))
        for i in range(0, len(self.mylist)):
            if (str(name) == str(self.mylist[i].name)):
                # print("found node at " + str(i))
                return self.mylist[i]

    def get_List(self):
        return self.mylist

    def get_node_name(self, index):
        return self.mylist[index].name

    def print_list(self):
        for i in range(len(self.mylist)):
            print(str(self.mylist[i].xpos) + " ")



class process_node:
    name = ""
    xpos = 0
    ypos = 0

    def __init__(self, name, xpos, ypos):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        # print("Create process name: "+self.name +"At xpos:"+str(self.xpos)+" At ypos: "+str(self.ypos))


class resource_node:
    name = ""
    xpos = 0
    ypos = 0
    instance = 1
    instance_left = 0

    def __init__(self, name, xpos, ypos, instance):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.instance = int(instance)
        self.instance_left = int(instance)
        # print("Create resource name: "+self.name +" At xpos:"+str(self.xpos)+" At ypos: "+str(self.ypos)+" Instance: "+ str(self.instance))


class line_list:
    linelist = []

    def __init__(self):
        self.linelist = []
        print("Create Line list")

    def add_line(self, line):
        self.linelist.append(line)

    def get_line(self, fromnode, tonode):
        for i in range(len(self.linelist)):
            if (fromnode == self.linelist[i].fromnode and tonode == self.linelist[i].tonode):
                print(self.linelist[i].obj)
                return self.linelist[i]

        return 0

    def get_allocate(self, tonode, fromnode):
        count = 0
        for i in range(len(self.linelist)):
            if (self.linelist[i].tonode.name == tonode and self.linelist[i].fromnode.name == fromnode):
                count += 1
        return count


class line_object:
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    fromnode = ""
    tonode = ""
    obj = ""

    def __init__(self, x0, y0, x1, y1, fromnode, tonode, obj):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.fromnode = fromnode
        self.tonode = tonode
        self.obj = obj
        # print("Create Edge object from " + fromnode.name + " to " + tonode.name)


def print_vectors(resource_list, process_list, request_list, allocate_list):
    # print("Resource = ", end="")
    # for i in range(len(resource_list.mylist)):
    #     print(resource_list.mylist[i].name, end=" ")
    # print("")
    # print("Process = ", end="")
    # for i in range(len(process_list.mylist)):
    #     print(process_list.mylist[i].name, end=" ")
    # print()
    print(">>>>>>>>>>>>>>>>>>>>")
    print("Allocation")
    print("   ", end="")
    for i in range(len(resource_list.mylist)):
        print(resource_list.mylist[i].name, end=" ")
    print()
    for i in range(len(process_list.mylist)):
        print(process_list.mylist[i].name, end=" ")
        for j in range(len(resource_list.mylist)):
            print(allocate_list.get_allocate(process_list.mylist[i].name, resource_list.mylist[j].name), end="  ")
        print()
    print()

    print("Request")
    print("   ", end="")
    for i in range(len(resource_list.mylist)):
        print(resource_list.mylist[i].name, end=" ")
    print()
    for i in range(len(process_list.mylist)):
        print(process_list.mylist[i].name, end=" ")
        for j in range(len(resource_list.mylist)):
            print(request_list.get_allocate(resource_list.mylist[j].name, process_list.mylist[i].name), end="  ")
        print()
    print("<<<<<<<<<<<<<<<<<<<<")


class banker:
    request_matrix = []
    allocation_matrix = []

    available_matrix = []
    unavailable_matrix = []

    temp_vector = []
    instance_matrix = []

    finish_matrix = []
    sequence = []

    def __init__(self, resource_list, process_list, request_list, allocate_list):
        if (len(self.request_matrix) != 0):
            self.request_matrix = []
            self.allocation_matrix = []

            self.available_matrix = []
            self.unavailable_matrix = []

            self.temp_vector = []
            self.instance_matrix = []

            self.finish_matrix = []
            self.sequence = []
        for i in range(len(process_list.mylist)):
            for j in range(len(resource_list.mylist)):
                self.temp_vector.append(
                    request_list.get_allocate(resource_list.mylist[j].name, process_list.mylist[i].name))
            self.request_matrix.append(self.temp_vector)
            self.temp_vector = []
        for i in range(len(process_list.mylist)):
            for j in range(len(resource_list.mylist)):
                self.temp_vector.append(
                    allocate_list.get_allocate(process_list.mylist[i].name, resource_list.mylist[j].name))
            self.allocation_matrix.append(self.temp_vector)
            self.temp_vector = []
        for i in range(len(resource_list.mylist)):
            self.instance_matrix.append(resource_list.mylist[i].instance)
        for i in range(len(self.instance_matrix)):
            self.unavailable_matrix.append(0)
            self.available_matrix.append(0)
        for i in range(len(resource_list.mylist)):
            for j in range(len(process_list.mylist)):
                self.unavailable_matrix[i] += int(self.allocation_matrix[j][i])
        for i in range(len(self.instance_matrix)):
            self.available_matrix[i] = self.instance_matrix[i] - self.unavailable_matrix[i]

        self.print_matrix()
        self.run_banker()

    def create_finish_matrix(self):
        for i in range(len(self.request_matrix)):
            self.finish_matrix.append(False)

    def check_finish_process(self, available, request):
        for i in range(len(available)):
            if (not available[i] >= request[i]):
                return False
        return True

    def check_left_finish(self):
        count = 0
        for i in range(len(self.finish_matrix)):
            if (self.finish_matrix[i] == False):
                count += 1
        return count

    def sum_v2_to_v1(self, vector1, vector2):
        for i in range(len(vector1)):
            vector1[i] += vector2[i]

    def print_matrix(self):
        print("Request = ", end="")
        print(self.request_matrix)
        print("Allocate = ", end="")
        print(self.allocation_matrix)
        print("Total instance = ", end="")
        print(self.instance_matrix)
        print("Available = ", end="")
        print(self.available_matrix)
        print("Used = ", end="")
        print(self.unavailable_matrix)

    def run_banker(self):
        temp_request = self.request_matrix
        lentempnow = len(temp_request)
        lentempprev = len(temp_request)
        self.create_finish_matrix()
        while (len(temp_request) > 0):
            for i in range(len(temp_request)):
                # print(i, end=" ")
                # print(" Available ", end="")
                # print(self.available_matrix, end="")
                # print(" Request ", end="")
                # print(self.request_matrix[i])
                if (self.check_finish_process(self.available_matrix, self.request_matrix[i]) and (
                not self.finish_matrix[i])):
                    self.sum_v2_to_v1(self.available_matrix, self.allocation_matrix[i])
                    # print("Run " + str(i) + " now Available", end=" ")
                    # print(self.available_matrix)
                    self.finish_matrix[i] = True
                    self.sequence.append(i)
                if (self.check_left_finish() == 0):
                    break
            lentempprev = lentempnow
            lentempnow = self.check_left_finish()
            if (lentempnow == lentempprev):
                print("no more sequence")
                break
        # print("done banker")
        print(self.sequence)


resource_list = myList()
process_list = myList()
request_list = line_list()
allocate_list = line_list()

root = Tk()
app = Application(root)
root.mainloop()
