def fahrenheit(t_celsius):
    if t_celsius > -273.15:
        return t_celsius*9/5+32
    else:
        print('Not phisycally possible')

print(fahrenheit(25))
print(fahrenheit(-300))

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}

print(money['under_bed'][1])
temperatures=[10,-20,-289,100]
for temp in temperatures:
    print(fahrenheit(temp))
