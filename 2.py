print("welcome to my bank")
cash=0 
end=1
while end :
    t=input("write 1 for puting money , 2 for checking balance and 3 for taking cash = ")
    if t == '1' :
        c=int(input(" how much money : "))
        cash+=c
    elif t== '3':
        c=int(input(" how much money : "))
        cash-=c
    elif t == '2' :
        print(cash)
    f=input("do you want to leave? 1 for yes and 2 for no: ")
    if f=="1" :
        end=0
print("youre welcome")