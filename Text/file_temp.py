def celsius_to_fahrenheit(t_celsius):
    if t_celsius > -273.15:
        return t_celsius*9/5+32
    else:
        return False

temperatures=[10,-20,-289,100]

with open("temperatures.txt","w+") as file:
    for temp in temperatures:
        if celsius_to_fahrenheit(temp):
            file.write(str(celsius_to_fahrenheit(temp))+'\n')
    file.seek(0)
    content = file.read()

print(content)
