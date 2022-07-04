##try:
##    a = int(input("enter a:"))
##    b = int(input("enter b :"))
##    c = a/b
##    print("a/b = %d" %c)
##except:
##    print("divison by zero is not possible.")
##else:
##    print("hi i am else block")
##try:
##    file = open("rgh.txt","r")
##finally:
##    file.close()
##    print("file closed")

##while(True):
##    try:
##        a=int(input("Input first no:"))
##        b=int(input("input second n0:"))
##        if a<=0 or b<0:
##            raise Exception("negative numbers not allowed! try again")
##        c=a/b
##        print("div is ", c)
##        break
##    except ValueError:
##        print("please input integers only! try again")
##    except ZeroDivisionError:
##        print("please input non-zero denominator")

b = lambda x:x * 2
print("The result is:",b(5))
