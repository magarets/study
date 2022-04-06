def add(*number):
    sum = 0
    for n in number:
        sum += n
    return sum

print(add(10, 20))
print(add(10, 20, 30))