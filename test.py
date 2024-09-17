total = 0
iterations = 0
list = []

with open('output.txt', 'r') as file:
    for line in file:
        # Split the line at the colon and get the part after it
        number = int(line.split(":")[1].strip())
        if(number < 14687):
            list.append(number)
            total = total + number
            iterations = iterations + 1
#list.sort()
print("Average = ", total / iterations)
print("Median = ", list[len(list)//2])
with open('output_sorted.txt', 'w') as file:
    for number in list:
        print(number, file = file)


# total = 0
# iterations = 0
# list = []
# with open('output_sorted.txt', 'r') as file:
#     for number in file:
#         number = int(number)
#         list.append(number)
#         total = total + number
#         iterations = iterations + 1
# list.sort()
# print("Average = ", total / iterations)
# print("Median = ", list[len(list)//2])