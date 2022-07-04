user_list=[]
total_items = int(input("how many items u want:"))
for i in range(0,total_items):
    user_display_str ="Enter the item {}:"
    user_list.append(str(input(user_display_str.format(i+1))))
print(user_list)
