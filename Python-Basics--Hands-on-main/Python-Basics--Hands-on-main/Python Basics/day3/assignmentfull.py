item_list =["dosa", "idli", "sambar", "juice", "cakes", "masalapuri", "samosa"]
print("###### CANTEEN ######")
user_input1 = input("want to order?")

user_input4 = input("Want to view the menu? yes/no:")
if "yes" in user_input4:
 
    
    data ={'dosa':'Rs20', 'idli':'rs10', 'sambar':'rs5', 'juice':'rs15', 'cakes':'rs40', 'masalapuri':'rs20', 'samosa': 'rs5'}
    [print (x + ':' + str(data[x])) for x in data]

if "yes" in user_input1:
    user_list=""
    total_items = int(input("how many items u want:"))
    for i in range(0,total_items):
        
        
        user_display_str ="Enter the item {}:"
        user_list=str(input(user_display_str.format(i+1)))

        
if user_list in item_list:
    print("YOUR ORDER IS TAKEN")
else:
    print( user_list +" " + "not found")
       
        
    user_input2 = input("insert an item :")
    
    user_input3 = input("remove an item :")
   
    item_list.insert(0,user_input2) 
    item_list.remove(user_input3)
    [print (x) for x in item_list]


if "no" in user_input1:
    print("Thank you")
