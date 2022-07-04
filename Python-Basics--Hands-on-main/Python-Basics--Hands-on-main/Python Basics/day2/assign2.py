user_input = input("enter the value:")
user_input2 = input("want to check:")

if "yes" in user_input2:
    user_input3 = input("enter the word:")
    if user_input3 in user_input:
        print("checked")
    else:
        print("not found")
else:
  if "no" in user_input2:
        print("exit")

