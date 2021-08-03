d={}
class Employee:
    def salary_slip(self,name,add,pan,deduct=0,basic=0):
        self.name=name
        self.add=add
        self.pan=pan
        self.basic=basic
        self.bonus=basic*2
        self.deduct=deduct
        netsal=self.basic+self.bonus-self.deduct
        return netsal
    def accept(self):
        name=input("Enter name:")
        add=input("Enter adress:")
        pan=input("panno:")
        basic=int(input("basic salary"))
        deduct=int(input("Deduct="))
        self.netsal=self.salary_slip(name,add,pan,deduct,basic)

    def display(self):
        print("name=",self.name)
        print("address=",self.add)
        print("pan=",self.pan)
        print("basic=",self.basic)
        print("deduct=",self.deduct)
        print("netsalary=",self.netsal)

    def search (self,name):
        for k,v in d.items():
            print(k,v)
            if k==name:
                v.display()

while True:
    print("1-insert data")
    print("2-display data")
    print("3-update dictionary")
    print("4-search data")
    print("0-exit")

    ch=int(input("enter your choice"))
    if ch==1:
        e1=Employee()
        e1.accept()
        
    if ch==2:
        e1.display()

    if ch==3:
        d.update({e1.name:e1})

    if ch==4:
        name=(input("Enter name: "))
        e1.search(name)
    
    if ch==0:
        break
