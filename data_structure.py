class myList:
    mylist = []
    def __init__(self):
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


class process_node:
    def __init__(self,name,Instances,xpos,ypos):
        self.name = name
        self.Instances = Instances
        self.xpos = xpos
        self.ypos = ypos
        print("Create node")


process_list = myList()
process1 = process_node("p1",2,50,50)
process_list.add_node(process1)
process_list.get_node("p1")
