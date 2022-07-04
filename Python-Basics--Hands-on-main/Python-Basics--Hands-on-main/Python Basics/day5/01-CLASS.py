##class cse:
##    students=60
##
##section_a=cse()
##print(section_a.students)
   
##class cse:
##    def create_section(x):
##        students=x
##        print("created" + students)
##        return students
##
##
##section_a=cse.create_section("30")
##section_b=cse.create_section("20")
##
##print(section_b)

class lib:
    def __init__(self,a,b):
        self.book_name=a
        self.author=b
    def book_name_print(self,b):
        print("book name is" + self.book_name)
        return b*2

b1=lib('harry potter', 'jk')
print(b1.author)
print(b1.book_name_print(2))
