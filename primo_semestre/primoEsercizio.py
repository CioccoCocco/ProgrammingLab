list = [1, 2, 3, 4, 5, 6, 7, 8]

sum = 0

for number in list:
    sum += number
    
print(sum)

sum = sum(list)
print(sum)