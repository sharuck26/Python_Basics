actor = ["vj" , "surya" , "ak", "js"]
actress = ["dd", "sam" ,"tri", "sl"]

#print(actress[1:])

'''actor.insert(1,"mithun")
print(actor)

actor[-1:]=actress
print(actor)

print(actor+actress)'''

'''actor.extend(actress)
print(actor)'''

'''actor.remove("js")
print(actor)'''

#actor.pop(3)
#print(actor)

'''del actor[1]
print(actor)'''

"""actor.clear()
print(actor)"""

#[print (x) for x in actor]

'''newlist = []

for x in actor:
    if "a" in x:
        newlist.append(x)

print(newlist)'''


#[print (x) for x in actor if "a" in x]


'''newlist =[]
newlist = [x for x in actor if "a" in x ]
print(newlist)'''

'''newlist = []
newlist = [x for x in actor if "vj" not in x]
print(newlist)'''

'''newlist = []
newlist = [x.upper() for x in actor if "vj" not in x]
print(newlist)'''


'''newlist = []
newlist = ["ak" for x in actor ]
print(newlist)'''

'''newlist = []
newlist = [x if "surya" in x else "ak" for x in actor ]
print(newlist)'''

'''actor.sort()
print(actor)'''

'''actor.sort(reverse=True)
print(actor)'''

#print(actor.count("ak"))

#print(actor.index("vj"))

actor.update("loki")
