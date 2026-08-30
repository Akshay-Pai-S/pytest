
try:
    file = open('myfile.txt', 'r')
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
finally:
    file.close()

print('***Using with***')

with open('myfile.txt', 'r') as file:
    # print(file.readline())
    # list2 = file.read().split('\n')
    # print(list2)
    for line in file:
        print(line.strip())