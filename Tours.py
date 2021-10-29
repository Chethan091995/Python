dest={1:["Mysore",100],2:["Chennai",350],3:["Goa",250],4:["Mangalore",300],5:["OOty",225],6:["Coorg",190],7:["Trivenderam",325],8:["Vizag",400]}
driver_bata=400
cabs={1:["Regular",12],2:["Semi Lux",18],3:["Luxury",22]}
from datetime import date
res=[]
class sample():
    #dest={"Mysore":100,"Chennai":350,"Goa":250,"Mangalore":300,"OOty":225,"Coorg":190,"Trivenderam":325,"Vizag":400}
    
    def cus(self):
        name=input("Enter your name")
        res.append(name)
        return name
    def destiny(self):
        
        
        for i in list(dest.keys()):
            print(i,dest[i][0])
        
        while 1:
            num=int(input("Enter your destination"))
            if num in dest.keys():
                res.append(dest[num][0])
                res.append(dest[num][1])
                break
            else:
                print("Enter the proper destination")
        
        return dest[num][0],dest[num][1]
    def way(self):
        print("Choose 1.One way 2.Two way")
        #choice=int(input("Enter your choice"))
        #n=0
        while 1:
            choice=int(input("Enter your choice"))
            
            if choice==1:
                res.append(1)
                print("Thanks for choosing one way")
                break
            elif choice==2:
                res.append(2)
                print("Thanks for choosing two way")
                break
            else:
                print("Enter proper choice")
                

            
            
        
    def prin(self):
        self.Place,self.Distance=self.destiny()
        print(self.Place,self.Distance," KMS for 1 side")

    
    

    def cabs_required(self):
        for j in list(cabs.keys()):
            print(j,cabs[j][0])
        while 1:
            cab_num=int(input("Choose the cab as numbers"))
            if cab_num in cabs.keys():
                #res.append(cabs[cab_num][0])
                #res.append(cabs[cab_num][1])
                return cabs[cab_num][0],cabs[cab_num][1]
            else:
                print("Enter the valid number")
        print("Enter 1.One way 2.Two way")
        
        
    def prin_cabs(self):
        self.Cab_v,self.Price=self.cabs_required()
        res.append(self.Cab_v)
        res.append(self.Price)
        print(self.Cab_v, self.Price ,"Per km")
    def num_days(self):
            #s_year=int(input("Enter year"))
        if res[3]==2:
            print("Enter the starting date")
            s_day=int(input("Enter date"))
            s_month=int(input("Enter month"))
            self.date1=date(2021,s_month,s_day)
   
            #e_year=int(input("Enter year"))
            print("Enter returning date")
            e_day=int(input("Enter date"))
            e_month=int(input("Enter month"))
            self.date2=date(2021,e_month,e_day)
            #res.append((date2-date1).days)
            return (self.date2-self.date1).days
        else:
            print("Enter the starting date")
            s_day=int(input("Enter date"))
            s_month=int(input("Enter month"))
            self.date1=date(2021,s_month,s_day)
            return 1
            #res.append(1)
            
    def prin_days(self):
        
            
        self.days=self.num_days()
        res.append(self.days)
        print("Number of days : ",self.days)
        
            
    def result(self):
        
        n=12
        self.cus()
        self.prin()
        self.way()
        self.prin_days()
        self.prin_cabs()
            
             
        
        sum=0
        print("******************************VRL TRavels****************************************")
        print("Bill number:" ,n,"\n")
        print("*********************************************************************************")
        print("Customer Name               : ", res[0],"\n")
        print("Destiny                     : ", res[1] )
        print("One /Two way                : " ,res[3])
        print("Total distance              : ", res[2]*res[3])
        if res[3]==2:
            
            print("Number of days              : ",res[4],"days starting from ",self.date1 ,"ending ",self.date2)
        else:
            print("Number of days              : ",res[4],"day on ",self.date1)
        print("Extra charges per day is 1000")
        if res[3]>1:
            
            print("Total extra chrages          : ", 1000*(res[4]),"Rupees")
            sum+=1000*(res[4])
        else:
            sum+=1000
        
        print("Driver Bata per day is 400 rupees")
        if res[4]>1:
            print("Total driver chrages        : ", res[4]*400, "Rupees")
            sum=sum+400*res[4]
        else:
            sum=sum+400
            
        print("Cab selected                : ",res[-2])
        print("Total cab chrage            : ",float(res[-1]*res[3]*res[2])," Rupees")
        if res[3]==2:
            print("10 % discount               : ",round(float(0.1*res[-1]*res[3]*res[2]),2)," Rupees")
            print("Cab charge after deduction  : ",(res[2]*res[3]*res[-1])-round(float((0.1*res[-1]*res[2]*res[3])),2)," Rupees")
            sum+=round(float(res[-1]*res[2]*res[3]),2)-round(float(0.1*res[-1]*res[2]*res[3]),2)
        else:
            sum+=res[-1]*res[3]*res[2]
            
        
        print("GST  15%                    :", float(0.15*sum)," Rupees")
        print("Grand Total                 :", sum+float(0.15*sum)," Ruppes")
        
        print("\n***********************Thank You, Visit Again******************************************")
        n+=3
        
        

a=sample()

a.result()
