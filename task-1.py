t=input("please enter something : ")
if t[0: ] in '-0123456789':
    print("integer")
elif ',' in t :
    print("list")
else :
    print("string")