class Category:
    def __init__(self,name):
        self.name = name
        self.Deposit_list = [] 
        self.TotalDeposited = 0 
        


    def Statement(self,name): 
        print(name.center(30, '*'))  
        for i in self.Deposit_list: 
            print(i['Description'].ljust(23)[:23]+str(format(i['Amount'], '.2f')).rjust(7)[:7])
        print("Total: "+str(self.TotalDeposited))



    def Deposit(self,Amount,Description):
        self.Amount = Amount
        self.Description = Description
        self.Deposit_list.append({'Amount':Amount,'Description':Description})
        self.TotalDeposited += Amount
        self.Statement(self.name)
    
    

    def Withdraw(self,Amount,Description):
        if (self.Check_funds(Amount)):
            Amount = ((abs(Amount))*(-1)) 
            self.Deposit_list.append({'Amount':Amount,'Description':Description})
            self.TotalDeposited += Amount
            self.Statement(self.name)
    
    def Balance(self): 
        return print("Total: "+str(self.TotalDeposited))
    

    def Transfer(self,Amount,Category):
        if (self.Check_funds(Amount)): 
            Category.Deposit(Amount,"Transfer From "+Category.name)
            self.Withdraw(((abs(Amount))*(-1)),"Transfer To "+Category.name)

    def Check_funds(self,Amount):
         if 0 <=(self.TotalDeposited-Amount): 
             return True
         else:
             return False


Transaction_Food = Category('Food')
Transaction_Items = Category('Clothings') 
Transaction_Auto = Category('Clothingsss') 

Transaction_Food.Deposit(1000,'initial deposit')
Transaction_Food.Withdraw(10.15,'groceries')
Transaction_Food.Withdraw(15.89,'restaurant and more foo')
Transaction_Food.Transfer(50.00,Transaction_Items)



# def create_spend_chart(Categories):

#     i = 100
#     border = 0
#     retstr = ''

#     while (i >= -1000):
#         retstr += (str(i).rjust(3)+'| ')+" "+" "+" \n "
#         if (i <= 0 and border == 0):
#             retstr += '----------\n'.rjust(15)
#             border = 1 
#         i -= 10
#     maxlength = len(Categories[0].name)
#     for i in Categories:
#         maxlength = max(maxlength,len(i.name))
#     i = 0 
#     while(i <= maxlength):
#         retstr += 
#         i += 1
#     print(maxlength)

#     # return (retstr)
# print(create_spend_chart([Transaction_Food,Transaction_Items,Transaction_Auto]))


# # a = input()
# # for x in range (0,len(a)):
# #     print(a[x])