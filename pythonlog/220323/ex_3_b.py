x = int(input("input x: "))
y = int(input("input y: "))

if(x > y):
    max = x
    min = y
else:
    max = y
    min = x
print(f"MAX = {max} MIN = {min}")