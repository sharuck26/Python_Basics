'''def mit(msg1, msg2):
    print("im " + msg1)
    return msg2


secrete_msg=mit('5' , 'natasha')
print(secrete_msg)'''


def sg(**temp):
    print(" good morning " + temp['msg1'])
    return temp['msg2']

secrete_msg=sg(msg2='5',msg1='natasa')
print(secrete_msg)
    
