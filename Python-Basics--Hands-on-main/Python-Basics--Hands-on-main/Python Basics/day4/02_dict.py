#data ={'name':'arjun', 'age':40, 'occ':'business', 'gender':'male'}

#print(data)
#print(data['name'])

#data['name']='mithun'
#print(data)
'''for x in data:
    print(x)
    
for x in data:
    print(data[x])'''

'''for x in data:
    print(x +':'+ str(data[x]))'''

'''data.update({'age':21})
print(data)'''

'''data.pop('occ')
print(data)'''

'''data.popitem()
print(data)'''

#temp= data.values()
#print(temp)

#temp = data.keys()
#print(temp)

data1={'digital':{"mithun": "goood boy"},'age': '20' ,'occ':'student'}


#print(data1['digital'])

temp=data1['digital']
temp2=temp['mithun']
print(temp2)
