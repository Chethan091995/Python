import json
from prettytable import PrettyTable
from datetime import *
import random
from tabulate import *

"""
id_items_price={1:['DOSA',20],2:['Masala_Dosa',40],3:['Vegitable_pallav',40],4:['Pongal',50],5:['Bisi_Bele_Bath',70],6:['Kaara_Bath',40],7:['Poori',40],8:['Vada',30],9:['Chapathi',35],10:['Lemon_Rice',30]}


with open('item_price_per_plate.json','a+') as file:
    json.dump(id_items_price,file,indent=1)
"""

class hotel_order_bill:
    
    Hotel_name='New Shanthi Sagar'
    
    bill_no=1524
    
    table=set()
    
    gst=15
    
    containers_charge=20
    
    food_items={'items':[]}
    
    order_details={'orders':[('date','bill_no','total_quantity','GST_AMT','Total_Paid_Amount','parcel_choice')]}
    
    
    with open('item_price_per_plate.json') as file:
        id_items_price=json.load(file)
    
    def menu_card(self):
        
        print('!--------------The Menu Card--------------!',end='\n\n')
        
        x = PrettyTable()
        x.field_names=['Item.ID','Item per plate','price in INR']
        
        for i,j in self.id_items_price.items():
            x.add_row([i, j[0],j[1]])
        
        print(x)
        
    
    def date_time(self):
        
        return datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M:%S %p')
    
    def bill_number(self):
        
        self.bill_no+=3
        
        return self.bill_no
        
        
        
    def order(self):
        
        while True:
            self.item_id=input('Enter Item Id of what item you want : ')
            #print(self.id_items_price)
            if self.item_id in self.id_items_price.keys() and self.item_id.isdigit():
                return self.item_id
            else:
                print('Please select valid item id ')
                
        
    def qua_ntity(self,quantity=1):
        
        try:
            self.quantity=int(input('Enter the quantity of the item :'))
        except ValueError:
            self.quantity=quantity
        
        return abs(self.quantity)
    
    def price_c(self):
        
        item_id=self.order()
        quantity=self.qua_ntity()
        
        self.price=self.id_items_price[item_id][1]*quantity
        
        self.item_name=self.id_items_price[item_id][0]
        
        self.food_items['items'].append((item_id,self.item_name,self.quantity,self.price))
        
        
    def total_amount_order(self): 
        
        parcel_choice=self.container_charge()
        
        items=self.food_items['items']
        
        if parcel_choice==1:
            
            self.total=sum(list(map(lambda x : x[-1],items)))
            self.totalqun=sum(list(map(lambda x : x[2],items)))
        else:
            
            self.total=sum(list(map(lambda x : x[-1],items)))+self.containers_charge
            self.totalqun=sum(list(map(lambda x : x[2],items)))+1
        
        gst_amt=(self.total*self.gst)/100
        
        self.twg=self.total+gst_amt
        
        #self.totalqun=sum(list(map(lambda x : x[2],items)))
        
        return self.totalqun,self.total,gst_amt,self.twg,parcel_choice
    
    def table_no(self):
        
        while True:
            self.t_no=random.randint(1,20)
            
            if self.t_no not in self.table:
                self.table.add(self.t_no)
                if len(self.table)==20:
                    self.table.clear()
                return self.t_no
    
    def waiter_no(self):
        
        return random.randint(1,20)
    
    def container_charge(self,charge=1):
        
        print('1. Having here 2. Take away')
        
        try :
            self.charge=int(input('Enter the above options : '))
            
        except ValueError:
            
            self.charge=1
            
        return self.charge
               
        
    
    def display(self):
        
        self.sl_no=0
        
        date=self.date_time()
        
        bill_no=self.bill_number()
        
        total_qun,total,gst_amt,twg,parcel_choice=self.total_amount_order()
        
        print('!---------------------Item_Bill------------------------!',end='\n\n')
                
                
        print('Hotel : {}'.format(self.Hotel_name),end='\n\n')
        print('Date and Time: {}'.format(date),end='\n\n')
        print('Bill_number : {}'.format(bill_no),end='\n\n')
        
        if parcel_choice==1:
            print('Table_number :{}'.format(self.table_no()),end='\n\n')
            print('waiter_number :{}'.format(self.waiter_no()),end='\n\n')
            
        self.order_details['orders'].append((date,bill_no,total_qun,gst_amt,twg,parcel_choice))
                
        x = PrettyTable()
        x.field_names=['sl.no','Item_ID','Item_name','quantity','Price INR']
        
        for i in self.food_items['items']:
            self.sl_no+=1
            x.add_row([self.sl_no,i[0],i[1],abs(i[2]),i[3]])

        
        if parcel_choice==1:
            
            print(x)
            
        else:
            x.add_row([self.sl_no+1,'','Container_charge','1',self.containers_charge])
            print(x)

        
        
        
        x=[['Total_quantities        :',abs(self.totalqun)],
        ['Total_amount_before_Tax :INR',self.total],
        ['GST                     :INR',gst_amt],
        ['Amount_to_be_paid       :INR',twg]]
            
        print(tabulate(x),end='\n\n\n\n')
        
        self.food_items['items'].clear()
        
        print('!--------------------------THANK YOU-----------------------------!')

        
    def customer_order(self):
        
        #self.menu_card()
        
        while True:
            
            try :
                
                self.add_items=input('Enter O to order and B for Billing :')[0].upper()
                
                if self.add_items=='O' and self.add_items.isalpha():
                    
                    self.price_c()
                
                elif self.add_items=='B' and self.add_items.isalpha():
                    
                    if len(self.food_items['items'])>0:
                        
                        self.display()
                        
                        break
                            
                    else:
                        print('You not choose any item please try again')  
                else:
                    print('select valid option')
                
                   
            except IndexError:
                print('Try again')
                
    def __total_sale(self,high=0):
        
        self.total_sale=sum(list(filter(lambda x : type(x)==int or type(x)==float , map(lambda x: x[4],self.order_details['orders']))))
        
        try:
            self.highest_bill_amount=max(list(filter(lambda x : type(x)==int or type(x)==float , map(lambda x: x[4],self.order_details['orders'])))) 
        except ValueError:
            self.highest_bill_amount=high                            
        print('The highest bill amount is :INR {} and total sale is :INR {}'.format(self.highest_bill_amount,self.total_sale))                            
       
    def sale_details(self):
        
        self.__total_sale()
                                         


def main_program():
    
    h=hotel_order_bill()
    #h.customer_order()
    
    h.menu_card()
    
    while(True):
        
        user=input('Enter S for Start and E for Exit :')[0].upper()
        
        if user=='E' and user.isalpha():
            print(h.order_details['orders'])
            h.sale_details()
            break
        
        elif user=='S' and user.isalpha():
            
            h.customer_order()
            
main_program()
