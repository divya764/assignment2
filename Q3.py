data = input("enter customer heights : ")

def inchToCent(value):
    return value * 2.54

heights = data.split()

new_list = []

for x in heights:
    value = int(x)
    new_list.append(inchToCent(value))

print("show list : ", new_list)