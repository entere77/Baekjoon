input_nums=[list(map(int, input().split())) for _ in range(9)]
max_value=0
max_row=0
max_column=0
for row in range(9):
    for column in range(9):
        if max_value<=input_nums[row][column]:
            max_value=input_nums[row][column]
            max_row=row+1
            max_column=column+1
print(max_value)
print(max_row,max_column)