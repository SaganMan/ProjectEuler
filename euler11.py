# Project Euler Problem 11
# Greatest product of four numbers in any direction in grid (grid.text)
# This is my worst code

numbers = [[] for i in range(20)]
no_index = 0
tmp = ''
with open('grid.txt', 'r') as f:
    for line in f:
        for x in range(len(line)):
            if line[x].isdigit():
                tmp += line[x]
            if len(tmp) == 2:
                numbers[no_index].append(int(tmp))
                tmp = ''
        no_index += 1
        line = ''

tmp_number = [1, 1]
max_number = [0, 0]

def FuncMax(tmp_number, max_number):
    for i in range(0, 2):
        max_number[i] = max(tmp_number[i], max_number[i])
        tmp_number[i] = 1

#The below is for horizantal and vertical multiplications
for i in range(0, 20):
    for j in range(0, 17):
        for n in range(j, j + 4):
            tmp_number[0] *= numbers[i][n]
            tmp_number[1] *= numbers[n][i]
        FuncMax(tmp_number, max_number)
print(max_number)
        
# The below is for Diagonal Multiplications
for s in range(0, 20):
    for j in range(s, 20):
        if j + 4 <= 20:
            for n in range(j, j + 4):
                tmp_number[0] *= numbers[n - s][n]
                tmp_number[1] *= numbers[n][n - s]
            FuncMax(tmp_number, max_number)

for l in range(0, 17):
    for i in range(3, 20):
        for j in range(l, 17):
            k = j + 4
            while i > 0:
                while j < k:
                    tmp_number[0] *= numbers[i][j]
                    i -= 1
                    j += 1
                    if j == k:
                        i = 0
                FuncMax(tmp_number, max_number)

print(max(max_number))
